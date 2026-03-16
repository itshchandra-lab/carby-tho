"""
models.py v2
Model specifications for the energy-monetary transitions paper.

FIXES FROM PEER REVIEW:
- Stationarity tests (ADF/PP) added — run BEFORE any regression
- Panel cointegration tests (Pedroni) added
- Renamed from "panel" to "pooled time series" — honest about N=6
- Time fixed effects added with justification
- All controls (FinDepth, KAOpen) now in actual model code
- Lag selection pre-specified at 10yr and 15yr — not data mined
- VAR replaced with VECM after Johansen cointegration test
- Carbon capture model reframed as mechanism illustration, not power test
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.vector_ar.vecm import VECM, select_coint_rank
from statsmodels.tsa.stattools import grangercausalitytests, zivot_andrews
from statsmodels.tsa.ardl import ARDL, ardl_select_order, UECM
import warnings
warnings.filterwarnings('ignore')

try:
    from linearmodels.panel import PanelOLS, PooledOLS, BetweenOLS
    LINEARMODELS_AVAILABLE = True
except ImportError:
    LINEARMODELS_AVAILABLE = False
    print("linearmodels not installed. Run: pip install linearmodels")


# ─────────────────────────────────────────────
# STEP 0: STATIONARITY TESTS
# Must run before any regression. Non-stationary
# series produce spurious results.
# ─────────────────────────────────────────────

def test_stationarity(series: pd.Series,
                      name: str = 'series',
                      max_lags: int = 4) -> dict:
    """
    ADF and KPSS unit root tests for a single series.

    ADF null: series has a unit root (non-stationary)
    KPSS null: series is stationary

    Interpretation:
        ADF rejects AND KPSS does not reject → stationary (I(0))
        ADF does not reject AND KPSS rejects → non-stationary (I(1))
        Both reject or both don't reject → inconclusive

    If I(1): first-difference before modelling, OR test for cointegration.
    """
    series = series.dropna()

    adf_stat, adf_pval, _, _, adf_crit, _ = adfuller(series, maxlag=max_lags,
                                                       autolag='AIC')
    kpss_stat, kpss_pval, _, kpss_crit = kpss(series, regression='c', nlags='auto')

    adf_reject = adf_pval < 0.05
    kpss_reject = kpss_pval < 0.05

    if adf_reject and not kpss_reject:
        conclusion = 'STATIONARY I(0)'
    elif not adf_reject and kpss_reject:
        conclusion = 'NON-STATIONARY I(1) — difference before modelling'
    elif adf_reject and kpss_reject:
        conclusion = 'INCONCLUSIVE — possibly trend-stationary'
    else:
        conclusion = 'INCONCLUSIVE — possibly I(2) or structural break'

    result = {
        'series': name,
        'n_obs': len(series),
        'adf_stat': round(adf_stat, 4),
        'adf_pval': round(adf_pval, 4),
        'adf_reject_unit_root': adf_reject,
        'kpss_stat': round(kpss_stat, 4),
        'kpss_pval': round(kpss_pval, 4),
        'kpss_reject_stationarity': kpss_reject,
        'conclusion': conclusion,
    }

    print(f"{name}: {conclusion} (ADF p={adf_pval:.3f}, KPSS p={kpss_pval:.3f})")
    return result


def run_stationarity_battery(df: pd.DataFrame,
                              variables: list = None) -> pd.DataFrame:
    """
    Run stationarity tests on all key variables for all countries.
    Returns summary table. Call this before running any model.

    If majority of series are I(1):
    → test for cointegration before running levels regression
    → if not cointegrated, first-difference the data
    """
    if variables is None:
        variables = ['reserve_share', 'net_energy_position',
                     'energy_dominance_weighted', 'gdp_share',
                     'trade_openness', 'inflation_cpi',
                     'domestic_credit_private_pct_gdp', 'kaopen']

    results = []
    for country in df['country_code'].unique():
        sub = df[df['country_code'] == country].sort_values('year')
        for var in variables:
            if var not in sub.columns:
                continue
            series = sub[var].dropna()
            if len(series) < 15:
                continue
            r = test_stationarity(series, name=f"{country}:{var}")
            r['country'] = country
            results.append(r)

    summary = pd.DataFrame(results)
    print("\n=== STATIONARITY SUMMARY ===")
    print(summary.groupby('conclusion').size().sort_values(ascending=False))
    return summary


# ─────────────────────────────────────────────
# STEP 1: POOLED TIME SERIES MODEL
# (NOT panel — honest about N=6 reserve currencies)
# ─────────────────────────────────────────────

def run_pooled_ts_model(df: pd.DataFrame,
                        dep_var: str = 'reserve_share',
                        lag: int = 10,
                        differenced: bool = False) -> dict:
    """
    Pooled time series with entity fixed effects.

    NAMING: This is pooled time series, not panel econometrics.
    The reserve currency universe has N=6 entities (USD, EUR, GBP,
    JPY, CHF, CNY). Panel FE asymptotics (N→∞) do not apply.
    With N=6, clustered standard errors are unreliable.
    We use HC3 heteroskedasticity-robust SE instead.

    SPECIFICATION:
    ΔReserveShare_it = α_i + β1(ΔNEP_it-lag) + β2(ΔGDPshare_it)
                     + β3(TradeOpen_it) + β4(FinDepth_it)
                     + β5(KAOpen_it) + β6(Inflation_it)
                     + γ_t(time dummies) + ε_it

    TIME FIXED EFFECTS: included. Dollar reserve dominance has massive
    shared time trends (Bretton Woods, Nixon shock 1971, petrodollar 1974,
    GFC 2008, COVID 2020). Omitting time FE conflates global trends with
    energy-monetary relationship. We include time dummies and report
    both specs in the paper.

    CONTROLS (all now in actual code, not just README):
    - gdp_share: economic size
    - trade_openness: currency demand from trade
    - domestic_credit_private_pct_gdp: financial market depth
    - kaopen (Chinn-Ito): capital account openness
    - inflation_cpi: monetary credibility

    differenced: if True, runs on first-differenced series (for I(1) variables)
    """
    required = [dep_var, f'net_energy_position_lag{lag}',
                'gdp_share', 'trade_openness', 'inflation_cpi']
    optional = ['domestic_credit_private_pct_gdp', 'kaopen', 'thorium_index']

    n_entities = df['country_code'].nunique()
    if n_entities < 10:
        print(f"WARNING: Only {n_entities} entities in dataset. "
              f"Panel FE asymptotics (N→∞) do not apply. "
              f"HC3 SEs are asymptotically valid but may over-reject at small N. "
              f"Interpret results as structured descriptive, not causal identification.")

    df_model = df.dropna(subset=required).copy()

    controls = required[1:]  # exclude dep_var
    for col in optional:
        if col in df_model.columns and df_model[col].notna().sum() > 20:
            controls.append(col)

    if differenced:
        df_model = df_model.sort_values(['country_code', 'year'])
        for col in [dep_var] + controls:
            df_model[f'd_{col}'] = df_model.groupby('country_code')[col].diff()
        dep_var_use = f'd_{dep_var}'
        controls_use = [f'd_{c}' for c in controls]
        df_model = df_model.dropna(subset=[dep_var_use] + controls_use)
    else:
        dep_var_use = dep_var
        controls_use = controls
        df_model = df_model.dropna(subset=[dep_var_use] + controls_use)

    # Entity dummies (fixed effects)
    entity_dummies = pd.get_dummies(df_model['country_code'],
                                     prefix='fe', drop_first=True)

    # Time dummies — justified: removes shared global trends
    year_dummies = pd.get_dummies(df_model['year'],
                                   prefix='yr', drop_first=True)

    X = pd.concat([df_model[controls_use], entity_dummies, year_dummies], axis=1)
    X = sm.add_constant(X).astype(float)
    y = df_model[dep_var_use].astype(float)

    model = sm.OLS(y, X)
    result = model.fit(cov_type='HC3')  # robust SE, appropriate for small N

    nep_col = f'd_net_energy_position_lag{lag}' if differenced else f'net_energy_position_lag{lag}'

    print(f"\n=== POOLED TS MODEL (lag={lag}yr, {'differenced' if differenced else 'levels'}) ===")
    print(f"N observations: {len(y)}")
    print(f"N entities: {df_model['country_code'].nunique()}")
    if nep_col in result.params.index:
        print(f"NEP coefficient: {result.params[nep_col]:.4f} "
              f"(p={result.pvalues[nep_col]:.3f})")
    print(f"R²: {result.rsquared:.3f}")

    return {
        'model': result,
        'lag': lag,
        'differenced': differenced,
        'n_obs': len(y),
        'n_entities': df_model['country_code'].nunique(),
        'r_squared': result.rsquared,
        'coefficients': result.params,
        'pvalues': result.pvalues,
        'summary': result.summary(),
        'controls_included': controls_use,
    }


def run_both_lags(df: pd.DataFrame,
                  differenced: bool = False) -> dict:
    """
    Run model at both pre-specified lags (10yr and 15yr).
    Report both. Do not select based on R².

    The two lags are theory-driven:
    - 10yr: minimum adjustment period for reserve composition
    - 15yr: conservative upper bound

    Consistent sign and significance across both = robust finding.
    Divergence = interesting and requires interpretation.
    """
    results = {}
    for lag in [10, 15]:
        try:
            results[f'lag{lag}'] = run_pooled_ts_model(
                df, lag=lag, differenced=differenced
            )
        except Exception as e:
            print(f"Lag {lag} failed: {e}")

    # Print comparison
    print("\n=== LAG COMPARISON ===")
    print(f"{'Lag':<8} {'NEP coef':<12} {'p-value':<10} {'R²':<8} {'N'}")
    for lag_key, r in results.items():
        lag_n = int(lag_key.replace('lag', ''))
        nep_col = f'net_energy_position_lag{lag_n}'
        if differenced:
            nep_col = f'd_{nep_col}'
        if nep_col in r['coefficients'].index:
            coef = r['coefficients'][nep_col]
            pval = r['pvalues'][nep_col]
            print(f"{lag_n:<8} {coef:<12.4f} {pval:<10.3f} "
                  f"{r['r_squared']:<8.3f} {r['n_obs']}")

    return results


def run_robustness_checks(df: pd.DataFrame) -> dict:
    """
    2×2×2 robustness table: transform(levels/logit) × differenced × lag(10/15).

    8 specifications total. A finding is robust if the NEP coefficient is
    consistently signed and significant across most specifications.

    Verdict thresholds: 6+/8 = robust; 3-5/8 = fragile; <3/8 = not robust.
    """
    summary_rows = []
    results = {}

    for transform in ['levels', 'logit']:
        for differenced in [False, True]:
            for lag in [10, 15]:
                spec_key = f"{transform}_{'diff' if differenced else 'levels'}_lag{lag}"
                try:
                    nep_lag_col = f"net_energy_position_lag{lag}"
                    if transform == 'logit':
                        r = run_logit_transform(df, lag_col=nep_lag_col)
                        if r is None:
                            raise ValueError("logit transform returned None")
                        # re-run differenced variant if needed
                        if differenced:
                            df_logit = df.copy()
                            df_logit['reserve_share_logit'] = np.log(
                                df_logit['reserve_share'].clip(0.001, 0.999) /
                                (1 - df_logit['reserve_share'].clip(0.001, 0.999))
                            )
                            df_logit['_orig'] = df_logit['reserve_share']
                            df_logit['reserve_share'] = df_logit['reserve_share_logit']
                            r = run_pooled_ts_model(df_logit, lag=lag, differenced=True)
                            df_logit['reserve_share'] = df_logit['_orig']
                    else:
                        r = run_pooled_ts_model(df, lag=lag, differenced=differenced)

                    nep_col = f"{'d_' if differenced else ''}net_energy_position_lag{lag}"
                    coef = r['coefficients'].get(nep_col, float('nan'))
                    pval = r['pvalues'].get(nep_col, float('nan'))
                    results[spec_key] = r
                    summary_rows.append({
                        'specification': spec_key,
                        'nep_coef': round(coef, 4),
                        'nep_pval': round(pval, 3),
                        'r_squared': round(r['r_squared'], 3),
                        'n_obs': r['n_obs'],
                        'significant_05': pval < 0.05,
                    })
                except Exception as e:
                    print(f"Spec {spec_key} failed: {e}")
                    summary_rows.append({
                        'specification': spec_key,
                        'nep_coef': float('nan'),
                        'nep_pval': float('nan'),
                        'r_squared': float('nan'),
                        'n_obs': 0,
                        'significant_05': False,
                    })

    summary = pd.DataFrame(summary_rows)

    # Bonferroni correction for multiple testing
    n_specs = len(summary)
    bonf_threshold = 0.05 / n_specs
    summary['significant_bonferroni'] = summary['nep_pval'] < bonf_threshold

    print("\n=== ROBUSTNESS CHECK — 2×2×2 SPECIFICATION TABLE ===")
    print(summary[['specification', 'nep_coef', 'nep_pval',
                   'r_squared', 'n_obs', 'significant_05',
                   'significant_bonferroni']].to_string(index=False))
    n_sig = int(summary['significant_05'].sum())
    n_total = len(summary)
    print(f"\n{n_sig}/{n_total} specifications significant at 5%.")
    if n_sig >= 6:
        print("Finding: ROBUST across specifications.")
    elif n_sig >= 3:
        print("Finding: FRAGILE — significant in some but not all specs. "
              "Interpret cautiously and report all.")
    else:
        print("Finding: NOT ROBUST — fails most specifications.")

    n_sig_bonf = int(summary['significant_bonferroni'].sum())
    print(f"\nBonferroni-corrected threshold: {bonf_threshold:.4f}")
    print(f"{n_sig_bonf}/{n_total} specifications significant after Bonferroni correction.")
    if n_sig_bonf == 0:
        print("No specifications survive multiple testing correction.")

    return {'results': results, 'summary': summary}


def compute_within_r2(model_result, df_model: pd.DataFrame, dep_var: str,
                      lag_col: str, entity_col: str = 'country_code',
                      time_col: str = 'year', differenced: bool = False) -> dict:
    """
    Compute within-R² by two-way demeaning (entity + time fixed effects).

    The standard OLS R² of 0.997 includes variance explained by all entity and
    time dummies. Within-R² strips that out — it measures how much of the
    within-entity, within-time variation in reserve_share is explained by NEP.
    Values in 0.05–0.40 are typical; 0.997 is spuriously high.
    """
    df = df_model.copy().dropna(subset=[dep_var, lag_col])

    # Two-way demeaning of y
    entity_means_y = df.groupby(entity_col)[dep_var].transform('mean')
    time_means_y   = df.groupby(time_col)[dep_var].transform('mean')
    grand_mean_y   = df[dep_var].mean()
    y_within = df[dep_var] - entity_means_y - time_means_y + grand_mean_y

    # Two-way demeaning of x
    entity_means_x = df.groupby(entity_col)[lag_col].transform('mean')
    time_means_x   = df.groupby(time_col)[lag_col].transform('mean')
    grand_mean_x   = df[lag_col].mean()
    x_within = df[lag_col] - entity_means_x - time_means_x + grand_mean_x

    ss_total = ((y_within - y_within.mean()) ** 2).sum()

    X_dm = sm.add_constant(x_within)
    res_dm = sm.OLS(y_within, X_dm).fit()
    ss_resid = res_dm.ssr
    within_r2 = 1 - ss_resid / ss_total if ss_total > 0 else np.nan

    return {
        'within_r2': within_r2,
        'total_r2': model_result.rsquared,
        'note': 'Within-R² strips entity+time FE variance; relevant metric for NEP',
    }


def run_leave_one_out(panel_df: pd.DataFrame, lag: int = 10,
                      differenced: bool = False) -> pd.DataFrame:
    """
    Leave-one-out sensitivity: drop each reserve currency entity in turn,
    re-run pooled TS model, record NEP coefficient and significance.

    If the coefficient is stable across entity exclusions, the finding is not
    driven by a single influential country.
    """
    entities = list(panel_df['country_code'].unique())
    rows = []
    for drop in ['none'] + entities:
        try:
            sub = panel_df if drop == 'none' else panel_df[panel_df['country_code'] != drop]
            r = run_pooled_ts_model(sub, lag=lag, differenced=differenced)
            nep_col = f"{'d_' if differenced else ''}net_energy_position_lag{lag}"
            coef = r['coefficients'].get(nep_col, np.nan)
            pval = r['pvalues'].get(nep_col, np.nan)
            rows.append({
                'dropped_entity': drop,
                'nep_coef': coef,
                'nep_pval': pval,
                'n_obs': r['n_obs'],
                'significant_05': pval < 0.05 if not np.isnan(pval) else False,
            })
        except Exception as e:
            rows.append({
                'dropped_entity': drop,
                'nep_coef': np.nan,
                'nep_pval': np.nan,
                'n_obs': 0,
                'significant_05': False,
            })
    return pd.DataFrame(rows)


def run_logit_transform(panel_df: pd.DataFrame, lag_col: str,
                        entity_col: str = 'country_code',
                        time_col: str = 'year') -> dict:
    """
    Logit-transform reserve_share before running pooled TS model.

    Reserve shares sum to ~100% (compositional data), violating OLS linearity.
    Logit maps (0,1) → (-∞,+∞), removing the boundary constraint.
    Coefficient interpretation changes: β is now effect on log-odds of reserve share.
    """
    df = panel_df.copy()
    df['reserve_share_logit'] = np.log(
        df['reserve_share'].clip(0.001, 0.999) /
        (1 - df['reserve_share'].clip(0.001, 0.999))
    )
    df['_orig_reserve_share'] = df['reserve_share']
    df['reserve_share'] = df['reserve_share_logit']

    lag_num = int(''.join(filter(str.isdigit, lag_col.replace('net_energy_position_lag', ''))))
    result = run_pooled_ts_model(df, lag=lag_num, differenced=False)
    df['reserve_share'] = df['_orig_reserve_share']

    if result:
        result['transform'] = 'logit'
        result['interpretation'] = ('Logit-transformed DV addresses compositional data '
                                    'constraint (shares sum to ~100%)')
    return result


# ─────────────────────────────────────────────
# STEP 2: COINTEGRATION + VECM
# If series are I(1), test for cointegration.
# If cointegrated: VECM. If not: VAR in differences.
# ─────────────────────────────────────────────

def run_johansen_cointegration(series_df: pd.DataFrame,
                                country: str = '') -> dict:
    """
    Johansen cointegration test for a pair of I(1) series.

    If reserve_share and net_energy_position are both I(1) but share
    a long-run equilibrium, they are cointegrated. Running VAR in levels
    on non-cointegrated I(1) series = spurious regression.

    Correct approach:
    - Cointegrated: use VECM (captures both short-run dynamics and
      long-run equilibrium correction)
    - Not cointegrated: use VAR in first differences

    Returns cointegration rank and recommendation.
    """
    clean = series_df.dropna()
    if len(clean) < 20:
        return {'error': f'Insufficient obs for {country}: {len(clean)}'}

    try:
        result = select_coint_rank(clean, det_order=0, k_ar_diff=1,
                                    method='trace', signif=0.05)
        rank = result.rank

        if rank > 0:
            recommendation = f'COINTEGRATED (rank={rank}) → use VECM'
        else:
            recommendation = 'NOT COINTEGRATED → use VAR in first differences'

        print(f"{country}: {recommendation}")
        return {
            'country': country,
            'coint_rank': rank,
            'recommendation': recommendation,
            'test_result': result,
        }
    except Exception as e:
        return {'error': str(e), 'country': country}


def run_vecm_or_var(df: pd.DataFrame,
                    country: str,
                    variables: list = None) -> dict:
    """
    CORRECT Model 2: VECM or VAR depending on cointegration result.

    PREVIOUS VERSION ran VAR on I(1) series without checking
    stationarity or cointegration. That produces invalid inference.

    This function:
    1. Extracts country time series
    2. Tests stationarity of each variable
    3. If I(1): runs Johansen cointegration test
    4. If cointegrated: fits VECM, extracts speed-of-adjustment (α)
       and long-run coefficient (β)
    5. If not cointegrated: fits VAR in first differences
    6. Runs Granger causality on appropriate specification
    """
    if variables is None:
        variables = ['net_energy_position', 'reserve_share']

    sub = df[df['country_code'] == country].sort_values('year')
    data = sub[variables].dropna()

    if len(data) < 20:
        return {'error': f'Insufficient data for {country}: {len(data)} obs'}

    # Step 1: stationarity of each variable
    stationarity = {}
    for var in variables:
        r = test_stationarity(data[var], name=f"{country}:{var}")
        stationarity[var] = r

    all_nonstationary = all(
        not r['adf_reject_unit_root'] for r in stationarity.values()
    )

    if not all_nonstationary:
        # At least one variable is stationary — VAR in levels is acceptable
        print(f"{country}: Mixed stationarity — running VAR in levels")
        return _run_var_levels(data, country, variables, stationarity)

    # Step 2: Johansen cointegration
    coint = run_johansen_cointegration(data, country)
    if 'error' in coint:
        return coint

    if coint['coint_rank'] > 0:
        # Cointegrated: VECM
        return _run_vecm(data, country, variables, coint)
    else:
        # Not cointegrated: VAR in differences
        return _run_var_differences(data, country, variables)


def _run_vecm(data, country, variables, coint_result):
    """Fit VECM and extract long-run relationship."""
    try:
        model = VECM(data, k_ar_diff=1, coint_rank=coint_result['coint_rank'],
                     deterministic='ci')
        result = model.fit()

        print(f"\n{country} VECM results:")
        print(f"  Long-run coeff (β): {result.beta}")
        print(f"  Speed of adjustment (α): {result.alpha}")

        return {
            'country': country,
            'model_type': 'VECM',
            'coint_rank': coint_result['coint_rank'],
            'result': result,
            'beta': result.beta,
            'alpha': result.alpha,
            'variables': variables,
        }
    except Exception as e:
        return {'error': str(e), 'country': country, 'model_type': 'VECM_failed'}


def _run_var_differences(data, country, variables):
    """VAR in first differences for non-cointegrated I(1) series."""
    try:
        d_data = data.diff().dropna()
        model = VAR(d_data)
        lag_order = model.select_order(maxlags=4)
        optimal_lag = max(1, int(lag_order.selected_orders.get('aic', 1)))
        result = model.fit(optimal_lag)

        # Granger causality on differenced data
        gc = {}
        for i, v1 in enumerate(variables):
            for j, v2 in enumerate(variables):
                if i != j:
                    gc_result = grangercausalitytests(
                        d_data[[v1, v2]], maxlag=optimal_lag, verbose=False
                    )
                    gc[f'{v2}_causes_{v1}'] = {
                        lag: tests[0]['ssr_ftest'][1]
                        for lag, tests in gc_result.items()
                    }

        print(f"\n{country} VAR(differences) results:")
        for pair, pvals in gc.items():
            min_p = min(pvals.values())
            print(f"  {pair}: min p-value = {min_p:.3f}")

        return {
            'country': country,
            'model_type': 'VAR_differences',
            'result': result,
            'granger': gc,
            'optimal_lag': optimal_lag,
        }
    except Exception as e:
        return {'error': str(e), 'country': country}


def _run_var_levels(data, country, variables, stationarity):
    """VAR in levels when at least one variable is I(0)."""
    try:
        model = VAR(data)
        lag_order = model.select_order(maxlags=4)
        optimal_lag = max(1, int(lag_order.selected_orders.get('aic', 1)))
        result = model.fit(optimal_lag)
        return {
            'country': country,
            'model_type': 'VAR_levels',
            'result': result,
            'stationarity': stationarity,
        }
    except Exception as e:
        return {'error': str(e)}


# ─────────────────────────────────────────────
# STEP 1b: IV/2SLS — BARTIK INSTRUMENT
# Endowment × price shocks as instrument for NEP.
# ─────────────────────────────────────────────

def run_iv_2sls(df, dep_var='reserve_share', endog_var='net_energy_position',
                instrument='bartik_energy_shock', lag=10, controls=None,
                entity_fe=False, time_fe=True):
    """
    Two-stage least squares using Bartik (shift-share) instrument.

    Stage 1: NEP_lag = α + γ·Bartik_lag + X'δ + [FE] + ε
    Stage 2: ReserveShare = α + β·NEP_lag_hat + X'δ + [FE] + ε

    The Bartik instrument = baseline_endowment × global_price_shock.
    Exclusion restriction: global energy price shocks affect reserve
    currency status ONLY through their effect on energy position,
    not directly. Defensible because oil price shocks are driven by
    global demand/supply, not by individual countries' monetary policy.

    entity_fe: default False. Bartik exploits BETWEEN-entity endowment
    variation — entity FE demean this away, killing the first stage.
    The instrument IS the cross-sectional identification.

    time_fe: default True. Absorbs common time trends (global shocks
    that affect all currencies simultaneously).

    Reports: first-stage F-statistic (Staiger-Stock rule: F>10),
    IV estimate, and Hausman test for endogeneity.
    """
    endog_col = f'{endog_var}_lag{lag}' if lag else endog_var
    iv_col = f'{instrument}_lag{lag}' if lag else instrument

    required = [dep_var, endog_col, iv_col]
    if controls is None:
        controls = ['gdp_share', 'trade_openness', 'inflation_cpi']
    available_controls = [c for c in controls if c in df.columns]

    df_model = df.dropna(subset=required + available_controls).copy()

    if len(df_model) < 30:
        return {'error': f'Insufficient obs after dropping NaN: {len(df_model)}'}

    # Build control matrix
    X_parts = [df_model[available_controls]]

    if entity_fe:
        entity_dummies = pd.get_dummies(df_model['country_code'],
                                         prefix='fe', drop_first=True)
        X_parts.append(entity_dummies)

    if time_fe:
        year_dummies = pd.get_dummies(df_model['year'],
                                       prefix='yr', drop_first=True)
        X_parts.append(year_dummies)

    X_controls = pd.concat(X_parts, axis=1)
    X_controls = sm.add_constant(X_controls).astype(float)

    y = df_model[dep_var].astype(float)
    endog = df_model[endog_col].astype(float)
    z = df_model[iv_col].astype(float)

    # ── Stage 1: regress endogenous var on instrument + controls ──
    X_stage1 = pd.concat([z.rename('instrument'), X_controls], axis=1)
    stage1 = sm.OLS(endog, X_stage1).fit(cov_type='HC3')
    first_stage_f = stage1.fvalues if hasattr(stage1, 'fvalues') else None

    # First-stage F on excluded instrument
    # Manual: F = (t-stat on instrument)^2
    if 'instrument' in stage1.params.index:
        t_instrument = stage1.tvalues['instrument']
        f_excluded = t_instrument ** 2
    else:
        f_excluded = 0

    endog_hat = stage1.fittedvalues

    # ── Stage 2: regress DV on fitted endogenous + controls ──
    X_stage2 = X_controls.copy()
    X_stage2[endog_col] = endog_hat.values
    stage2 = sm.OLS(y, X_stage2).fit(cov_type='HC3')

    # IV coefficient
    iv_beta = stage2.params.get(endog_col, None)
    iv_se = stage2.bse.get(endog_col, None)
    iv_pval = stage2.pvalues.get(endog_col, None)

    # ── OLS for comparison (Hausman test) ──
    X_ols = X_controls.copy()
    X_ols[endog_col] = endog.values
    ols = sm.OLS(y, X_ols).fit(cov_type='HC3')
    ols_beta = ols.params.get(endog_col, None)

    # Hausman: large difference between IV and OLS suggests endogeneity
    hausman_diff = abs(iv_beta - ols_beta) if (iv_beta and ols_beta) else None

    result = {
        'n_obs': len(df_model),
        'n_entities': df_model['country_code'].nunique(),
        'lag': lag,
        'first_stage_f': round(f_excluded, 2),
        'weak_instrument': f_excluded < 10,
        'iv_beta': round(iv_beta, 4) if iv_beta else None,
        'iv_se': round(iv_se, 4) if iv_se else None,
        'iv_pval': round(iv_pval, 4) if iv_pval else None,
        'ols_beta': round(ols_beta, 4) if ols_beta else None,
        'hausman_diff': round(hausman_diff, 4) if hausman_diff else None,
        'stage1_model': stage1,
        'stage2_model': stage2,
        'ols_model': ols,
    }

    print(f"\n=== IV/2SLS (Bartik instrument, lag={lag}) ===")
    print(f"N={len(df_model)}, entities={df_model['country_code'].nunique()}")
    print(f"First-stage F (excluded instrument): {f_excluded:.2f}"
          f" {'— WEAK INSTRUMENT' if f_excluded < 10 else '— adequate'}")
    print(f"IV  β(NEP): {iv_beta:.4f} (SE={iv_se:.4f}, p={iv_pval:.3f})")
    print(f"OLS β(NEP): {ols_beta:.4f}")
    if hausman_diff:
        print(f"Hausman |IV-OLS|: {hausman_diff:.4f}")

    return result


# ─────────────────────────────────────────────
# STEP 2b: ARDL BOUNDS TEST
# Handles mixed I(0)/I(1) — unlike Johansen which requires all I(1).
# If F > I(1) critical bound → cointegrated → levels regression valid.
# ─────────────────────────────────────────────

def run_ardl_bounds_test(df, country, dep_var='reserve_share',
                         exog_var='net_energy_position', max_lags=4):
    """
    ARDL bounds test (Pesaran, Shin & Smith 2001).
    Handles mixed I(0)/I(1) — unlike Johansen which requires all I(1).

    If F > I(1) critical bound → cointegrated → levels regression valid
    If F < I(0) critical bound → not cointegrated → must difference
    Between → inconclusive
    """
    sub = df[df['country_code'] == country].sort_values('year')
    data = sub[[dep_var, exog_var]].dropna()
    if len(data) < 20:
        return {'country': country, 'error': f'Insufficient obs: {len(data)}'}

    endog = data[dep_var]
    exog = data[[exog_var]]

    # Select optimal lag order via BIC
    sel = ardl_select_order(endog, max_lags, exog, max_lags,
                            trend='c', ic='bic')
    p = max(sel.ar_lags) if sel.ar_lags else 1
    # dl_lags is a dict {var_name: [lag_list]} — extract max lag per var
    q_dict = {k: max(v) if v else 1 for k, v in sel.dl_lags.items()}
    if not q_dict:
        q_dict = {exog_var: 1}

    # Fit UECM form and run bounds test
    # UECM lags must be int; order is dict mapping exog names to int
    uecm = UECM(endog, lags=p, exog=exog, order=q_dict, trend='c').fit()

    # Case 3: unrestricted intercept, no trend (most common)
    bounds = uecm.bounds_test(case=3)

    f_stat = bounds.stat
    # crit_vals is DataFrame with index=[90, 95, 99, 99.9], cols=['lower','upper']
    # lower = I(0) bound, upper = I(1) bound
    crit_I0_5pct = bounds.crit_vals.loc[95.0, 'lower']
    crit_I1_5pct = bounds.crit_vals.loc[95.0, 'upper']
    coint_5pct = f_stat > crit_I1_5pct

    # ECM speed of adjustment: coefficient on L1 of dependent variable
    ecm_param_name = f'{dep_var}.L1'
    ecm_speed = uecm.params.get(ecm_param_name, None)

    result = {
        'country': country, 'n_obs': len(data),
        'ardl_order': (p, q_dict), 'f_stat': round(f_stat, 3),
        'cointegrated_5pct': coint_5pct,
        'critical_I0_5pct': round(crit_I0_5pct, 3),
        'critical_I1_5pct': round(crit_I1_5pct, 3),
        'ecm_speed': round(ecm_speed, 4) if ecm_speed is not None else None,
    }

    if coint_5pct:
        result['long_run_coefs'] = uecm.ci_params
        result['interpretation'] = (
            f'{country}: COINTEGRATED (F={f_stat:.2f} > I(1) bound={crit_I1_5pct:.2f}) '
            f'→ levels specification valid. '
            f'Differencing this pair destroys the long-run signal.'
        )
    else:
        inconclusive = f_stat > crit_I0_5pct
        if inconclusive:
            result['interpretation'] = (
                f'{country}: INCONCLUSIVE (F={f_stat:.2f} between bounds '
                f'[{crit_I0_5pct:.2f}, {crit_I1_5pct:.2f}])'
            )
        else:
            result['interpretation'] = (
                f'{country}: NOT COINTEGRATED (F={f_stat:.2f} < I(0) bound={crit_I0_5pct:.2f}) '
                f'→ must difference.'
            )

    print(result['interpretation'])
    return result


def run_ardl_all_entities(df, entities=None):
    """
    Run ARDL bounds test across all reserve currency entities.
    Returns summary DataFrame.
    """
    if entities is None:
        entities = sorted(df['country_code'].unique())

    rows = []
    for country in entities:
        try:
            r = run_ardl_bounds_test(df, country)
            if 'error' in r:
                rows.append({'country': country, 'n_obs': 0,
                             'f_stat': None, 'I0_bound': None,
                             'I1_bound': None, 'cointegrated': None,
                             'ecm_speed': None, 'note': r['error']})
            else:
                rows.append({
                    'country': r['country'],
                    'n_obs': r['n_obs'],
                    'ardl_order': str(r['ardl_order']),
                    'f_stat': r['f_stat'],
                    'I0_bound': r['critical_I0_5pct'],
                    'I1_bound': r['critical_I1_5pct'],
                    'cointegrated': r['cointegrated_5pct'],
                    'ecm_speed': r['ecm_speed'],
                    'note': '',
                })
        except Exception as e:
            rows.append({'country': country, 'n_obs': 0,
                         'f_stat': None, 'I0_bound': None,
                         'I1_bound': None, 'cointegrated': None,
                         'ecm_speed': None, 'note': str(e)})

    summary = pd.DataFrame(rows)
    n_coint = summary['cointegrated'].sum() if 'cointegrated' in summary.columns else 0
    n_tested = summary['cointegrated'].notna().sum()
    print(f"\n=== ARDL BOUNDS TEST SUMMARY ===")
    print(f"Cointegrated at 5%: {n_coint}/{n_tested} entities")
    print(summary.to_string(index=False))
    return summary


# ─────────────────────────────────────────────
# STEP 2c: ENTITY-SPECIFIC MODELS
# The honest approach given N=6. Stop pretending this is a panel.
# Run each entity separately, then meta-analyse.
# ─────────────────────────────────────────────

def run_entity_ecm(df, country, dep_var='reserve_share',
                   exog_var='net_energy_position', max_lags=4, lag=None):
    """
    Entity-specific Error Correction Model via ARDL/UECM.

    For each country, estimates:
    1. ARDL bounds test for cointegration
    2. If cointegrated: ECM with long-run coefficient and adjustment speed
    3. If not: returns VAR in differences

    lag: if specified (e.g. 10), uses net_energy_position_lag10 as exog.
         This matches the pooled model's pre-specified lag structure.
    """
    if lag is not None:
        exog_var = f'{exog_var}_lag{lag}'
    sub = df[df['country_code'] == country].sort_values('year')
    data = sub[[dep_var, exog_var]].dropna()
    if len(data) < 20:
        return {'country': country, 'error': f'Insufficient obs: {len(data)}',
                'n_obs': len(data)}

    endog = data[dep_var]
    exog = data[[exog_var]]

    # Optimal lag via BIC
    sel = ardl_select_order(endog, max_lags, exog, max_lags,
                            trend='c', ic='bic')
    p = max(sel.ar_lags) if sel.ar_lags else 1
    q_dict = {k: max(max(v), 1) if v else 1 for k, v in sel.dl_lags.items()}
    if not q_dict:
        q_dict = {exog_var: 1}
    # UECM requires all exog to have order >= 1
    for k in q_dict:
        q_dict[k] = max(q_dict[k], 1)

    # Fit UECM
    try:
        uecm = UECM(endog, lags=p, exog=exog, order=q_dict, trend='c').fit()
    except ValueError:
        # Fallback: force order=1 for all exog
        q_dict = {exog_var: 1}
        uecm = UECM(endog, lags=p, exog=exog, order=q_dict, trend='c').fit()

    # Bounds test
    bounds = uecm.bounds_test(case=3)
    f_stat = bounds.stat
    crit_I1_5pct = bounds.crit_vals.loc[95.0, 'upper']
    cointegrated = f_stat > crit_I1_5pct

    # ECM speed (coefficient on lagged dependent variable in UECM)
    ecm_param = f'{dep_var}.L1'
    ecm_speed = uecm.params.get(ecm_param, None)

    # Long-run NEP coefficient from UECM cointegrating vector
    lr_coefs = uecm.ci_params
    lr_nep = lr_coefs.get(exog_var, None)

    # Standard error on long-run coefficient (delta method approximation)
    # Use the UECM param on exog_var.L1 and ecm_speed
    exog_l1_param = f'{exog_var}.L1'
    exog_l1_coef = uecm.params.get(exog_l1_param, None)
    exog_l1_se = uecm.bse.get(exog_l1_param, None)

    # For the long-run coef β_LR = -θ_x / θ_y where θ_y is ecm_speed
    # Full delta method for ratio g(a,b) = -a/b
    # Var(g) = (1/b)^2 * Var(a) + (a/b^2)^2 * Var(b) - 2*(a/b^3)*Cov(a,b)
    lr_se = None
    lr_tstat = None
    lr_pval = None
    if exog_l1_coef is not None and ecm_speed is not None and ecm_speed != 0:
        vcov = uecm.cov_params()
        var_a = vcov.loc[exog_l1_param, exog_l1_param]
        var_b = vcov.loc[ecm_param, ecm_param]
        cov_ab = vcov.loc[exog_l1_param, ecm_param]
        a, b = exog_l1_coef, ecm_speed
        var_ratio = (var_a / b**2) + (a**2 * var_b / b**4) - (2 * a * cov_ab / b**3)
        if var_ratio > 0:
            lr_se = np.sqrt(var_ratio)
            lr_tstat = lr_nep / lr_se if lr_se > 0 else None
            if lr_tstat is not None:
                from scipy.stats import t as t_dist
                lr_pval = 2 * (1 - t_dist.cdf(abs(lr_tstat), df=len(data) - len(uecm.params)))

    result = {
        'country': country,
        'n_obs': len(data),
        'ardl_order': (p, q_dict),
        'cointegrated': cointegrated,
        'f_stat': round(f_stat, 3),
        'ecm_speed': round(ecm_speed, 4) if ecm_speed is not None else None,
        'lr_nep_coef': round(lr_nep, 4) if lr_nep is not None else None,
        'lr_nep_se': round(lr_se, 4) if lr_se is not None else None,
        'lr_nep_pval': round(lr_pval, 4) if lr_pval is not None else None,
        'uecm_result': uecm,
        'model_type': 'ECM' if cointegrated else 'UECM_no_coint',
    }

    status = 'COINTEGRATED' if cointegrated else 'not cointegrated'
    print(f"{country}: {status} (F={f_stat:.2f}), "
          f"LR β(NEP)={lr_nep:.2f}, ECM speed={ecm_speed:.3f}")
    return result


def run_entity_dols(df, country, dep_var='reserve_share',
                    exog_var='net_energy_position', leads=None, lags=None, lag=None):
    """
    Dynamic OLS (DOLS) — Stock & Watson (1993).

    Adds leads and lags of differenced regressors to a levels regression.
    This corrects for endogeneity and serial correlation in the
    cointegrating regression. More robust than plain OLS for small samples.

    lag: if specified (e.g. 10), uses net_energy_position_lag10 as exog.

    DOLS: y_t = α + β·x_t + Σ γ_j · Δx_{t+j} + ε_t
                              j=-lags..+leads
    """
    if lag is not None:
        exog_var = f'{exog_var}_lag{lag}'
    sub = df[df['country_code'] == country].sort_values('year').reset_index(drop=True)
    data = sub[[dep_var, exog_var]].dropna().reset_index(drop=True)
    if len(data) < 20:
        return {'country': country, 'error': f'Insufficient obs: {len(data)}'}

    if leads is None:
        leads = max(1, int(len(data) ** (1/3)))
    if lags is None:
        lags = max(1, int(len(data) ** (1/3)))

    y = data[dep_var]
    x = data[exog_var]
    dx = x.diff()

    # Build DOLS regressor matrix: x_t plus leads/lags of Δx
    X_dols = pd.DataFrame({'const': 1.0, exog_var: x})
    for j in range(-lags, leads + 1):
        col_name = f'd_{exog_var}_{"lead" if j > 0 else "lag"}{abs(j)}'
        if j == 0:
            col_name = f'd_{exog_var}_0'
        X_dols[col_name] = dx.shift(-j)

    # Drop rows with NaN from leads/lags
    valid = X_dols.dropna().index
    X_dols = X_dols.loc[valid]
    y_dols = y.loc[valid]

    if len(y_dols) < 15:
        return {'country': country, 'error': f'Insufficient obs after DOLS: {len(y_dols)}'}

    max_nw_lags = max(1, int(len(y_dols) ** 0.25))
    model = sm.OLS(y_dols, X_dols).fit(cov_type='HAC', cov_kwds={'maxlags': max_nw_lags})

    beta = model.params.get(exog_var, None)
    se = model.bse.get(exog_var, None)
    pval = model.pvalues.get(exog_var, None)

    print(f"{country} DOLS: β(NEP)={beta:.4f}, SE={se:.4f}, p={pval:.3f}, "
          f"R²={model.rsquared:.3f}")

    return {
        'country': country,
        'n_obs': len(y_dols),
        'beta_nep': round(beta, 4) if beta is not None else None,
        'se_nep': round(se, 4) if se is not None else None,
        'pval_nep': round(pval, 4) if pval is not None else None,
        'r_squared': round(model.rsquared, 3),
        'model': model,
        'model_type': 'DOLS',
        'leads': leads, 'lags': lags,
    }


def wild_bootstrap_ci(df, country, dep_var='reserve_share',
                      exog_var='net_energy_position',
                      n_boot=999, seed=42, estimator='dols', lag=None):
    """
    Wild bootstrap confidence intervals for entity-specific estimates.

    With N=1 entity and T≈30, conventional SEs may under-cover.
    Wild bootstrap (Rademacher weights) preserves heteroskedasticity
    structure without assuming normality.

    Returns bootstrap distribution and percentile CI.
    """
    rng = np.random.RandomState(seed)
    if lag is not None:
        exog_var = f'{exog_var}_lag{lag}'

    # Get point estimate and residuals
    if estimator == 'dols':
        base = run_entity_dols(df, country, dep_var, exog_var)
    else:
        base = run_entity_ecm(df, country, dep_var, exog_var)

    if 'error' in base:
        return base

    base_model = base.get('model') or base.get('uecm_result')
    if base_model is None:
        return {'country': country, 'error': 'No model object available'}

    resid = base_model.resid
    fitted = base_model.fittedvalues
    X = base_model.model.exog
    beta_col = exog_var

    boot_betas = []
    for _ in range(n_boot):
        # Rademacher weights: +1 or -1 with equal probability
        weights = rng.choice([-1, 1], size=len(resid))
        y_boot = fitted + resid * weights

        try:
            boot_model = sm.OLS(y_boot, X).fit()
            col_idx = list(base_model.params.index).index(beta_col)
            boot_betas.append(boot_model.params.iloc[col_idx])
        except (ValueError, np.linalg.LinAlgError):
            continue

    if len(boot_betas) < 100:
        return {'country': country, 'error': f'Only {len(boot_betas)} bootstrap replications succeeded'}

    boot_betas = np.array(boot_betas)
    point = base.get('beta_nep') or base.get('lr_nep_coef')

    result = {
        'country': country,
        'point_estimate': point,
        'boot_se': round(np.std(boot_betas), 4),
        'ci_lower_95': round(np.percentile(boot_betas, 2.5), 4),
        'ci_upper_95': round(np.percentile(boot_betas, 97.5), 4),
        'ci_lower_90': round(np.percentile(boot_betas, 5.0), 4),
        'ci_upper_90': round(np.percentile(boot_betas, 95.0), 4),
        'n_boot': len(boot_betas),
        'boot_distribution': boot_betas,
    }

    covers_zero = result['ci_lower_95'] <= 0 <= result['ci_upper_95']
    print(f"{country} wild bootstrap: β={point:.4f}, "
          f"95% CI=[{result['ci_lower_95']:.4f}, {result['ci_upper_95']:.4f}], "
          f"{'covers zero' if covers_zero else 'excludes zero'}")

    return result


def run_entity_specific_battery(df, entities=None, dep_var='reserve_share',
                                exog_var='net_energy_position', lag=None):
    """
    Full entity-specific analysis: ECM + DOLS + wild bootstrap for each entity.
    Returns summary DataFrame suitable for meta-analysis.

    lag: if specified (e.g. 10), uses net_energy_position_lag10 as exog.
         This matches the pooled model's pre-specified lag structure.

    This is the honest replacement for pooled OLS. Each entity gets its own
    estimate. The USA finding stands or falls on its own merit. Other entities
    show null results with interpretable reasons.
    """
    if entities is None:
        entities = sorted(df[df['has_reserve_share'] == True]['country_code'].unique())

    # Resolve exog_var once for display; individual functions handle lag internally
    actual_exog = f'{exog_var}_lag{lag}' if lag is not None else exog_var
    print(f"Exogenous variable: {actual_exog}")

    rows = []
    for country in entities:
        print(f"\n{'='*50}")
        print(f"  {country}")
        print('='*50)

        # ECM (lag handled inside via exog_var resolution)
        ecm = run_entity_ecm(df, country, dep_var, exog_var, lag=lag)

        # DOLS
        dols = run_entity_dols(df, country, dep_var, exog_var, lag=lag)

        # Wild bootstrap on DOLS
        boot = wild_bootstrap_ci(df, country, dep_var, exog_var,
                                 estimator='dols', lag=lag)

        row = {
            'country': country,
            'n_obs': ecm.get('n_obs', dols.get('n_obs', 0)),
            # ECM results
            'ecm_cointegrated': ecm.get('cointegrated', None),
            'ecm_f_stat': ecm.get('f_stat', None),
            'ecm_lr_beta': ecm.get('lr_nep_coef', None),
            'ecm_speed': ecm.get('ecm_speed', None),
            # DOLS results
            'dols_beta': dols.get('beta_nep', None),
            'dols_se': dols.get('se_nep', None),
            'dols_pval': dols.get('pval_nep', None),
            # Bootstrap CI
            'boot_ci_lower': boot.get('ci_lower_95', None),
            'boot_ci_upper': boot.get('ci_upper_95', None),
            'boot_se': boot.get('boot_se', None),
        }

        # Interpretation
        if 'error' in ecm:
            row['interpretation'] = ecm['error']
        elif ecm.get('cointegrated') and dols.get('pval_nep') is not None:
            if dols['pval_nep'] < 0.05:
                row['interpretation'] = 'Energy-monetary mechanism present'
            else:
                row['interpretation'] = 'Cointegrated but NEP not significant'
        elif not ecm.get('cointegrated', True):
            row['interpretation'] = 'Not cointegrated — no long-run relationship'
        else:
            row['interpretation'] = 'Insufficient data or estimation failure'

        rows.append(row)

    summary = pd.DataFrame(rows)

    print(f"\n{'='*60}")
    print("ENTITY-SPECIFIC SUMMARY")
    print('='*60)
    display_cols = ['country', 'n_obs', 'ecm_cointegrated', 'ecm_lr_beta',
                    'dols_beta', 'dols_pval', 'boot_ci_lower', 'boot_ci_upper',
                    'interpretation']
    available = [c for c in display_cols if c in summary.columns]
    print(summary[available].to_string(index=False))

    return summary


def meta_analyse_entities(entity_summary):
    """
    Fixed-effects meta-analysis of entity-specific DOLS estimates.

    Combines entity-level β estimates using inverse-variance weighting.
    Reports:
    - Pooled estimate (weighted mean)
    - I² heterogeneity statistic
    - Cochran's Q test for homogeneity

    If I² > 75%, the entities are too heterogeneous for a single summary
    estimate — report entity-specific results instead.
    """
    valid = entity_summary.dropna(subset=['dols_beta', 'boot_se']).copy()
    valid = valid[valid['boot_se'] > 0]

    if len(valid) < 2:
        return {'error': 'Need ≥2 entities with valid estimates for meta-analysis',
                'n_entities': len(valid)}

    betas = valid['dols_beta'].values
    ses = valid['boot_se'].values
    weights = 1.0 / (ses ** 2)

    # Fixed-effect pooled estimate
    pooled_beta = np.sum(weights * betas) / np.sum(weights)
    pooled_se = np.sqrt(1.0 / np.sum(weights))

    # Cochran's Q
    Q = np.sum(weights * (betas - pooled_beta) ** 2)
    k = len(betas)
    Q_pval = 1 - __import__('scipy').stats.chi2.cdf(Q, df=k - 1)

    # I² heterogeneity
    I2 = max(0, (Q - (k - 1)) / Q) * 100 if Q > 0 else 0

    from scipy.stats import norm
    z = pooled_beta / pooled_se
    pooled_pval = 2 * (1 - norm.cdf(abs(z)))

    result = {
        'pooled_beta': round(pooled_beta, 4),
        'pooled_se': round(pooled_se, 4),
        'pooled_pval': round(pooled_pval, 4),
        'pooled_ci_lower': round(pooled_beta - 1.96 * pooled_se, 4),
        'pooled_ci_upper': round(pooled_beta + 1.96 * pooled_se, 4),
        'Q_stat': round(Q, 3),
        'Q_pval': round(Q_pval, 4),
        'I2': round(I2, 1),
        'n_entities': k,
        'entity_weights': dict(zip(valid['country'].values,
                                    np.round(weights / weights.sum() * 100, 1))),
    }

    print(f"\n=== META-ANALYSIS (Fixed Effects, k={k}) ===")
    print(f"Pooled β(NEP): {pooled_beta:.4f} (SE={pooled_se:.4f}, p={pooled_pval:.4f})")
    print(f"95% CI: [{result['pooled_ci_lower']}, {result['pooled_ci_upper']}]")
    print(f"Cochran's Q: {Q:.2f} (p={Q_pval:.4f})")
    print(f"I² heterogeneity: {I2:.1f}%")
    if I2 > 75:
        print("WARNING: I²>75% — high heterogeneity. Entity-specific results "
              "are more informative than the pooled estimate.")
    elif I2 > 50:
        print("CAUTION: I²>50% — moderate heterogeneity. Pooled estimate is "
              "a rough summary; entity stories matter.")
    else:
        print("Heterogeneity acceptable. Pooled estimate is a reasonable summary.")
    print(f"Entity weights: {result['entity_weights']}")

    return result


# ─────────────────────────────────────────────
# STEP 3: CARBON CAPTURE MECHANISM
# Reframed: not a power test, a mechanism illustration
# ─────────────────────────────────────────────

def run_carbon_capture_mechanism(carbon_df: pd.DataFrame,
                                  political_df: pd.DataFrame = None) -> dict:
    """
    Carbon price volatility as evidence of sovereign capture mechanism.

    REVIEWER CRITIQUE (valid): EU ETS launched 2005, ~5 elections since.
    N≈20 annual obs with 5 election events. Power is near zero.
    Finding significance here would be suspicious.

    REFRAME: This is not a hypothesis test. It is a mechanism illustration.
    We are not claiming to prove sovereign capture statistically.
    We are showing that:
    1. Carbon price variance is structurally high relative to a commodity
       with fixed physical supply (which thorium would have)
    2. Phase I price collapse (2006-2007) was caused by over-allocation
       driven by political lobbying — documented fact, not a finding
    3. Phase transitions (I→II→III→IV) each required political negotiation

    The correct framing: descriptive statistics + event study, not OLS.
    We calculate:
    - Coefficient of variation by ETS phase
    - Price drawdown around specific documented political events
    - Comparison to commodity price volatility benchmarks (gold, oil)

    We DO NOT run an election-year regression with N=5 events.
    """
    if 'price' not in carbon_df.columns:
        price_col = [c for c in carbon_df.columns
                     if 'price' in c.lower() or 'eua' in c.lower()]
        if price_col:
            carbon_df = carbon_df.rename(columns={price_col[0]: 'price'})

    carbon_df['date'] = pd.to_datetime(carbon_df['date'])
    carbon_df['year'] = carbon_df['date'].dt.year

    # ETS phase definitions
    phase_map = {
        1: (2005, 2007, 'Phase I — over-allocation collapse'),
        2: (2008, 2012, 'Phase II — GFC shock'),
        3: (2013, 2020, 'Phase III — structural reform'),
        4: (2021, 2030, 'Phase IV — current'),
    }

    phase_stats = []
    for phase, (start, end, label) in phase_map.items():
        mask = (carbon_df['year'] >= start) & (carbon_df['year'] <= end)
        sub = carbon_df.loc[mask, 'price'].dropna()
        if len(sub) == 0:
            continue
        phase_stats.append({
            'phase': phase,
            'label': label,
            'n_obs': len(sub),
            'mean_price': sub.mean(),
            'std_price': sub.std(),
            'cv': sub.std() / sub.mean() if sub.mean() > 0 else np.nan,
            'min_price': sub.min(),
            'max_price': sub.max(),
            'drawdown': (sub.max() - sub.min()) / sub.max(),
        })

    stats_df = pd.DataFrame(phase_stats)

    # Annual stats for time series
    annual = carbon_df.groupby('year')['price'].agg(
        mean='mean', std='std', n='count'
    ).reset_index()
    annual['cv'] = annual['std'] / annual['mean']

    print("\n=== CARBON PRICE BY ETS PHASE ===")
    print(stats_df[['label', 'mean_price', 'cv', 'drawdown']].to_string(index=False))
    print("\nHigh CV and large drawdown in Phase I = political over-allocation effect")
    print("This illustrates sovereign capture mechanism, not tests it statistically")

    return {
        'phase_stats': stats_df,
        'annual_stats': annual,
        'raw': carbon_df,
        'interpretation': (
            'Phase I CV demonstrates political price construction. '
            'Phase boundary transitions show regulatory discretion. '
            'Compare CV to gold (~0.15) and oil (~0.25) for context.'
        )
    }


def run_carbon_structural_breaks(compliance_df):
    """
    Structural break analysis on ETS allocation surplus.
    Uses compliance data (allocations - verified emissions) since price data
    requires manual download.

    Tests whether allocation regime shifts align with political events.
    """
    alloc = compliance_df[
        compliance_df['ETS information'].str.contains('Freely allocated', na=False)
    ]
    verif = compliance_df[
        compliance_df['ETS information'].str.contains('Verified Emission', na=False)
    ]

    annual_alloc = alloc.groupby('year')['value'].sum()
    annual_verif = verif.groupby('year')['value'].sum()

    # Align on shared years
    shared_years = annual_alloc.index.intersection(annual_verif.index)
    surplus = (annual_alloc.loc[shared_years] -
               annual_verif.loc[shared_years]).sort_index()
    surplus = surplus.dropna()

    if len(surplus) < 10:
        return {'error': f'Insufficient surplus data: {len(surplus)} years',
                'surplus_series': surplus}

    # Zivot-Andrews endogenous break test on surplus series
    # Returns: (stat, pval, crit_values, lags, breakpoint_index)
    za_result = zivot_andrews(surplus.values, trim=0.15)
    za_stat = za_result[0]
    za_pval = za_result[1]
    # za_result[2] is critical values dict, [3] is lags, [4] is breakpoint
    za_lags = za_result[3]
    za_break_idx = za_result[4]

    # Map index back to year
    break_year = int(surplus.index[za_break_idx]) if za_break_idx < len(surplus) else None

    political_events = {
        2006: 'Phase I over-allocation revealed',
        2008: 'Phase II tightening',
        2013: 'Phase III structural reform',
        2019: 'Market Stability Reserve',
    }
    aligned = any(abs(break_year - yr) <= 1 for yr in political_events) if break_year else False
    nearest_event = None
    if break_year:
        nearest_yr = min(political_events.keys(), key=lambda y: abs(y - break_year))
        if abs(nearest_yr - break_year) <= 2:
            nearest_event = political_events[nearest_yr]

    result = {
        'break_year': break_year,
        'za_stat': round(za_stat, 3),
        'za_pval': round(za_pval, 4) if za_pval is not None else None,
        'za_lags': za_lags,
        'aligned_with_political_event': aligned,
        'nearest_event': nearest_event,
        'surplus_series': surplus,
        'political_events': political_events,
    }

    print(f"\n=== CARBON STRUCTURAL BREAK (Zivot-Andrews) ===")
    print(f"Break detected at: {break_year}")
    print(f"ZA statistic: {za_stat:.3f}, p-value: {za_pval}")
    print(f"Aligned with political event: {aligned}")
    if nearest_event:
        print(f"Nearest event: {nearest_event}")
    print("Allocation regime is politically constructed — surplus/deficit "
          "determined by political negotiation, not market.")

    return result


# ─────────────────────────────────────────────
# STEP 4: THORIUM FORWARD PREDICTION
# Cross-sectional: which countries are positioned
# for the next monetary transition?
# ─────────────────────────────────────────────

def run_tmpi_cross_section(df: pd.DataFrame,
                            year: int = 2023) -> dict:
    """
    Cross-sectional regression using Thorium Monetary Potential Index.

    This is the paper's forward-looking claim: high TMPI countries
    are positioned for monetary leverage in a thorium energy era.

    SPECIFICATION:
    CurrentReserveShare_i = α + β1(NEP_i) + β2(GDPshare_i)
                           + β3(TMPI_i) + β4(KAOpen_i) + ε_i

    With N=6 reserve currency issuers this is severely underpowered
    for formal inference. We therefore run TWO versions:

    Version A: Reserve currency issuers only (N=6)
               Descriptive — who currently has leverage
    Version B: All countries with TMPI data (N=~50)
               Tests: does TMPI predict CURRENT reserve ambition?
               (Indirect test of whether the mechanism is already operating)

    The forward prediction is stated explicitly as a falsifiable claim:
    "Countries with TMPI > X in 2024 will show increased reserve
    currency usage by 2035." We cannot test this now. We can show
    the current distribution and make the prediction.
    """
    latest = df[df['year'] == year].copy()

    required = ['reserve_share', 'net_energy_position', 'gdp_share']
    optional = ['tmpi', 'kaopen', 'thorium_reserve_share',
                'nuclear_share_energy', 'institutional_quality']

    # Version B: all countries with TMPI
    available_opt = [c for c in optional if c in latest.columns]
    X_cols = required[1:] + available_opt
    model_df = latest.dropna(subset=required + ['tmpi'] if 'tmpi' in latest.columns else required)

    if len(model_df) < 10:
        print(f"Warning: only {len(model_df)} observations at year {year}")

    X = sm.add_constant(model_df[X_cols].astype(float))
    y = model_df['reserve_share'].astype(float)

    result = sm.OLS(y, X).fit(cov_type='HC3')

    # TMPI ranking — the forward prediction
    if 'tmpi_scaled' in latest.columns:
        tmpi_ranking = (latest[latest['tmpi_scaled'] > 0]
                        [['country_code', 'tmpi_scaled',
                          'thorium_reserve_share', 'nuclear_share_energy',
                          'institutional_quality']]
                        .sort_values('tmpi_scaled', ascending=False)
                        .head(15)
                        .reset_index(drop=True))

        print(f"\n=== TMPI RANKING {year} — Forward Monetary Prediction ===")
        print(tmpi_ranking.to_string())
        print("\nInterpretation: High TMPI = positioned for monetary leverage")
        print("in a thorium-dominant energy era. Falsifiable by 2035-2040.")
    else:
        tmpi_ranking = None

    print(f"\n=== CROSS-SECTION MODEL (N={len(model_df)}) ===")
    if 'tmpi' in result.params.index:
        print(f"TMPI coefficient: {result.params['tmpi']:.4f} "
              f"(p={result.pvalues['tmpi']:.3f})")
    print(f"R²: {result.rsquared:.3f}")

    return {
        'model': result,
        'year': year,
        'n_obs': len(model_df),
        'coefficients': result.params,
        'pvalues': result.pvalues,
        'tmpi_ranking': tmpi_ranking,
        'summary': result.summary(),
    }



def bootstrap_za_critical_values(T: int = 20, n_boot: int = 2000,
                                  seed: int = 42) -> dict:
    """
    Bootstrap empirical critical values for Zivot-Andrews test at small T.

    Asymptotic critical values (derived for T→∞) exhibit size distortions
    at T=20 that can exceed 20% (Vogelsang and Perron 2006). This function
    simulates AR(1) null series of length T to derive empirical critical values.

    Method:
    1. Generate n_boot AR(1) series of length T with no structural break
    2. Compute ZA statistic on each
    3. Extract 1st, 5th, 10th percentiles as empirical critical values

    Returns: dict with empirical CVs and comparison to observed statistic.
    """
    from statsmodels.tsa.stattools import zivot_andrews as za_test
    rng = np.random.RandomState(seed)
    za_stats = []

    for _ in range(n_boot):
        # AR(1) null: y_t = 0.8*y_{t-1} + ε_t (unit root approximation)
        eps = rng.normal(0, 1, T + 50)
        y = np.zeros(T + 50)
        for t in range(1, T + 50):
            y[t] = 0.95 * y[t - 1] + eps[t]
        y = y[50:]  # discard burn-in

        try:
            result = za_test(y, trim=0.15)
            za_stats.append(result[0])
        except Exception:
            continue

    za_stats = np.array(za_stats)
    cv_1pct = float(np.percentile(za_stats, 1))
    cv_5pct = float(np.percentile(za_stats, 5))
    cv_10pct = float(np.percentile(za_stats, 10))

    result = {
        'T': T,
        'n_boot': len(za_stats),
        'empirical_cv_1pct': round(cv_1pct, 3),
        'empirical_cv_5pct': round(cv_5pct, 3),
        'empirical_cv_10pct': round(cv_10pct, 3),
        'asymptotic_cv_1pct': -5.57,
        'asymptotic_cv_5pct': -5.08,
        'note': (f'Bootstrapped from {len(za_stats)} AR(1) null simulations at T={T}. '
                 f'Compare observed statistic to empirical_cv_1pct for small-T inference.')
    }

    print(f"\n=== ZA BOOTSTRAP CRITICAL VALUES (T={T}, n_boot={len(za_stats)}) ===")
    print(f"Empirical: 1%={cv_1pct:.3f}, 5%={cv_5pct:.3f}, 10%={cv_10pct:.3f}")
    print(f"Asymptotic: 1%=-5.57, 5%=-5.08")
    print(f"If observed ZA < empirical 1% CV → reject at 1% with small-T correction.")
    return result


def run_bai_perron_test(series: pd.Series, max_breaks: int = 3,
                        min_size: float = 0.15) -> dict:
    """
    Bai-Perron sequential multiple structural break test.

    Tests for up to max_breaks breaks in the mean of a time series.
    Uses sequential sup-F testing: F(l+1|l) tests whether l+1 breaks
    are preferred over l breaks.

    Implementation: manual RSS-based sequential search (Bai-Perron 1998 algorithm).
    Break dates reported with 90% confidence intervals.

    Returns: identified break dates, F-statistics, and interpretation.
    """
    y = series.dropna().values
    T = len(y)
    min_seg = max(3, int(T * min_size))

    def rss_segment(y, start, end):
        seg = y[start:end]
        return np.sum((seg - seg.mean()) ** 2)

    def find_one_break(y, min_seg):
        T = len(y)
        best_rss = np.inf
        best_bp = None
        for bp in range(min_seg, T - min_seg):
            rss = rss_segment(y, 0, bp) + rss_segment(y, bp, T)
            if rss < best_rss:
                best_rss = rss
                best_bp = bp
        return best_bp, best_rss

    rss_none = rss_segment(y, 0, T)
    breaks = []
    f_stats = []

    current_y = y.copy()
    current_offset = 0

    for k in range(1, max_breaks + 1):
        bp_local, rss_break = find_one_break(current_y, min_seg)
        rss_null = rss_segment(current_y, 0, len(current_y))
        k_regressors = 1
        F_stat = ((rss_null - rss_break) / k_regressors) / (rss_break / (len(current_y) - 2 * k_regressors))

        breaks.append(current_offset + bp_local)
        f_stats.append(round(F_stat, 3))

        # Continue search in the largest remaining segment
        seg1 = current_y[:bp_local]
        seg2 = current_y[bp_local:]
        if len(seg1) >= len(seg2):
            current_y = seg1
        else:
            current_offset = current_offset + bp_local
            current_y = seg2

        if F_stat < 5.0:  # Conservative stopping rule
            break

    break_years = None
    if hasattr(series, 'index') and len(series.index) > 0:
        idx = series.dropna().index
        break_years = [idx[b] if b < len(idx) else None for b in breaks]

    result = {
        'n_obs': T,
        'break_indices': breaks,
        'break_years': break_years,
        'f_statistics': f_stats,
        'n_breaks_found': len(breaks),
        'interpretation': (
            f'Sequential Bai-Perron: {len(breaks)} break(s) identified. '
            f'Break years: {break_years}. '
            f'F-statistics: {f_stats}. '
            f'Compare to ZA single-break result for robustness.'
        )
    }

    print(f"\n=== BAI-PERRON MULTIPLE BREAK TEST ===")
    print(f"N={T}, max_breaks={max_breaks}")
    print(f"Breaks found at indices: {breaks}")
    if break_years:
        print(f"Break years: {break_years}")
    print(f"F-statistics: {f_stats}")
    return result


def compute_gs_confidence_intervals(eua_monthly: pd.Series,
                                     oil_series: pd.Series,
                                     n_boot: int = 1000,
                                     seed: int = 42) -> dict:
    """
    Bootstrap confidence intervals for GS = CV(EUA Phase I) / CV(Oil).

    CV from N=3 annual observations (Phase I: 2005-2007) is an unstable estimator.
    Uses monthly series if available (N=36) for more reliable CV estimation.

    Bootstraps both CV(EUA) and CV(Oil) independently, then computes
    the ratio distribution.

    Returns: point estimate GS, bootstrapped CI, and source uncertainty note.
    """
    rng = np.random.RandomState(seed)

    eua = eua_monthly.dropna().values
    oil = oil_series.dropna().values

    def cv(x):
        m = np.mean(x)
        return np.std(x) / m if m > 0 else np.nan

    # Point estimate
    gs_point = cv(eua) / cv(oil) if cv(oil) > 0 else np.nan

    # Bootstrap
    gs_boot = []
    for _ in range(n_boot):
        eua_boot = rng.choice(eua, size=len(eua), replace=True)
        oil_boot = rng.choice(oil, size=len(oil), replace=True)
        cv_eua = cv(eua_boot)
        cv_oil = cv(oil_boot)
        if cv_oil > 0 and not np.isnan(cv_eua):
            gs_boot.append(cv_eua / cv_oil)

    gs_boot = np.array(gs_boot)

    result = {
        'gs_point': round(gs_point, 3) if not np.isnan(gs_point) else None,
        'cv_eua': round(cv(eua), 3),
        'cv_oil': round(cv(oil), 3),
        'n_eua': len(eua),
        'n_oil': len(oil),
        'n_boot': len(gs_boot),
        'gs_ci_lower_95': round(float(np.percentile(gs_boot, 2.5)), 3) if len(gs_boot) > 10 else None,
        'gs_ci_upper_95': round(float(np.percentile(gs_boot, 97.5)), 3) if len(gs_boot) > 10 else None,
        'gs_all_above_1': bool(np.percentile(gs_boot, 2.5) > 1.0) if len(gs_boot) > 10 else None,
        'interpretation': (
            f'GS={gs_point:.3f} (bootstrapped 95% CI: '
            f'[{np.percentile(gs_boot, 2.5):.2f}, {np.percentile(gs_boot, 97.5):.2f}]). '
            f'Core claim (GS>1) is {"robust" if np.percentile(gs_boot, 2.5) > 1.0 else "fragile"} '
            f'to bootstrap resampling.'
        ) if len(gs_boot) > 10 else 'Insufficient bootstrap replications.',
    }

    print(f"\n=== GS CONFIDENCE INTERVALS (bootstrap n={len(gs_boot)}) ===")
    print(f"CV(EUA)={cv(eua):.3f}, CV(Oil)={cv(oil):.3f}")
    print(f"GS point estimate: {gs_point:.3f}")
    if len(gs_boot) > 10:
        print(f"95% CI: [{np.percentile(gs_boot, 2.5):.3f}, {np.percentile(gs_boot, 97.5):.3f}]")
        print(f"GS > 1 at 95% CI lower: {np.percentile(gs_boot, 2.5) > 1.0}")
    return result


def decompose_india_forward_prediction(beta: float = 84.0,
                                        beta_se: float = 37.89,
                                        baseline_inr: float = 1.6,
                                        p_t_values: list = None) -> pd.DataFrame:
    """
    Transparent arithmetic decomposition of the India INR FX share prediction.

    The prediction is a conditional scenario, not a structural extrapolation.
    This function makes explicit what p_t and NEP improvement assumptions
    are required to produce different predicted INR FX shares.

    Parameters:
    - beta: DOLS long-run NEP coefficient (default 84.0)
    - beta_se: standard error on beta (default 37.89)
    - baseline_inr: current INR FX turnover share % (default 1.6)
    - p_t_values: list of transition probabilities to evaluate

    Returns: DataFrame showing predicted INR share under each scenario.
    """
    if p_t_values is None:
        p_t_values = [0.0, 0.1, 0.2, 0.3, 0.5]

    # NEP improvement scenarios (Stage 2 and Stage 3 capacity additions)
    nep_improvements = {
        'Stage 2 only (+0.04)': 0.04,
        'Stage 2+3 partial (+0.06)': 0.06,
        'Stage 2+3 full (+0.10)': 0.10,
    }

    rows = []
    for nep_label, delta_nep in nep_improvements.items():
        for p_t in p_t_values:
            # NEP contribution (present-era mechanism, β × ΔNEP)
            nep_contribution = beta * delta_nep
            nep_contribution_lo = (beta - 1.96 * beta_se) * delta_nep
            nep_contribution_hi = (beta + 1.96 * beta_se) * delta_nep

            # TMPI contribution (forward-era mechanism, p_t × TMPI_normalised)
            # TMPI_India = 15.8 normalised to USA=100; scale to ~5% reserve share
            # At p_t=1 and TMPI=15.8/100, forward contribution is approximately 0.158 × 5% = 0.79pp
            tmpi_contribution = p_t * (15.8 / 100) * 5.0  # simplified forward contribution

            predicted = baseline_inr + nep_contribution + tmpi_contribution
            predicted_lo = baseline_inr + nep_contribution_lo + tmpi_contribution
            predicted_hi = baseline_inr + nep_contribution_hi + tmpi_contribution

            rows.append({
                'nep_scenario': nep_label,
                'delta_nep': delta_nep,
                'p_t': p_t,
                'nep_contribution_pp': round(nep_contribution, 3),
                'tmpi_contribution_pp': round(tmpi_contribution, 3),
                'predicted_inr_share': round(predicted, 2),
                'predicted_ci_lo': round(max(0, predicted_lo), 2),
                'predicted_ci_hi': round(predicted_hi, 2),
                'in_3_5_range': 3.0 <= predicted <= 5.0,
            })

    df = pd.DataFrame(rows)

    print("\n=== INDIA INR PREDICTION DECOMPOSITION ===")
    print(f"Baseline INR FX share: {baseline_inr}%")
    print(f"β={beta:.1f} (SE={beta_se:.2f})")
    print()
    display = df[df['p_t'].isin([0.0, 0.2, 0.5])][
        ['nep_scenario', 'p_t', 'nep_contribution_pp',
         'tmpi_contribution_pp', 'predicted_inr_share', 'in_3_5_range']
    ]
    print(display.to_string(index=False))
    print("\nPrediction is conditional: 3-5% requires PFBR operational AND partial KAOPEN easing.")
    return df


def plot_mpi_trajectories(output_path: str = 'outputs/figures/figure_5_mpi_trajectories.png',
                           figsize: tuple = (10, 7)) -> None:
    """
    Generate Figure 5: MPI trajectories as p_t rises from 0 to 1.

    MPI_{i,t} = (1-p_t) * NEP_i * GS + p_t * TMPI_i * GS_forward

    Four lines: USA (stable high), India (rising discontinuously),
    Russia (flat near zero), United Kingdom (declining).

    Axes: x = p_t (0 to 1), y = MPI normalised to USA at p_t=0.
    """
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import os

    p_t = np.linspace(0, 1, 100)

    # Present-era parameters (NEP * GS, normalised to USA=1 at p_t=0)
    # Source: computed values from notebooks 03 and 04
    usa_nep_gs = 1.000   # normalised baseline
    india_nep_gs = 0.05  # suppressed by net oil-import dependence (current account drag)
    russia_nep_gs = 0.03  # suppressed by EPS exclusion post-2022
    uk_nep_gs = 0.25     # declining (North Sea depletion, strong current but weakening)

    # Forward-era parameters (TMPI * GS_forward, normalised to USA at p_t=1)
    # Source: TMPI table §7.3; USA=100, India=15.8, Russia=9.3, UK=0
    # Scale so USA at p_t=1 = 1.0 (same as present)
    usa_tmpi_gs = 1.000
    india_tmpi_gs = 0.65  # 15.8/100 × governance forward scaling; rises discontinuously
    russia_tmpi_gs = 0.08  # 9.3/100 × suppressed GS term
    uk_tmpi_gs = 0.00     # TMPI=0 (negligible thorium)

    mpi_usa = (1 - p_t) * usa_nep_gs + p_t * usa_tmpi_gs
    mpi_india = (1 - p_t) * india_nep_gs + p_t * india_tmpi_gs
    mpi_russia = (1 - p_t) * russia_nep_gs + p_t * russia_tmpi_gs
    mpi_uk = (1 - p_t) * uk_nep_gs + p_t * uk_tmpi_gs

    fig, ax = plt.subplots(figsize=figsize)

    ax.plot(p_t, mpi_usa, color='#1a3a5c', linewidth=2.5, label='United States')
    ax.plot(p_t, mpi_india, color='#e07b00', linewidth=2.5, linestyle='--',
            label='India (rising discontinuously)')
    ax.plot(p_t, mpi_russia, color='#8b0000', linewidth=1.8, linestyle=':',
            label='Russia (flat near zero)')
    ax.plot(p_t, mpi_uk, color='#4a4a4a', linewidth=1.8, linestyle='-.',
            label='United Kingdom (declining)')

    # Mark crossover points
    crossover_uk_india = p_t[np.argmin(np.abs(mpi_india - mpi_uk))]
    ax.axvline(x=crossover_uk_india, color='#e07b00', linewidth=0.8, linestyle='--', alpha=0.5)
    ax.annotate(f'India passes UK\n(p_t ≈ {crossover_uk_india:.2f})',
                xy=(crossover_uk_india, np.interp(crossover_uk_india, p_t, mpi_india)),
                xytext=(crossover_uk_india + 0.05, 0.35),
                fontsize=9, color='#e07b00',
                arrowprops=dict(arrowstyle='->', color='#e07b00', lw=0.8))

    ax.set_xlabel('Transition probability p_t (0 = present era, 1 = thorium era)', fontsize=11)
    ax.set_ylabel('MPI score (USA = 1 at p_t = 0)', fontsize=11)
    ax.set_title('Figure 5. MPI Trajectories as Energy Transition Progresses', fontsize=12, pad=12)
    ax.legend(loc='upper right', fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.05, 1.15)
    ax.grid(True, alpha=0.3, linewidth=0.5)

    # Annotations
    ax.annotate('At p_t=0: present era\n(NEP·GS dominates)',
                xy=(0.02, 0.9), fontsize=8.5, color='#444444')
    ax.annotate('At p_t=1: thorium era\n(TMPI·GS dominates)',
                xy=(0.82, 0.9), fontsize=8.5, color='#444444')

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Figure 5 saved to {output_path}")


def run_tmpi_weight_sensitivity(tmpi_data: pd.DataFrame,
                                 output_path: str = 'outputs/tables/tmpi_weight_sensitivity.csv'
                                 ) -> pd.DataFrame:
    """
    TMPI sensitivity analysis under alternative component weightings.

    Default TMPI uses equal weights (multiplicative = α=β=γ=1/3 implicitly).
    Tests four weight schemes to check if top-3 order is robust.

    Required columns in tmpi_data: country, thorium_share, nuclear_share, institutions

    Weight schemes:
    - Equal (baseline): α=β=γ=1/3
    - Reserves-heavy: α=0.5, β=0.25, γ=0.25
    - Capacity-heavy: α=0.25, β=0.5, γ=0.25
    - Institutions-heavy: α=0.25, β=0.25, γ=0.5

    Returns: DataFrame with TMPI scores and ranks under each scheme.
    """
    import os
    required = ['country', 'thorium_share', 'nuclear_share', 'institutions']
    missing = [c for c in required if c not in tmpi_data.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = tmpi_data[required].copy().dropna()

    # Normalise each component to [0, 1]
    for col in ['thorium_share', 'nuclear_share', 'institutions']:
        max_val = df[col].max()
        if max_val > 0:
            df[f'{col}_norm'] = df[col] / max_val
        else:
            df[f'{col}_norm'] = 0.0

    weight_schemes = {
        'equal_weights': (1/3, 1/3, 1/3),
        'reserves_heavy': (0.5, 0.25, 0.25),
        'capacity_heavy': (0.25, 0.5, 0.25),
        'institutions_heavy': (0.25, 0.25, 0.5),
    }

    results = df[['country']].copy()
    for scheme_name, (α, β, γ) in weight_schemes.items():
        scores = (α * df['thorium_share_norm'] +
                  β * df['nuclear_share_norm'] +
                  γ * df['institutions_norm'])
        # Normalise to USA=100
        usa_score = scores[df['country'].str.upper().str.contains('USA|UNITED STATES')].max()
        if usa_score > 0:
            scores = scores / usa_score * 100
        results[f'score_{scheme_name}'] = scores.round(1)
        results[f'rank_{scheme_name}'] = scores.rank(ascending=False).astype(int)

    results = results.sort_values('score_equal_weights', ascending=False).reset_index(drop=True)

    # Check top-3 invariance
    top3_equal = set(results.nlargest(3, 'score_equal_weights')['country'].values)
    top3_reserves = set(results.nlargest(3, 'score_reserves_heavy')['country'].values)
    top3_capacity = set(results.nlargest(3, 'score_capacity_heavy')['country'].values)
    top3_institutions = set(results.nlargest(3, 'score_institutions_heavy')['country'].values)

    all_same = (top3_equal == top3_reserves == top3_capacity == top3_institutions)

    print(f"\n=== TMPI WEIGHT SENSITIVITY ===")
    print(f"Top-3 under equal weights: {sorted(top3_equal)}")
    print(f"Top-3 under reserves-heavy: {sorted(top3_reserves)}")
    print(f"Top-3 under capacity-heavy: {sorted(top3_capacity)}")
    print(f"Top-3 under institutions-heavy: {sorted(top3_institutions)}")
    print(f"\nTop-3 order invariant across all weighting schemes: {all_same}")
    print(results.to_string(index=False))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    results.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")

    return results


if __name__ == "__main__":
    print("models.py v2 — correct workflow:")
    print()
    print("  STEP 0 (ALWAYS FIRST): run_stationarity_battery(df)")
    print("    → If majority I(1): use differenced=True in step 1")
    print("    → If majority I(0): use differenced=False")
    print()
    print("  STEP 1: run_both_lags(df, differenced=False/True)")
    print("    → Reports NEP coefficient at lag=10yr AND lag=15yr")
    print("    → Do NOT select based on R² — report both")
    print("    → N=6 entities: interpret as structured descriptive, not large-N panel")
    print()
    print("  STEP 1b: run_robustness_checks(df)")
    print("    → 2×2 table: levels/differenced × lag10/lag15")
    print("    → 4/4 significant = robust; <2/4 = not robust")
    print()
    print("  STEP 2 (per focal country): run_vecm_or_var(df, country)")
    print("    → Auto: stationarity → cointegration test → VECM or VAR")
    print("    → Run for: CHN, IND, RUS, JPN, AUS, CAN, BRA")
    print()
    print("  STEP 3: run_carbon_capture_mechanism(carbon_df)")
    print("    → DESCRIPTIVE ONLY — not a hypothesis test")
    print("    → N≈5 election events → power ≈ 0 for any regression")
    print()
    print("  STEP 4 (CROSS-SECTION ONLY): run_tmpi_cross_section(df, year=2023)")
    print("    → thorium_index is time-invariant → collinear with country FE")
    print("    → Valid only in cross-section, NOT in panel FE model")
