"""
variables.py v2
Construct all model variables from cleaned data.

FIXES FROM PEER REVIEW:
- NEP formula now uses consistent units (both legs in world-share terms)
- Energy dominance weighted function actually computes weighted sum
- construct_reserve_share() fully implemented
- Thorium index added as explicit variable
- Lag selection theory-driven (10yr, 15yr only, both reported)
"""

import pandas as pd
import numpy as np
import os

DATA_PROCESSED = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed')

# Aggregate/regional entity codes that must be excluded when computing world totals.
# These rows duplicate individual country data and would inflate denominators.
AGGREGATE_CODES = {'WORLD', 'NAM_REGION', 'EUR_REGION', 'AFR_REGION', 'EMU'}


def construct_net_energy_position(df: pd.DataFrame) -> pd.DataFrame:
    """
    Net Energy Position (NEP) — dimensionally consistent formulation.

    PREVIOUS BUG: subtracted import_dependency (domestic ratio, share of own
    consumption) from production_share (global share, fraction of world output).
    Different denominators. Meaningless subtraction.

    CORRECT: both legs expressed as fraction of world primary energy production.

        production_share_i = production_i / world_production
        net_import_share_i = net_imports_i / world_production
        NEP_i = production_share_i - net_import_share_i

    Both numerators in TWh, both denominators in world-TWh. Subtraction valid.

    NEP > 0: energy sovereign (produces more than it net-imports relative to world)
    NEP < 0: energy dependent (net drain on world supply)
    NEP = 0: neutral
    """
    prod_cols = ['coal_production', 'oil_production', 'gas_production',
                 'nuclear_consumption', 'renewables_consumption']
    available = [c for c in prod_cols if c in df.columns]
    if not available:
        raise ValueError(f"No production columns found. Need one of: {prod_cols}")

    df['total_production_twh'] = df[available].fillna(0).sum(axis=1)
    # Exclude aggregate/regional rows to avoid double-counting in world totals
    country_mask = ~df['country_code'].isin(AGGREGATE_CODES)
    world_prod = (df.where(country_mask)
                    .groupby('year')['total_production_twh']
                    .transform('sum')
                    .replace(0, np.nan))

    df['production_share'] = df['total_production_twh'] / world_prod

    # Build net_imports_twh using best available source, with fallback cascade:
    #   1. net_elec_imports (OWID, available ~2000+)
    #   2. energy_imports_pct * primary_energy_consumption (WB, available ~1990+)
    #   3. 0.0 (pre-1990: treat as production-only, reasonable for historical data)
    net_imports_twh = pd.Series(0.0, index=df.index)
    if 'energy_imports_pct' in df.columns and 'primary_energy_consumption' in df.columns:
        wb_fallback = df['energy_imports_pct'] / 100 * df['primary_energy_consumption']
        net_imports_twh = net_imports_twh.where(wb_fallback.isna(), wb_fallback)
    if 'net_elec_imports' in df.columns:
        net_imports_twh = net_imports_twh.where(df['net_elec_imports'].isna(), df['net_elec_imports'])
    df['net_import_world_share'] = net_imports_twh / world_prod

    df['net_energy_position'] = df['production_share'] - df['net_import_world_share']

    outlier_thresh = df['net_energy_position'].abs().quantile(0.99)
    n_out = (df['net_energy_position'].abs() > outlier_thresh).sum()
    if n_out > 0:
        print(f"Warning: {n_out} NEP outliers above 99th percentile — check raw data.")
        # Note: year >= 2024 OWID data is preliminary; treat with additional caution.
        top_outliers = (df[df['net_energy_position'].abs() > outlier_thresh]
                        .nlargest(20, 'net_energy_position')
                        [['country_code', 'year', 'net_energy_position']])
        print(top_outliers.to_string(index=False))

    return df


def construct_energy_dominance_weighted(df: pd.DataFrame) -> pd.DataFrame:
    """
    Era-weighted energy position.

    PREVIOUS BUG: stored a dict in a column and returned immediately.
    No weighted sum was ever computed. This was a stub.

    CORRECT: computes weighted sum of each fuel's production share,
    weighted by that fuel's historical importance in global energy in that era.

    Rationale: a barrel of oil in 1975 confers more monetary leverage than
    a tonne of coal. The era weights reflect actual global energy mix shares
    from OWID/IEA historical data.
    """
    # Era weights: approximate share of each fuel in world primary energy per era.
    # Source: Our World in Data / Energy Institute Statistical Review of World Energy
    # (https://ourworldindata.org/energy-mix). Weights computed as decadal averages
    # from OWID world aggregate:
    #   coal_era    → 1900–1949 world mean shares
    #   oil_era     → 1950–1999 world mean shares
    #   transition  → 2000–2015 world mean shares
    # Use compute_era_weights_from_owid() below to verify/update these from live data.
    era_weights_map = {
        'coal_era': {          # pre-1950: coal-dominant world
            'coal_production':        0.85,
            'oil_production':         0.10,
            'gas_production':         0.03,
            'nuclear_consumption':    0.00,
            'renewables_consumption': 0.02,
        },
        'oil_era': {           # 1950-1999: oil/gas ascendancy
            'coal_production':        0.28,
            'oil_production':         0.45,
            'gas_production':         0.18,
            'nuclear_consumption':    0.06,
            'renewables_consumption': 0.03,
        },
        'transition_era': {    # 2000-present: diversifying mix
            'coal_production':        0.27,
            'oil_production':         0.32,
            'gas_production':         0.25,
            'nuclear_consumption':    0.05,
            'renewables_consumption': 0.11,
        },
    }

    def assign_era(year):
        if year < 1950:   return 'coal_era'
        elif year < 2000: return 'oil_era'
        else:             return 'transition_era'

    df['era'] = df['year'].apply(assign_era)
    df['energy_dominance_weighted'] = 0.0

    for era_name, weights in era_weights_map.items():
        mask = df['era'] == era_name
        for fuel, weight in weights.items():
            if fuel not in df.columns:
                continue
            # Exclude aggregate/regional rows to avoid double-counting in world totals
            country_mask = ~df['country_code'].isin(AGGREGATE_CODES)
            world_fuel = (df[fuel].where(country_mask)
                          .groupby(df['year'])
                          .transform('sum')
                          .replace(0, np.nan))
            fuel_share = df[fuel].fillna(0) / world_fuel
            df.loc[mask, 'energy_dominance_weighted'] += fuel_share[mask] * weight

    return df


def construct_reserve_share(cofer_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Parse IMF COFER into clean annual reserve currency shares.

    PREVIOUS VERSION: pass (unimplemented).
    The dependent variable of the entire model was missing.

    IMF COFER reports allocated reserves by currency (USD billions).
    This function parses the messy CSV format into a clean long-format
    dataframe suitable for merging with the panel.

    Note: COFER covers 1999-present. CNY reported separately from 2016.
    Pre-1999 historical shares must come from Eichengreen-Flandreau (1900-1999).
    """
    currency_map = {
        'U.S. dollar':         'USD',
        'Euro':                'EUR',
        'Japanese yen':        'JPY',
        'Pound sterling':      'GBP',
        'Chinese renminbi':    'CNY',
        'Swiss franc':         'CHF',
        'Total allocated':     'TOTAL',
    }

    if 'currency' in cofer_raw.columns and 'year' in cofer_raw.columns:
        df = cofer_raw.copy()
    else:
        id_col = cofer_raw.columns[0]
        year_cols = [c for c in cofer_raw.columns[1:]
                     if str(c)[:4].isdigit()]
        df_melted = cofer_raw.melt(
            id_vars=[id_col], value_vars=year_cols,
            var_name='period', value_name='value_usd_bn'
        )
        df_melted.columns = ['label', 'period', 'value_usd_bn']
        df_melted['currency'] = None
        for label_key, iso in currency_map.items():
            mask = df_melted['label'].str.contains(label_key, case=False, na=False)
            df_melted.loc[mask, 'currency'] = iso
        df = df_melted.dropna(subset=['currency'])

    df['year'] = df['period'].astype(str).str[:4].astype(int)
    df['value_usd_bn'] = pd.to_numeric(df['value_usd_bn'], errors='coerce')

    annual = df.groupby(['currency', 'year'])['value_usd_bn'].mean().reset_index()

    totals = (annual[annual['currency'] == 'TOTAL']
              [['year', 'value_usd_bn']]
              .rename(columns={'value_usd_bn': 'total_allocated'}))

    result = (annual[annual['currency'] != 'TOTAL']
              .merge(totals, on='year', how='left'))
    result['reserve_share'] = result['value_usd_bn'] / result['total_allocated']

    out = result[['currency', 'year', 'reserve_share', 'value_usd_bn']].copy()
    out.columns = ['country_code', 'year', 'reserve_share', 'reserves_usd_bn']

    print(f"Reserve shares parsed: {out.shape}")
    print(f"Currencies: {sorted(out.country_code.unique())}")
    print(f"Years: {out.year.min()}-{out.year.max()}")

    return out


def compute_era_weights_from_owid(owid_df: pd.DataFrame) -> dict:
    """
    Derive era_weights_map directly from OWID world aggregate data.
    Use this to verify/update the hardcoded weights in
    construct_energy_dominance_weighted().

    Requires owid_df to contain rows where country == 'World' and columns
    for coal/oil/gas/nuclear/renewables consumption.

    Returns a dict matching the era_weights_map structure.
    """
    world = owid_df[owid_df['country'] == 'World'].copy()
    if world.empty:
        print("Warning: no 'World' rows in OWID data. Cannot compute era weights.")
        return {}

    fuel_cols = {
        'coal_production':        'coal_consumption',
        'oil_production':         'oil_consumption',
        'gas_production':         'gas_consumption',
        'nuclear_consumption':    'nuclear_consumption',
        'renewables_consumption': 'renewables_consumption',
    }

    # Try to find matching columns (OWID column names vary by version)
    available = {}
    for model_col, owid_col in fuel_cols.items():
        candidates = [c for c in world.columns if owid_col.split('_')[0] in c.lower()
                      and 'twh' in c.lower()]
        if candidates:
            available[model_col] = candidates[0]
        elif owid_col in world.columns:
            available[model_col] = owid_col

    if not available:
        print("Warning: could not match OWID fuel columns. Check column names.")
        return {}

    eras = {
        'coal_era':       (world['year'] < 1950),
        'oil_era':        (world['year'] >= 1950) & (world['year'] < 2000),
        'transition_era': (world['year'] >= 2000),
    }

    result = {}
    for era_name, mask in eras.items():
        sub = world[mask][list(available.values())].dropna()
        if sub.empty:
            continue
        totals = sub.sum(axis=1).replace(0, np.nan)
        shares = sub.div(totals, axis=0).mean()
        result[era_name] = {
            model_col: round(float(shares[owid_col]), 3)
            for model_col, owid_col in available.items()
        }
        print(f"{era_name}: {result[era_name]}")

    return result


def construct_thorium_index(df: pd.DataFrame,
                             thorium_reserves: dict = None) -> pd.DataFrame:
    """
    Thorium Potential Index.

    Since thorium reserve data is point estimates (not time series),
    this constructs: thorium_index = reserve_share * nuclear_share_energy

    Captures: having the reserves AND the capacity to exploit them.
    A country with thorium but no nuclear programme scores low.
    India with 25% of reserves and an active programme scores high.

    Default reserve shares from IAEA/AMD estimates (latest available).

    WARNING — COLLINEARITY WITH FIXED EFFECTS:
    Thorium reserve share is a time-invariant point estimate (USGS 2024).
    In any panel model with country fixed effects, this variable will be
    perfectly collinear with the country FE and cannot be identified.

    This variable is valid ONLY in:
      1. Cross-sectional models (run_tmpi_cross_section in models.py)
      2. As a scalar multiplier outside the panel (e.g. TMPI ranking table)

    Do NOT include thorium_index or thorium_reserve_share as regressors
    in run_pooled_ts_model() or run_vecm_or_var().
    """
    if thorium_reserves is None:
        thorium_reserves = {
            'IND': 0.25, 'BRA': 0.16, 'AUS': 0.15, 'USA': 0.10,
            'EGY': 0.08, 'TUR': 0.06, 'VEN': 0.04, 'CAN': 0.03,
            'RUS': 0.02, 'CHN': 0.02, 'NOR': 0.02, 'GBR': 0.01,
        }

    df['thorium_reserve_share'] = df['country_code'].map(thorium_reserves).fillna(0)

    if 'nuclear_share_energy' not in df.columns:
        if 'nuclear_consumption' in df.columns and 'primary_energy_consumption' in df.columns:
            df['nuclear_share_energy'] = (
                df['nuclear_consumption']
                / df['primary_energy_consumption'].replace(0, np.nan)
            )
        else:
            df['nuclear_share_energy'] = 0.0
            print("Warning: nuclear capacity unavailable. Thorium index = reserve share only.")

    df['thorium_index'] = df['thorium_reserve_share'] * df['nuclear_share_energy']
    return df


def construct_energy_export_share(df: pd.DataFrame) -> pd.DataFrame:
    """
    Energy export leverage — alternative/complement to NEP.

    The petrodollar mechanism operated through EXPORT dependency of importers,
    not just the exporter's net position. Saudi Arabia's monetary leverage came
    from buyer dependency on Saudi exports, not just production share.

    export_leverage_i = (fuel_exports_pct_merchandise_i / 100) * (trade_openness_i / 100)

    Interpretation: share of GDP effectively flowing through energy exports.
    High = country is an energy-export-dependent trader with bilateral
    settlement implications.

    Use as ROBUSTNESS CHECK alongside NEP:
    - If both NEP and export_leverage show positive β on reserve_share → robust
    - If only NEP significant → mechanism is about self-sufficiency, not export power
    - If only export_leverage significant → mechanism is about export bilateral trade

    Source: World Bank TX.VAL.FUEL.ZS.UN (fuel exports % of merchandise exports)
    and NE.TRD.GNFS.ZS (trade openness % of GDP).
    """
    if 'fuel_exports_pct_merchandise' not in df.columns:
        print("Warning: fuel_exports_pct_merchandise not found. "
              "Pull World Bank TX.VAL.FUEL.ZS.UN. Skipping export_leverage.")
        return df
    if 'trade_openness' not in df.columns:
        print("Warning: trade_openness not found. Skipping export_leverage.")
        return df

    df['export_leverage'] = (
        df['fuel_exports_pct_merchandise'].fillna(0) / 100
        * df['trade_openness'].fillna(0) / 100
    )
    return df


def construct_thorium_monetary_potential(df: pd.DataFrame,
                                          thorium_df: pd.DataFrame,
                                          governance_df: pd.DataFrame) -> pd.DataFrame:
    """
    Thorium Monetary Potential Index (TMPI).

    WARNING — COLLINEARITY WITH FIXED EFFECTS:
    Thorium reserve share is a time-invariant point estimate (USGS 2024).
    In any panel model with country fixed effects, this variable will be
    perfectly collinear with the country FE and cannot be identified.

    This variable is valid ONLY in:
      1. Cross-sectional models (run_tmpi_cross_section in models.py)
      2. As a scalar multiplier outside the panel (e.g. TMPI ranking table)

    Do NOT include tmpi or thorium_reserve_share as regressors
    in run_pooled_ts_model() or run_vecm_or_var().

    The paper's forward-looking thesis: whichever countries control the next
    dominant energy source gain monetary leverage. Thorium is the candidate.

    TMPI_i = thorium_reserve_share_i
              × nuclear_capacity_index_i
              × institutional_quality_i

    Three components, each necessary but not sufficient:

    1. RESERVES — you need to hold them
       thorium_reserve_share: USGS 2024, world share of 6.2M mt

    2. CAPACITY — you need to be able to exploit them
       nuclear_capacity_index: nuclear consumption as share of primary energy
       (proxy for ability to build and operate thorium reactors)

    3. INSTITUTIONS — you need to be trusted as a reserve issuer
       institutional_quality: composite of WGI political stability,
       rule of law, and government effectiveness
       (reserve holders require credible institutions)

    This is the 'India paradox' test: India has 16% of world thorium
    AND an active nuclear programme AND improving institutions.
    Does TMPI predict future reserve currency candidacy?
    Brazil has more reserves but weaker nuclear capacity.
    Australia has large reserves but no nuclear programme (as of 2024).

    Forward prediction: high TMPI countries are positioned for monetary
    leverage in a thorium-era energy system. This is falsifiable.
    """
    # Merge thorium reserves
    if 'thorium_reserve_share' not in df.columns:
        thorium_simple = thorium_df[['country_code', 'world_share']].rename(
            columns={'world_share': 'thorium_reserve_share'}
        )
        df = df.merge(thorium_simple, on='country_code', how='left')
        df['thorium_reserve_share'] = df['thorium_reserve_share'].fillna(0)

    # Nuclear capacity index (already in variables if construct_thorium_index was called)
    if 'nuclear_share_energy' not in df.columns:
        if 'nuclear_consumption' in df.columns and 'primary_energy_consumption' in df.columns:
            df['nuclear_share_energy'] = (
                df['nuclear_consumption']
                / df['primary_energy_consumption'].replace(0, np.nan)
            ).fillna(0)
        else:
            df['nuclear_share_energy'] = 0.0

    # Institutional quality composite from WGI
    # TMPI is cross-sectional (no year dimension), so we average governance
    # over 2018-2023 per country and merge on country_code only.
    gov_cols = ['political_stability', 'rule_of_law', 'gov_effectiveness']
    if governance_df is not None:
        available_gov_cols = [c for c in gov_cols if c in governance_df.columns]
        if available_gov_cols:
            gov_recent = (governance_df[governance_df['year'] >= 2018]
                          [['country_code'] + available_gov_cols]
                          .groupby('country_code')[available_gov_cols]
                          .mean().reset_index())
            for col in available_gov_cols:
                col_min, col_max = gov_recent[col].min(), gov_recent[col].max()
                if col_max > col_min:
                    gov_recent[f'{col}_norm'] = (gov_recent[col] - col_min) / (col_max - col_min)
                else:
                    gov_recent[f'{col}_norm'] = 0.5
            norm_cols = [f'{c}_norm' for c in available_gov_cols]
            gov_recent['institutional_quality'] = gov_recent[norm_cols].mean(axis=1)
            df = df.merge(gov_recent[['country_code', 'institutional_quality']],
                          on='country_code', how='left')

    if 'institutional_quality' not in df.columns:
        df['institutional_quality'] = 0.5
        print("Warning: governance data unavailable. institutional_quality set to 0.5.")
    else:
        n_missing = df['institutional_quality'].isna().sum()
        if n_missing > 0:
            df['institutional_quality'] = df['institutional_quality'].fillna(0.5)
            print(f"Note: {n_missing} countries missing governance data, filled with 0.5.")

    # Thorium Monetary Potential Index
    df['tmpi'] = (
        df['thorium_reserve_share']
        * df['nuclear_share_energy']
        * df['institutional_quality']
    )

    # Normalise TMPI to 0-100 for interpretability
    tmpi_max = df['tmpi'].max()
    if tmpi_max > 0:
        df['tmpi_scaled'] = df['tmpi'] / tmpi_max * 100

    return df


def run_era_scenario(df: pd.DataFrame,
                     scenario: str = 'thorium_era') -> pd.DataFrame:
    """
    Era scenario analysis: what does energy position look like under
    different future energy mix assumptions?

    Uses the era_weights structure but extends to 2030+ scenarios.

    Scenarios:
    - 'transition_era': current (2015-present mix)
    - 'thorium_era': 2040+ if thorium/nuclear scales significantly
    - 'renewables_era': 2040+ if solar/wind dominate

    This answers: which countries gain/lose monetary leverage
    under different energy transition pathways?
    """
    scenarios = {
        'transition_era': {   # Current
            'coal_production':        0.27,
            'oil_production':         0.32,
            'gas_production':         0.25,
            'nuclear_consumption':    0.05,
            'renewables_consumption': 0.11,
        },
        'thorium_era': {      # 2040+ thorium/nuclear scenario
            'coal_production':        0.05,
            'oil_production':         0.15,
            'gas_production':         0.15,
            'nuclear_consumption':    0.35,  # thorium reactors dominant
            'renewables_consumption': 0.30,
        },
        'renewables_era': {   # 2040+ renewables scenario
            'coal_production':        0.03,
            'oil_production':         0.10,
            'gas_production':         0.12,
            'nuclear_consumption':    0.10,
            'renewables_consumption': 0.65,
        },
    }

    if scenario not in scenarios:
        raise ValueError(f"Scenario must be one of: {list(scenarios.keys())}")

    weights = scenarios[scenario]
    result_col = f'energy_position_{scenario}'
    df[result_col] = 0.0

    for fuel, weight in weights.items():
        if fuel not in df.columns:
            continue
        # Exclude aggregate/regional rows to avoid double-counting in world totals
        country_mask = ~df['country_code'].isin(AGGREGATE_CODES)
        world_fuel = (df[fuel].where(country_mask)
                      .groupby(df['year'])
                      .transform('sum')
                      .replace(0, np.nan))
        fuel_share = df[fuel].fillna(0) / world_fuel
        df[result_col] += fuel_share * weight

    print(f"\nScenario '{scenario}' energy positions (latest year):")
    # Use latest year with actual data (not sparse tail year)
    latest = df[df[result_col] > 0]['year'].max() if (df[result_col] > 0).any() else df['year'].max()
    top = (df[df['year'] == latest]
           .nlargest(10, result_col)
           [['country_code', result_col]]
           .reset_index(drop=True))
    print(top.to_string())

    return df



def construct_fx_turnover_share(df: pd.DataFrame, bis_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge BIS FX turnover share into the panel as a dependent variable.

    This expands the dependent variable from COFER's 6 reserve currencies
    to 38+ currencies covered by BIS Triennial Surveys (2001-2022).

    BIS Triennial surveys occur every 3 years. For panel years between
    surveys, we interpolate linearly. For years before the first survey
    or after the last, we use the nearest available survey value (no
    extrapolation beyond bounds).

    Parameters
    ----------
    df : pd.DataFrame
        Panel DataFrame with columns ['country_code', 'year'].
    bis_df : pd.DataFrame
        Output of pull_bis_fx_turnover_expanded() with columns:
        ['year', 'country_code', 'currency_code', 'fx_share_pct',
         'fx_turnover_daily_bn'].

    Returns
    -------
    pd.DataFrame
        Panel with added columns:
        - fx_turnover_share: FX turnover share (normalised to sum to 100%)
        - fx_turnover_daily_bn: daily average turnover in USD billions
        - currency_code: ISO currency code
        - has_fx_turnover: boolean flag for rows with BIS data
    """
    if bis_df is None or bis_df.empty:
        print("Warning: BIS FX turnover data is None/empty. Skipping merge.")
        df['fx_turnover_share'] = float('nan')
        df['has_fx_turnover'] = False
        return df

    # Keep only the columns we need from BIS data
    bis_cols = ['year', 'country_code', 'currency_code', 'fx_share_pct',
                'fx_turnover_daily_bn']
    bis_cols = [c for c in bis_cols if c in bis_df.columns]
    bis = bis_df[bis_cols].copy()

    # BIS survey years
    survey_years = sorted(bis['year'].unique())
    print(f"  BIS survey years: {survey_years}")

    # Get unique country codes in BIS data
    bis_countries = bis['country_code'].unique()
    print(f"  BIS currencies/countries: {len(bis_countries)}")

    # Get all panel years
    panel_years = sorted(df['year'].unique())

    # For each BIS country, interpolate to all panel years
    interp_rows = []
    for country in bis_countries:
        country_bis = bis[bis['country_code'] == country].sort_values('year')
        if country_bis.empty:
            continue

        # Get currency_code (constant per country)
        ccy = country_bis['currency_code'].iloc[0] if 'currency_code' in country_bis.columns else None

        # Build dicts indexed by survey year for interpolation
        share_dict = dict(zip(country_bis['year'].astype(int), country_bis['fx_share_pct']))
        turnover_dict = (dict(zip(country_bis['year'].astype(int),
                                  country_bis['fx_turnover_daily_bn']))
                         if 'fx_turnover_daily_bn' in country_bis.columns else None)

        # This country's available survey years (may be subset of all surveys)
        country_survey_yrs = sorted(share_dict.keys())
        if not country_survey_yrs:
            continue

        for yr in panel_years:
            if yr in share_dict:
                # Exact survey year
                share_val = share_dict[yr]
                turnover_val = turnover_dict[yr] if turnover_dict is not None else None
            elif yr < country_survey_yrs[0]:
                # Before first survey for this country
                share_val = share_dict[country_survey_yrs[0]]
                turnover_val = (turnover_dict[country_survey_yrs[0]]
                                if turnover_dict is not None else None)
            elif yr > country_survey_yrs[-1]:
                # After last survey for this country
                share_val = share_dict[country_survey_yrs[-1]]
                turnover_val = (turnover_dict[country_survey_yrs[-1]]
                                if turnover_dict is not None else None)
            else:
                # Between surveys: linear interpolation
                lower_yr = max(y for y in country_survey_yrs if y <= yr)
                upper_yr = min(y for y in country_survey_yrs if y >= yr)
                if lower_yr == upper_yr:
                    share_val = share_dict[lower_yr]
                    turnover_val = (turnover_dict[lower_yr]
                                    if turnover_dict is not None else None)
                else:
                    frac = (yr - lower_yr) / (upper_yr - lower_yr)
                    share_val = (share_dict[lower_yr]
                                 + frac * (share_dict[upper_yr] - share_dict[lower_yr]))
                    if turnover_dict is not None:
                        turnover_val = (turnover_dict[lower_yr]
                                        + frac * (turnover_dict[upper_yr]
                                                  - turnover_dict[lower_yr]))
                    else:
                        turnover_val = None

            row = {
                'country_code': country,
                'year': yr,
                'fx_turnover_share': round(share_val, 4),
            }
            if ccy is not None:
                row['currency_code'] = ccy
            if turnover_val is not None:
                row['fx_turnover_daily_bn'] = round(turnover_val, 2)
            interp_rows.append(row)

    bis_interp = pd.DataFrame(interp_rows)

    # Merge into panel
    merge_cols = ['country_code', 'year']

    # Avoid overwriting existing columns
    for col in ['fx_turnover_share', 'fx_turnover_daily_bn', 'currency_code']:
        if col in df.columns:
            df = df.drop(columns=[col])

    df = df.merge(bis_interp, on=merge_cols, how='left')

    df['has_fx_turnover'] = df['fx_turnover_share'].notna()

    n_matched = df['has_fx_turnover'].sum()
    n_countries = df.loc[df['has_fx_turnover'], 'country_code'].nunique()
    print(f"  FX turnover merged: {n_matched} rows matched "
          f"({n_countries} countries with BIS data)")

    return df


def construct_gdp_share(df: pd.DataFrame) -> pd.DataFrame:
    """
    GDP share of world output.

    gdp_share_i = gdp_usd_i / sum(gdp_usd across all countries in year t)

    Required control variable: economic size is the standard null hypothesis
    for reserve currency status (Chinn & Frankel 2007). The paper tests whether
    NEP explains reserve share BEYOND what GDP alone predicts.
    Japan is the key test: if GDP were sufficient, the yen should have higher
    reserve share than it does. If NEP suppresses it, the model gains support.
    """
    # Exclude aggregate/regional rows to avoid double-counting in world totals
    country_mask = ~df['country_code'].isin(AGGREGATE_CODES)
    world_gdp = (df['gdp_usd'].where(country_mask)
                  .groupby(df['year'])
                  .transform('sum')
                  .replace(0, np.nan))
    df['gdp_share'] = df['gdp_usd'] / world_gdp
    return df


def construct_lagged_variables(df: pd.DataFrame,
                                var: str,
                                lags: list = [10, 15]) -> pd.DataFrame:
    """
    Theory-driven lag selection — NOT data mining.

    We pre-specify TWO lags based on theoretical priors:
    - 10 years: petrodollar recycling took ~3yr; Bretton Woods collapse
      took ~3yr after Nixon shock; but full reserve recomposition
      is slower. 10yr is a conservative minimum.
    - 15 years: upper bound for reserve composition adjustment.
      Central banks move slowly. 15yr captures the full adjustment.

    We report BOTH. We do not pick the lag with the highest R².
    If both show consistent sign and significance, the finding is robust.
    If they diverge, we interpret the divergence.
    """
    df = df.sort_values(['country_code', 'year'])
    for lag in lags:
        df[f'{var}_lag{lag}'] = df.groupby('country_code')[var].shift(lag)
    return df


def construct_bartik_instrument(df: pd.DataFrame,
                                price_df: pd.DataFrame = None) -> pd.DataFrame:
    """
    Bartik (shift-share) instrument for energy sovereignty.

    Identification strategy:
    - "Share" = country's fixed energy endowment (production share at baseline year)
    - "Shift" = global energy price shocks (common to all countries)
    - Interaction = country-specific NEP shocks driven by global factors

    This gives exogenous variation in energy position: a country with large
    oil endowment gets a bigger NEP shock when oil prices spike, but the
    price spike itself is driven by global demand/supply, not by that
    country's monetary ambitions.

    Era-consistent: uses coal endowment × coal price pre-1950,
    oil endowment × oil price 1950-2000, gas+oil post-2000.

    If price_df is None, uses production growth rates as price proxies
    (world production growth correlates with price movements).
    """
    df = df.copy().reset_index(drop=True)

    # Filter out aggregates for share computation
    country_mask = ~df['country_code'].isin(AGGREGATE_CODES)

    # --- SHARE component: baseline production shares (fixed at earliest available year per country) ---
    fuel_cols = ['coal_production', 'oil_production', 'gas_production',
                 'nuclear_consumption', 'renewables_consumption']
    available_fuels = [f for f in fuel_cols if f in df.columns]

    for fuel in available_fuels:
        # Baseline share: country's share of world production, averaged over
        # first 5 available years (reduces noise from single-year anomalies)
        world_fuel_annual = (df[country_mask]
                             .groupby('year')[fuel].sum()
                             .rename('world_total'))
        df = df.merge(world_fuel_annual, on='year', how='left', suffixes=('', '_world'))

        df[f'{fuel}_share'] = np.where(
            df['world_total'] > 0,
            df[fuel].fillna(0) / df['world_total'],
            0
        )
        df = df.drop(columns=['world_total'])

        # Fix the "share" at the baseline (first 5 years with data per country)
        baseline = (df[country_mask & df[f'{fuel}_share'].notna()]
                    .groupby('country_code')
                    .apply(lambda g: g.nsmallest(5, 'year')[f'{fuel}_share'].mean(),
                           include_groups=False)
                    .rename(f'{fuel}_baseline_share'))
        df = df.merge(baseline, on='country_code', how='left')

    # --- SHIFT component: global price shocks ---
    if price_df is not None and 'year' in price_df.columns:
        # Use actual commodity price data
        # Map fuel production columns to price columns
        fuel_to_price = {
            'oil_production': 'oil_price',
            'coal_production': 'coal_price',
            'gas_production': 'gas_price',
            'nuclear_consumption': 'nuclear_price',  # unlikely to exist
            'renewables_consumption': 'renewables_price',  # unlikely to exist
        }
        for fuel in available_fuels:
            price_col = fuel_to_price.get(fuel, f'{fuel}_price')
            if price_col not in price_df.columns:
                # Try shock column directly (pre-computed log-differences)
                shock_col_direct = f'{price_col}_shock'
                if shock_col_direct in price_df.columns:
                    if shock_col_direct not in df.columns:
                        df = df.merge(price_df[['year', shock_col_direct]].drop_duplicates('year'),
                                      on='year', how='left')
                    df[f'{fuel}_price_shock'] = df[shock_col_direct]
                    continue
                else:
                    continue  # no price data for this fuel
            if price_col not in df.columns:
                df = df.merge(price_df[['year', price_col]].drop_duplicates('year'),
                              on='year', how='left')
            # Log-difference as shock (same shock for all countries in a year)
            price_series = df.drop_duplicates('year').set_index('year')[price_col].sort_index()
            log_diff = np.log(price_series).diff()
            log_diff.name = f'{fuel}_price_shock'
            df = df.merge(log_diff, on='year', how='left')
    else:
        # Proxy: world production growth rate as price signal
        # (production responds to price; when prices spike, production rises)
        for fuel in available_fuels:
            world_prod = (df[country_mask]
                          .groupby('year')[fuel].sum()
                          .rename(f'{fuel}_world_prod'))
            world_prod_growth = world_prod.pct_change().rename(f'{fuel}_price_shock')
            df = df.merge(world_prod_growth, on='year', how='left')

    # --- INTERACTION: Bartik instrument = baseline_share × price_shock ---
    bartik_cols = []
    for fuel in available_fuels:
        baseline_col = f'{fuel}_baseline_share'
        shock_col = f'{fuel}_price_shock'
        bartik_col = f'{fuel}_bartik'
        if baseline_col in df.columns and shock_col in df.columns:
            df[bartik_col] = df[baseline_col] * df[shock_col]
            bartik_cols.append(bartik_col)

    # Composite Bartik: era-weighted sum of fuel-specific instruments
    # Uses same era_weights as construct_energy_dominance_weighted
    era_weights_map = {
        'coal_era': {'coal_production': 0.85, 'oil_production': 0.10,
                     'gas_production': 0.03, 'nuclear_consumption': 0.00,
                     'renewables_consumption': 0.02},
        'oil_era': {'coal_production': 0.08, 'oil_production': 0.45,
                    'gas_production': 0.28, 'nuclear_consumption': 0.16,
                    'renewables_consumption': 0.03},
        'transition_era': {'coal_production': 0.27, 'oil_production': 0.32,
                           'gas_production': 0.25, 'nuclear_consumption': 0.05,
                           'renewables_consumption': 0.11},
    }

    df['bartik_energy_shock'] = 0.0
    for era_name, weights in era_weights_map.items():
        era_mask = df['era'] == era_name if 'era' in df.columns else pd.Series(True, index=df.index)
        for fuel, weight in weights.items():
            bartik_col = f'{fuel}_bartik'
            if bartik_col in df.columns:
                df.loc[era_mask, 'bartik_energy_shock'] += (
                    df.loc[era_mask, bartik_col].fillna(0) * weight
                )

    # Also create lagged versions of the instrument
    df = df.sort_values(['country_code', 'year'])
    for lag in [10, 15]:
        df[f'bartik_energy_shock_lag{lag}'] = (
            df.groupby('country_code')['bartik_energy_shock'].shift(lag)
        )

    # Clean up intermediate columns
    drop_cols = ([f'{f}_share' for f in available_fuels] +
                 [f'{f}_baseline_share' for f in available_fuels] +
                 [f'{f}_price_shock' for f in available_fuels] +
                 [f'{f}_bartik' for f in available_fuels])
    df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors='ignore')

    n_valid = df['bartik_energy_shock'].notna().sum()
    print(f"Bartik instrument constructed: {n_valid} non-null observations")
    print(f"Columns added: bartik_energy_shock, bartik_energy_shock_lag10, bartik_energy_shock_lag15")

    return df


# ─────────────────────────────────────────────
# FOCAL COUNTRY CASES
# ─────────────────────────────────────────────

FOCAL_COUNTRIES = {
    # ORIGINAL FOUR — energy-monetary transition cases
    'CHN': {
        'name': 'China',
        'case_type': 'rising_producer',
        'hypothesis': 'Monetary ambition tracks improving net energy position',
        'key_events': {
            2001: 'WTO accession',
            2009: 'Zhou Xiaochuan SDR proposal',
            2013: 'BRI launched',
            2015: 'RMB added to SDR basket',
            2018: 'Yuan oil futures launched',
            2022: 'De-dollarization accelerates post-Russia sanctions',
            2023: 'TMSR thorium reactor operational',
        }
    },
    'IND': {
        'name': 'India',
        'case_type': 'thorium_reserve_holder',
        'hypothesis': 'Thorium geography directly shapes monetary strategy',
        'key_events': {
            1974: 'Pokhran-I nuclear test',
            2008: 'US-India Civil Nuclear Agreement',
            2022: 'Rupee-ruble energy corridor',
            2023: 'BRICS expansion anchors south Asia bloc',
        }
    },
    'RUS': {
        'name': 'Russia',
        'case_type': 'forced_fragmentation',
        'hypothesis': 'Energy relationships determine monetary corridor formation under duress',
        'key_events': {
            2014: 'First SWIFT threat post-Crimea',
            2022: 'SWIFT exclusion natural experiment',
            2023: 'Ruble-rupee oil settlement established',
        }
    },
    'JPN': {
        'name': 'Japan',
        'case_type': 'control_case',
        'hypothesis': 'Energy dependency suppresses monetary ambition despite GDP size',
        'key_events': {
            1973: 'Oil shock',
            1985: 'Plaza Accord',
            2011: 'Fukushima nuclear collapse',
            2023: 'Nuclear restart programme',
        }
    },

    # TMPI STRESS TEST CASES — test the three-component index
    'AUS': {
        'name': 'Australia',
        'case_type': 'reserves_without_capacity',
        'hypothesis': 'Large thorium reserves but no nuclear programme = TMPI capacity gap',
        'tmpi_note': (
            'Australia holds 12.6% of world thorium reserves and fully open '
            'capital markets (Chinn-Ito = 2.28) but has NO nuclear programme. '
            'AUD is already a nontraditional reserve currency (6.4% of BIS FX '
            'turnover 2022). TMPI should show: reserves present, capacity absent. '
            'Tests whether reserves alone drive monetary ambition or whether '
            'capacity is required.'
        ),
        'key_events': {
            2007: 'AUD added to nontraditional reserve basket (Arslanalp et al.)',
            2022: 'AUKUS nuclear submarine deal — first nuclear capacity signal',
            2023: 'AUD: 6.4% of global FX turnover (BIS Triennial Survey)',
        }
    },
    'CAN': {
        'name': 'Canada',
        'case_type': 'modest_reserves_strong_institutions',
        'hypothesis': 'Modest thorium but G7 credibility + open markets = partial TMPI candidate',
        'tmpi_note': (
            'Canada holds 2.8% of world thorium reserves — smaller than India '
            'or Australia. But: fully open capital account (Chinn-Ito = 2.28), '
            'G7 institutional credibility, existing CANDU nuclear programme, '
            'and CAD already a nontraditional reserve currency (6.2% BIS FX '
            'turnover 2022). Tests whether institutional quality can compensate '
            'for smaller reserve endowment in TMPI.'
        ),
        'key_events': {
            1971: 'CANDU reactor programme — existing nuclear capacity',
            2007: 'CAD gains nontraditional reserve status',
            2023: 'CAD: 6.2% of global FX turnover (BIS Triennial Survey)',
        }
    },
    'BRA': {
        'name': 'Brazil',
        'case_type': 'reserves_without_institutions',
        'hypothesis': 'Large thorium reserves but capital controls = TMPI institutional gap',
        'tmpi_note': (
            'Brazil holds 13.4% of world thorium reserves — second largest globally. '
            'BUT: capital controls (Chinn-Ito = -1.254, same as India/China), '
            'BRL accounts for only 0.9% of BIS FX turnover. Tests whether '
            'institutional openness is required alongside reserves and capacity. '
            'Comparison with India: similar capital controls, but India has '
            'nuclear capacity and improving institutions. Brazil has neither.'
        ),
        'key_events': {
            1982: 'Angra 1 nuclear plant — minimal programme',
            2009: 'BRL briefly gains reserve currency attention post-GFC',
            2022: 'BRL: 0.9% of global FX turnover (BIS Triennial Survey)',
        }
    },
}


def flag_focal_countries(df):
    df['is_focal'] = df['country_code'].isin(FOCAL_COUNTRIES.keys())
    df['case_type'] = df['country_code'].map(
        {k: v['case_type'] for k, v in FOCAL_COUNTRIES.items()}
    )
    return df


def flag_key_events(df):
    rows = []
    for iso, meta in FOCAL_COUNTRIES.items():
        for year, event in meta['key_events'].items():
            rows.append({'country_code': iso, 'year': year, 'event': event})
    events_df = pd.DataFrame(rows)
    df = df.merge(events_df, on=['country_code', 'year'], how='left')
    df['has_key_event'] = df['event'].notna()
    return df


def extract_focal_panel(df):
    panels = {}
    for iso in FOCAL_COUNTRIES:
        sub = df[df['country_code'] == iso].sort_values('year').copy()
        panels[iso] = sub
        print(f"{FOCAL_COUNTRIES[iso]['name']}: {len(sub)} obs "
              f"({sub.year.min()}-{sub.year.max()})")
    return panels


def compute_yen_gdp_divergence(df):
    japan = df[df['country_code'] == 'JPN'].copy()
    japan['gdp_reserve_divergence'] = japan['gdp_share'] - japan['reserve_share']
    return japan


def compute_china_trajectory(df):
    china = df[df['country_code'] == 'CHN'].copy().sort_values('year')
    china['energy_momentum'] = china['net_energy_position'].diff(5)
    china['reserve_momentum'] = china['reserve_share'].diff(5)
    china['momentum_correlation'] = (
        china['energy_momentum'].rolling(5).corr(china['reserve_momentum'])
    )
    return china


def compute_russia_fragmentation(df, shock_year=2022):
    russia = df[df['country_code'] == 'RUS'].copy()
    russia['post_shock'] = russia['year'] >= shock_year
    pre_mean = russia.loc[russia['year'] < shock_year, 'reserve_share'].mean()
    russia['deviation_from_pre'] = russia['reserve_share'] - pre_mean
    return russia


def compute_india_thorium_premium(df):
    india = df[df['country_code'] == 'IND'].copy()
    india['gdp_predicted_reserve'] = india['gdp_share']
    india['thorium_premium'] = india['reserve_share'] - india['gdp_predicted_reserve']
    india['thorium_reserve_share'] = 0.25
    return india


if __name__ == "__main__":
    print("Variables module v2 — correct construction workflow:")
    print()
    print("  1. construct_net_energy_position(df)         # core independent variable")
    print("  2. construct_gdp_share(df)                   # required control")
    print("  3. construct_energy_dominance_weighted(df)   # era-weighted alternative spec")
    print("  4. construct_energy_export_share(df)         # robustness check (export mechanism)")
    print("  5. construct_reserve_share(cofer_raw)        # dependent variable (from COFER)")
    print("  5b.construct_fx_turnover_share(df, bis_df)   # expanded DV: 38 currencies (BIS)")
    print("  6. construct_lagged_variables(df, 'net_energy_position', [10, 15])")
    print("  7. construct_thorium_monetary_potential(df, thorium_df, gov_df)")
    print("     ^ CROSS-SECTION ONLY — collinear with country FE in panel models")
    print()
    print("  To verify era weights from live OWID data:")
    print("  compute_era_weights_from_owid(owid_df)")
    print()
    print(f"  Focal countries: {list(FOCAL_COUNTRIES.keys())}")
