"""
clean.py
Data cleaning, standardization, and merging pipeline.
Converts raw pulled data -> model-ready panel.

Run after data_pull.py completes all pulls.
Output: data/processed/panel_model_ready.csv

Country code strategy:
  - OWID uses country names (not ISO3)
  - World Bank uses ISO3 country codes
  - IMF COFER uses currency codes (USD, EUR, etc.)
  - We standardize everything to ISO3 for the panel
  - COFER reserve shares are joined by currency->country mapping
"""

import os
import sys
import warnings
import pandas as pd
import numpy as np

# Make src/ importable from any working directory
_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

DATA_RAW = os.path.join(_SRC_DIR, '..', 'data', 'raw')
DATA_PROCESSED = os.path.join(_SRC_DIR, '..', 'data', 'processed')

# Focal countries whose missingness we actively warn about
FOCAL_ISO3 = {'CHN', 'IND', 'RUS', 'JPN', 'EMU'}

# Master country-name -> ISO3 mapping used across OWID and World Bank sources
COUNTRY_NAME_TO_ISO3 = {
    # Core focal countries
    'China':                        'CHN',
    'India':                        'IND',
    'Russia':                       'RUS',
    'Japan':                        'JPN',
    'United States':                'USA',
    'Germany':                      'DEU',
    'United Kingdom':               'GBR',
    'France':                       'FRA',
    'Switzerland':                  'CHE',
    'Australia':                    'AUS',
    'Canada':                       'CAN',
    'Brazil':                       'BRA',
    'South Africa':                 'ZAF',
    'Norway':                       'NOR',
    'Egypt':                        'EGY',
    'Turkey':                       'TUR',
    'Venezuela':                    'VEN',
    'World':                        'WORLD',

    # Additional countries for broader panel coverage
    'Argentina':                    'ARG',
    'Austria':                      'AUT',
    'Belgium':                      'BEL',
    'Chile':                        'CHL',
    'Colombia':                     'COL',
    'Czech Republic':               'CZE',
    'Denmark':                      'DNK',
    'Finland':                      'FIN',
    'Greece':                       'GRC',
    'Hungary':                      'HUN',
    'Indonesia':                    'IDN',
    'Iran':                         'IRN',
    'Iraq':                         'IRQ',
    'Ireland':                      'IRL',
    'Israel':                       'ISR',
    'Italy':                        'ITA',
    'Kazakhstan':                   'KAZ',
    'Kuwait':                       'KWT',
    'Malaysia':                     'MYS',
    'Mexico':                       'MEX',
    'Netherlands':                  'NLD',
    'New Zealand':                  'NZL',
    'Nigeria':                      'NGA',
    'North Korea':                  'PRK',
    'Pakistan':                     'PAK',
    'Philippines':                  'PHL',
    'Poland':                       'POL',
    'Portugal':                     'PRT',
    'Qatar':                        'QAT',
    'Romania':                      'ROU',
    'Saudi Arabia':                 'SAU',
    'Singapore':                    'SGP',
    'South Korea':                  'KOR',
    'Spain':                        'ESP',
    'Sweden':                       'SWE',
    'Taiwan':                       'TWN',
    'Thailand':                     'THA',
    'Ukraine':                      'UKR',
    'United Arab Emirates':         'ARE',
    'Uzbekistan':                   'UZB',
    'Vietnam':                      'VNM',

    # World Bank name variants (often differ from OWID)
    'Russian Federation':           'RUS',
    'Korea, Rep.':                  'KOR',
    'Korea, Dem. People\'s Rep.':   'PRK',
    'Iran, Islamic Rep.':           'IRN',
    'Egypt, Arab Rep.':             'EGY',
    'Yemen, Rep.':                  'YEM',
    'Venezuela, RB':                'VEN',
    'Slovak Republic':              'SVK',
    'Kyrgyz Republic':              'KGZ',
    'Lao PDR':                      'LAO',
    'Congo, Dem. Rep.':             'COD',
    'Congo, Rep.':                  'COG',
    'Cabo Verde':                   'CPV',
    'Bahamas, The':                 'BHS',
    'Gambia, The':                  'GMB',
    'Micronesia, Fed. Sts.':        'FSM',
    'St. Lucia':                    'LCA',
    'St. Vincent and the Grenadines': 'VCT',
    'Sao Tome and Principe':        'STP',
    'Hong Kong SAR, China':         'HKG',
    'Macao SAR, China':             'MAC',
    'West Bank and Gaza':           'PSE',
    'Brunei Darussalam':            'BRN',
    # Alternate spellings / historical names that appear in OWID
    'Czechia':                      'CZE',
    'Democratic Republic of Congo': 'COD',
    'Democratic Republic of the Congo': 'COD',
    'Republic of the Congo':        'COG',
    'Congo':                        'COG',
    'Cote d\'Ivoire':               'CIV',
    "Cote d'Ivoire":                'CIV',
    'Bolivia':                      'BOL',
    'Tanzania':                     'TZA',
    'Ethiopia':                     'ETH',
    'Ghana':                        'GHA',
    'Kenya':                        'KEN',
    'Morocco':                      'MAR',
    'Mozambique':                   'MOZ',
    'Myanmar':                      'MMR',
    'Peru':                         'PER',
    'Serbia':                       'SRB',
    'Slovakia':                     'SVK',
    'Trinidad and Tobago':          'TTO',
    'Tunisia':                      'TUN',
    'Ecuador':                      'ECU',
    'Libya':                        'LBY',
    'Algeria':                      'DZA',
    'Angola':                       'AGO',
    'Bahrain':                      'BHR',
    'Bangladesh':                   'BGD',
    'Belarus':                      'BLR',
    'Bosnia and Herzegovina':       'BIH',
    'Cameroon':                     'CMR',
    'Croatia':                      'HRV',
    'Cuba':                         'CUB',
    'Cyprus':                       'CYP',
    'Estonia':                      'EST',
    'Gabon':                        'GAB',
    'Georgia':                      'GEO',
    'Honduras':                     'HND',
    'Iceland':                      'ISL',
    'Jordan':                       'JOR',
    'Latvia':                       'LVA',
    'Lebanon':                      'LBN',
    'Lithuania':                    'LTU',
    'Luxembourg':                   'LUX',
    'Malta':                        'MLT',
    'Mongolia':                     'MNG',
    'Nepal':                        'NPL',
    'North Macedonia':              'MKD',
    'Oman':                         'OMN',
    'Panama':                       'PAN',
    'Paraguay':                     'PRY',
    'Slovenia':                     'SVN',
    'Sri Lanka':                    'LKA',
    'Sudan':                        'SDN',
    'Syria':                        'SYR',
    'Tajikistan':                   'TJK',
    'Turkmenistan':                 'TKM',
    'Uruguay':                      'URY',
    'Yemen':                        'YEM',
    'Zambia':                       'ZMB',
    'Zimbabwe':                     'ZWE',

    # European Union / Euro area aggregates — mapped to EMU to join with COFER EUR rows
    # (CURRENCY_TO_ISO3 maps EUR -> EMU)
    'European Union (27)':          'EMU',
    'Euro area':                    'EMU',   # World Bank "Euro area" aggregate
    'Europe':                       'EUR_REGION',
    'Asia Pacific':                 'ASIA_PAC',
    'Africa':                       'AFR_REGION',
    'North America':                'NAM_REGION',
    'South & Central America':      'SAM_REGION',
    'Middle East':                  'ME_REGION',
    'CIS':                          'CIS_REGION',
}

# IMF COFER currency -> ISO3 mapping
CURRENCY_TO_ISO3 = {
    'USD': 'USA',
    'EUR': 'EMU',   # Euro area — not a single country; kept as EMU
    'JPY': 'JPN',
    'GBP': 'GBR',
    'CNY': 'CHN',
    'CHF': 'CHE',
}


# ---------------------------------------------------------------------------
# Function 1: standardize_owid_country_codes
# ---------------------------------------------------------------------------

def standardize_owid_country_codes(df: pd.DataFrame) -> pd.DataFrame:
    """
    OWID uses full country names. Add an 'iso3' column using COUNTRY_NAME_TO_ISO3.

    Warns if any focal country (CHN/IND/RUS/JPN) fails to map — those are
    critical for the model and a miss would silently drop key observations.

    Parameters
    ----------
    df : pd.DataFrame
        Any OWID dataframe that has a 'country' column.

    Returns
    -------
    pd.DataFrame with added 'iso3' column (NaN where name not in mapping).
    """
    if 'country' not in df.columns:
        raise ValueError("standardize_owid_country_codes: df must have a 'country' column.")

    df = df.copy()
    df['iso3'] = df['country'].map(COUNTRY_NAME_TO_ISO3)

    # Warn about unmapped focal countries
    focal_names = {v: k for k, v in COUNTRY_NAME_TO_ISO3.items() if k in FOCAL_ISO3}
    for iso in FOCAL_ISO3:
        # Check whether ANY row for this ISO3 code mapped successfully
        if iso not in df['iso3'].values:
            # Try to find what name was used
            reverse_map = {v: k for k, v in COUNTRY_NAME_TO_ISO3.items()}
            expected_name = reverse_map.get(iso, iso)
            warnings.warn(
                f"standardize_owid_country_codes: focal country '{iso}' "
                f"(expected country name: '{expected_name}') did not map. "
                f"Check if name appears differently in source data."
            )

    n_mapped = df['iso3'].notna().sum()
    n_total = len(df)
    n_unmapped = n_total - n_mapped
    if n_unmapped > 0:
        print(f"  Country code mapping: {n_mapped}/{n_total} rows mapped "
              f"({n_unmapped} unmapped — non-focal regions/aggregates expected).")

    return df


# ---------------------------------------------------------------------------
# Function 2: clean_owid_energy
# ---------------------------------------------------------------------------

def clean_owid_energy(raw_path: str = None) -> pd.DataFrame:
    """
    Load and clean OWID energy dataset.

    Source file: data/raw/owid_energy.csv
    OWID energy codebook: https://github.com/owid/energy-data/blob/master/owid-energy-codebook.csv

    Key column mappings (OWID uses TWh suffixes and underscored names):
      coal_production         -> coal_production
      oil_production          -> oil_production
      gas_production          -> gas_production
      nuclear_consumption     -> nuclear_consumption  (or nuclear_electricity)
      renewables_consumption  -> renewables_consumption (or other_renewable_consumption)
      primary_energy_consumption -> primary_energy_consumption
      net_elec_imports        -> net_elec_imports (if present)

    Returns
    -------
    pd.DataFrame with columns: year, country_code, plus energy columns.
    Only rows where iso3 is not NaN are retained.
    """
    if raw_path is None:
        raw_path = os.path.join(DATA_RAW, 'owid_energy.csv')

    if not os.path.exists(raw_path):
        print(f"clean_owid_energy: file not found at {raw_path}. Skipping.")
        return None

    print(f"Loading OWID energy: {raw_path}")
    df = pd.read_csv(raw_path, low_memory=False)

    # Normalize column names for matching
    df.columns = [c.strip().lower() for c in df.columns]

    # Apply country name -> ISO3
    df = standardize_owid_country_codes(df)
    df = df[df['iso3'].notna()].copy()

    # Ensure year is integer
    df['year'] = pd.to_numeric(df['year'], errors='coerce').dropna().astype(int)
    df = df[df['year'].notna()].copy()
    df['year'] = df['year'].astype(int)

    # Build column mapping: desired_name -> actual_owid_col
    # OWID energy codebook column names (as of 2023-2024 dataset)
    col_candidates = {
        'coal_production': [
            'coal_production',          # TWh
        ],
        'oil_production': [
            'oil_production',           # TWh
        ],
        'gas_production': [
            'gas_production',           # TWh
        ],
        'nuclear_consumption': [
            'nuclear_consumption',
            'nuclear_electricity',
            'electricity_from_nuclear',
        ],
        'renewables_consumption': [
            'renewables_consumption',
            'other_renewable_consumption',
            'renewables_electricity',
            'electricity_from_renewables',
            'other_renewables_electricity_including_bioenergy',
        ],
        'primary_energy_consumption': [
            'primary_energy_consumption',
            'energy_consumption',
        ],
        'net_elec_imports': [
            'net_elec_imports',
            'net_electricity_imports',
            'electricity_net_imports',
        ],
    }

    selected = {'year': 'year', 'iso3': 'country_code'}
    for desired, candidates in col_candidates.items():
        for cand in candidates:
            if cand in df.columns:
                selected[cand] = desired
                break
        else:
            if desired != 'net_elec_imports':  # net_elec_imports is optional
                print(f"  Warning: could not find column for '{desired}' in OWID energy data. "
                      f"Tried: {candidates}")

    # Select and rename
    keep_cols = list(selected.keys())
    df_out = df[keep_cols].rename(columns=selected)

    # Drop duplicate country_code/year (keep first)
    df_out = df_out.drop_duplicates(subset=['country_code', 'year'])

    # Cast energy columns to numeric
    energy_cols = [c for c in df_out.columns if c not in ('country_code', 'year')]
    for col in energy_cols:
        df_out[col] = pd.to_numeric(df_out[col], errors='coerce')

    print(f"  OWID energy cleaned: {len(df_out)} rows, "
          f"{df_out['country_code'].nunique()} countries, "
          f"years {df_out['year'].min()}-{df_out['year'].max()}")
    print(f"  Columns: {list(df_out.columns)}")

    return df_out


# ---------------------------------------------------------------------------
# Function 3: clean_world_bank
# ---------------------------------------------------------------------------

def clean_world_bank(raw_path: str = None) -> pd.DataFrame:
    """
    Load and clean World Bank WDI data.

    World Bank data pulled by data_pull.py has columns:
      country (full name), year, gdp_usd, gdp_growth, trade_openness,
      energy_imports_pct, energy_use_per_capita, nuclear_pct_electricity,
      inflation_cpi

    We add ISO3 using the same country name mapping, then keep only
    the columns needed by the model.

    Returns
    -------
    pd.DataFrame with columns: year, country_code, plus WB indicator columns.
    """
    if raw_path is None:
        raw_path = os.path.join(DATA_RAW, 'world_bank.csv')

    if not os.path.exists(raw_path):
        print(f"clean_world_bank: file not found at {raw_path}. Skipping.")
        return None

    print(f"Loading World Bank data: {raw_path}")
    df = pd.read_csv(raw_path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]

    # Standardize country codes
    df = standardize_owid_country_codes(df)
    df = df[df['iso3'].notna()].copy()
    df = df.rename(columns={'iso3': 'country_code'})

    # Ensure year is integer
    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        df = df[df['year'].notna()].copy()
        df['year'] = df['year'].astype(int)

    # Columns to keep (all optional — only include what exists)
    desired_cols = [
        'country_code', 'year',
        'gdp_usd', 'gdp_growth', 'trade_openness',
        'energy_imports_pct', 'energy_use_per_capita',
        'nuclear_pct_electricity', 'inflation_cpi',
        'fuel_exports_pct_merchandise', 'fuel_imports_pct_merchandise',
    ]
    keep = [c for c in desired_cols if c in df.columns]
    df_out = df[keep].copy()

    # Cast indicator columns to numeric
    indicator_cols = [c for c in df_out.columns if c not in ('country_code', 'year')]
    for col in indicator_cols:
        df_out[col] = pd.to_numeric(df_out[col], errors='coerce')

    # Drop duplicates
    df_out = df_out.drop_duplicates(subset=['country_code', 'year'])

    print(f"  World Bank cleaned: {len(df_out)} rows, "
          f"{df_out['country_code'].nunique()} countries, "
          f"years {df_out['year'].min()}-{df_out['year'].max()}")
    print(f"  Columns: {list(df_out.columns)}")

    return df_out


# ---------------------------------------------------------------------------
# Function 4: clean_cofer
# ---------------------------------------------------------------------------

def clean_cofer(raw_path: str = None) -> pd.DataFrame:
    """
    Load and clean IMF COFER reserve currency share data.

    Calls construct_reserve_share() from variables.py to parse the messy
    COFER CSV format into clean long-format currency/year/share rows,
    then maps currency codes -> ISO3 country codes via CURRENCY_TO_ISO3.

    Note: EUR maps to 'EMU' (Euro Monetary Union) rather than a single country.
    COFER covers 1999-present; CNY reported separately from 2016.

    Returns
    -------
    pd.DataFrame with columns: country_code, year, reserve_share, reserves_usd_bn
    """
    if raw_path is None:
        raw_path = os.path.join(DATA_RAW, 'imf_cofer.csv')

    if not os.path.exists(raw_path):
        print(f"clean_cofer: file not found at {raw_path}. Skipping.")
        return None

    print(f"Loading IMF COFER data: {raw_path}")

    df_raw = pd.read_csv(raw_path, low_memory=False, encoding='utf-8-sig')
    print(f"  COFER raw: {df_raw.shape}")

    # -----------------------------------------------------------------------
    # Currency name → 3-letter code
    # -----------------------------------------------------------------------
    FXR_TO_CODE = {
        'Claims in US dollar':              'USD',
        'Claims in Euro':                   'EUR',
        'Claims in Japanese yen':           'JPY',
        'Claims in Pound sterling':         'GBP',
        'Claims in Chinese yuan renminbi':  'CNY',
        'Claims in Swiss franc':            'CHF',
        'Claims in Canadian dollar':        'CAD',
        'Claims in Australian dollar':      'AUD',
    }

    # -----------------------------------------------------------------------
    # Filter: World, Annual, % Shares, Allocated reserves
    # -----------------------------------------------------------------------
    mask = (
        (df_raw['COUNTRY'] == 'World') &
        (df_raw['FREQUENCY'] == 'Annual') &
        (df_raw['TYPE_OF_TRANSFORMATION'] == 'Shares') &
        (df_raw['INDICATOR'] == 'Allocated foreign exchange reserves') &
        (df_raw['FXR_CURRENCY'].isin(FXR_TO_CODE.keys()))
    )
    df_shares = df_raw[mask].copy()
    print(f"  Share rows filtered: {len(df_shares)}")

    if df_shares.empty:
        print("  clean_cofer: no matching rows found. Skipping.")
        return None

    # -----------------------------------------------------------------------
    # Identify annual year columns (YYYY only, not YYYY-QN)
    # -----------------------------------------------------------------------
    import re
    year_cols = [c for c in df_raw.columns if re.fullmatch(r'\d{4}', str(c))]

    # Melt to long format
    id_col = 'FXR_CURRENCY'
    df_long = df_shares[[id_col] + year_cols].melt(
        id_vars=id_col, var_name='year', value_name='reserve_share'
    )
    df_long['year'] = df_long['year'].astype(int)
    df_long['reserve_share'] = pd.to_numeric(df_long['reserve_share'], errors='coerce')

    # Drop missing share values
    df_long = df_long[df_long['reserve_share'].notna()].copy()

    # Map FXR_CURRENCY → currency code → ISO3
    df_long['currency_code'] = df_long[id_col].map(FXR_TO_CODE)
    df_long['country_code'] = df_long['currency_code'].map(CURRENCY_TO_ISO3).fillna(
        df_long['currency_code']
    )

    # -----------------------------------------------------------------------
    # Also pull total allocated reserves nominal value (for reserves_usd_bn)
    # -----------------------------------------------------------------------
    mask_total = (
        (df_raw['COUNTRY'] == 'World') &
        (df_raw['FREQUENCY'] == 'Annual') &
        (df_raw['TYPE_OF_TRANSFORMATION'] == 'Nominal value') &
        (df_raw['INDICATOR'] == 'Allocated foreign exchange reserves') &
        (df_raw['FXR_CURRENCY'] == 'Claims in All currencies')
    )
    df_total = df_raw[mask_total]
    if not df_total.empty:
        total_long = df_total[year_cols].T.reset_index()
        total_long.columns = ['year', 'total_allocated']
        total_long['year'] = total_long['year'].astype(int)
        total_long['total_allocated'] = pd.to_numeric(total_long['total_allocated'], errors='coerce')
        # Scale column says 'Units' (millions USD based on IMF COFER methodology)
        total_long['reserves_usd_bn'] = total_long['total_allocated'] / 1e3
        df_long = df_long.merge(total_long[['year', 'reserves_usd_bn']], on='year', how='left')
    else:
        df_long['reserves_usd_bn'] = float('nan')

    # Drop duplicates
    df_long = df_long.drop_duplicates(subset=['country_code', 'year'])

    print(f"  COFER cleaned: {len(df_long)} rows")
    print(f"  Reserve currency entities: {sorted(df_long['country_code'].unique())}")
    print(f"  Years: {df_long['year'].min()}-{df_long['year'].max()}")

    return df_long[['country_code', 'year', 'reserve_share', 'reserves_usd_bn']]


# ---------------------------------------------------------------------------
# Function 5: clean_chinn_ito
# ---------------------------------------------------------------------------

def clean_chinn_ito(raw_path: str = None) -> pd.DataFrame:
    """
    Load and clean Chinn-Ito Capital Account Openness (KAOPEN) index.

    File pulled by data_pull.py has columns:
      cn, ccode, country_name, year, kaopen, ka_open

    where 'cn' is the ISO2/abbreviated country code used by the Chinn-Ito
    dataset (e.g., 'CHN', 'IND') — this is actually the ISO3 code in most
    versions of the dataset. We use 'cn' directly as country_code when it
    looks like a 3-letter ISO code, otherwise fall back to country_name mapping.

    Returns
    -------
    pd.DataFrame with columns: country_code, year, kaopen
    """
    if raw_path is None:
        raw_path = os.path.join(DATA_RAW, 'chinn_ito_kaopen.csv')

    if not os.path.exists(raw_path):
        print(f"clean_chinn_ito: file not found at {raw_path}. Skipping.")
        return None

    print(f"Loading Chinn-Ito data: {raw_path}")
    df = pd.read_csv(raw_path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]

    # The 'cn' column in Chinn-Ito is a 3-letter ISO-like code (e.g., CHN, USA).
    # Confirm it looks like ISO3 (3 uppercase letters); fall back to country_name.
    if 'cn' in df.columns:
        sample_cn = df['cn'].dropna().head(20).tolist()
        looks_iso3 = all(
            isinstance(v, str) and len(v) == 3 and v.isalpha()
            for v in sample_cn
        )
        if looks_iso3:
            df['country_code'] = df['cn'].str.upper().str.strip()
        else:
            # Fall back to country_name mapping
            if 'country_name' in df.columns:
                df['country_code'] = df['country_name'].map(COUNTRY_NAME_TO_ISO3)
            else:
                df['country_code'] = df['cn']
    elif 'country_name' in df.columns:
        df['country_code'] = df['country_name'].map(COUNTRY_NAME_TO_ISO3)
    else:
        print("  clean_chinn_ito: cannot identify country code column. Skipping.")
        return None

    # Ensure year is integer
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df = df[df['year'].notna()].copy()
    df['year'] = df['year'].astype(int)

    # Keep kaopen; ka_open is an alternative binary version — we use kaopen
    keep_cols = ['country_code', 'year', 'kaopen']
    optional_extra = ['ka_open']
    for col in optional_extra:
        if col in df.columns:
            keep_cols.append(col)

    available = [c for c in keep_cols if c in df.columns]
    df_out = df[available].copy()

    df_out['kaopen'] = pd.to_numeric(df_out['kaopen'], errors='coerce')
    df_out = df_out[df_out['country_code'].notna()]
    df_out = df_out.drop_duplicates(subset=['country_code', 'year'])

    print(f"  Chinn-Ito cleaned: {len(df_out)} rows, "
          f"{df_out['country_code'].nunique()} countries, "
          f"years {df_out['year'].min()}-{df_out['year'].max()}")

    return df_out


# ---------------------------------------------------------------------------
# Function 6: clean_governance
# ---------------------------------------------------------------------------

def clean_governance(raw_path: str = None) -> pd.DataFrame:
    """
    Load and clean World Bank Governance Indicators (WGI).

    File pulled by pull_governance_indicators() is already in wide format
    with columns: country_code, year, political_stability, rule_of_law,
    gov_effectiveness, regulatory_quality.

    The country_code column already contains ISO3 codes (direct from WB API).

    Returns
    -------
    pd.DataFrame with columns: country_code, year, plus governance columns.
    """
    if raw_path is None:
        raw_path = os.path.join(DATA_RAW, 'governance_indicators.csv')

    if not os.path.exists(raw_path):
        print(f"clean_governance: file not found at {raw_path}. Skipping.")
        return None

    print(f"Loading governance indicators: {raw_path}")
    df = pd.read_csv(raw_path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]

    # World Bank API returns ISO3 directly in 'country_code'
    if 'country_code' not in df.columns:
        print("  clean_governance: missing 'country_code' column. Skipping.")
        return None

    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df = df[df['year'].notna()].copy()
    df['year'] = df['year'].astype(int)

    gov_cols = ['political_stability', 'rule_of_law', 'gov_effectiveness', 'regulatory_quality']
    keep = ['country_code', 'year'] + [c for c in gov_cols if c in df.columns]
    df_out = df[keep].copy()

    for col in gov_cols:
        if col in df_out.columns:
            df_out[col] = pd.to_numeric(df_out[col], errors='coerce')

    # Remove empty/aggregate country codes (World Bank API sometimes returns blanks)
    df_out = df_out[df_out['country_code'].notna() & (df_out['country_code'].str.strip() != '')]
    df_out = df_out.drop_duplicates(subset=['country_code', 'year'])

    print(f"  Governance cleaned: {len(df_out)} rows, "
          f"{df_out['country_code'].nunique()} countries, "
          f"years {df_out['year'].min()}-{df_out['year'].max()}")

    return df_out


# ---------------------------------------------------------------------------
# Function 7: merge_panel
# ---------------------------------------------------------------------------

def merge_panel(
    owid_df: pd.DataFrame,
    wb_df: pd.DataFrame = None,
    cofer_df: pd.DataFrame = None,
    chinn_ito_df: pd.DataFrame = None,
    governance_df: pd.DataFrame = None,
) -> pd.DataFrame:
    """
    Merge all cleaned sources into one panel DataFrame.

    Merge strategy:
      1. OWID energy as base (widest country/year coverage)
      2. Left-merge World Bank on ['country_code', 'year']
      3. Left-merge COFER on ['country_code', 'year']
         (only matches reserve currency issuers: USA, EMU, JPN, GBR, CHN, CHE)
      4. Left-merge Chinn-Ito on ['country_code', 'year'] if provided
      5. Left-merge governance indicators on ['country_code', 'year'] if provided

    All merges are left joins to preserve the OWID country/year universe.
    COFER reserve_share will be NaN for non-reserve-currency countries (expected).

    Parameters
    ----------
    owid_df       : cleaned OWID energy DataFrame (required — the base)
    wb_df         : cleaned World Bank DataFrame (optional)
    cofer_df      : cleaned COFER reserve share DataFrame (optional)
    chinn_ito_df  : cleaned Chinn-Ito KAOPEN DataFrame (optional)
    governance_df : cleaned governance indicators DataFrame (optional)

    Returns
    -------
    pd.DataFrame : merged panel with has_reserve_share boolean column added.
    """
    if owid_df is None or len(owid_df) == 0:
        raise ValueError("merge_panel: owid_df is required and cannot be empty.")

    panel = owid_df.copy()
    print(f"\nMerge panel — base (OWID energy): {len(panel)} rows, "
          f"{panel['country_code'].nunique()} countries")

    # --- World Bank ---
    if wb_df is not None and len(wb_df) > 0:
        # Avoid column collisions on non-key columns
        wb_cols = ['country_code', 'year'] + [
            c for c in wb_df.columns
            if c not in ('country_code', 'year') and c not in panel.columns
        ]
        panel = panel.merge(wb_df[wb_cols], on=['country_code', 'year'], how='left')
        print(f"  After World Bank merge: {len(panel)} rows")

    # --- COFER reserve shares ---
    if cofer_df is not None and len(cofer_df) > 0:
        cofer_cols = ['country_code', 'year', 'reserve_share', 'reserves_usd_bn']
        cofer_cols = [c for c in cofer_cols if c in cofer_df.columns]
        panel = panel.merge(cofer_df[cofer_cols], on=['country_code', 'year'], how='left')
        print(f"  After COFER merge: {len(panel)} rows "
              f"({panel['reserve_share'].notna().sum()} rows with reserve_share data)")

    # --- Chinn-Ito KAOPEN ---
    if chinn_ito_df is not None and len(chinn_ito_df) > 0:
        # Rename 'cn' -> 'country_code' if needed (already done in clean_chinn_ito)
        ci_cols = ['country_code', 'year'] + [
            c for c in chinn_ito_df.columns
            if c not in ('country_code', 'year') and c not in panel.columns
        ]
        ci_cols = [c for c in ci_cols if c in chinn_ito_df.columns]
        panel = panel.merge(chinn_ito_df[ci_cols], on=['country_code', 'year'], how='left')
        print(f"  After Chinn-Ito merge: {len(panel)} rows")

    # --- Governance indicators ---
    if governance_df is not None and len(governance_df) > 0:
        gov_cols = ['country_code', 'year'] + [
            c for c in governance_df.columns
            if c not in ('country_code', 'year') and c not in panel.columns
        ]
        gov_cols = [c for c in gov_cols if c in governance_df.columns]
        panel = panel.merge(governance_df[gov_cols], on=['country_code', 'year'], how='left')
        print(f"  After governance merge: {len(panel)} rows")

    # --- Add has_reserve_share flag ---
    if 'reserve_share' in panel.columns:
        panel['has_reserve_share'] = panel['reserve_share'].notna()
    else:
        panel['has_reserve_share'] = False

    # --- Diagnostics ---
    key_vars = [
        'net_energy_position', 'gdp_share', 'trade_openness',
        'reserve_share', 'kaopen', 'inflation_cpi',
    ]
    print(f"\n=== MERGE DIAGNOSTICS ===")
    print(f"  Total rows       : {len(panel)}")
    print(f"  Unique countries : {panel['country_code'].nunique()}")
    year_min = panel['year'].min()
    year_max = panel['year'].max()
    print(f"  Year range       : {year_min}-{year_max}")
    if 'has_reserve_share' in panel.columns:
        n_rs = panel['has_reserve_share'].sum()
        print(f"  Rows with reserve_share data : {n_rs}")
    available_key = [v for v in key_vars if v in panel.columns]
    if available_key:
        n_complete = panel[available_key].notna().all(axis=1).sum()
        print(f"  Rows with all key vars populated ({available_key}): {n_complete}")

    return panel


# ---------------------------------------------------------------------------
# Function 8: run_full_pipeline
# ---------------------------------------------------------------------------

def run_full_pipeline() -> pd.DataFrame:
    """
    Run complete cleaning pipeline.
    Returns model-ready panel DataFrame.
    Saves to data/processed/panel_model_ready.csv

    Steps:
      1. Load and clean each raw source (skips gracefully if file missing)
      2. Merge into single panel
      3. Construct derived variables via variables.py functions
      4. Save to data/processed/panel_model_ready.csv
      5. Print coverage summary
    """
    print("=" * 60)
    print("CARBY-THO CLEAN PIPELINE")
    print("=" * 60)

    # Ensure output directory exists
    os.makedirs(DATA_PROCESSED, exist_ok=True)
    os.makedirs(DATA_RAW, exist_ok=True)

    # -----------------------------------------------------------------------
    # Step 1: Load and clean each source
    # -----------------------------------------------------------------------

    print("\n[1/4] Loading and cleaning raw data sources...")

    owid_df = None
    try:
        owid_df = clean_owid_energy()
    except Exception as e:
        print(f"  clean_owid_energy() failed: {e}")

    wb_df = None
    try:
        wb_df = clean_world_bank()
    except Exception as e:
        print(f"  clean_world_bank() failed: {e}")

    cofer_df = None
    try:
        cofer_df = clean_cofer()
    except Exception as e:
        print(f"  clean_cofer() failed: {e}")

    chinn_ito_df = None
    try:
        chinn_ito_df = clean_chinn_ito()
    except Exception as e:
        print(f"  clean_chinn_ito() failed: {e}")

    governance_df = None
    try:
        governance_df = clean_governance()
    except Exception as e:
        print(f"  clean_governance() failed: {e}")

    # -----------------------------------------------------------------------
    # Step 2: Merge
    # -----------------------------------------------------------------------

    print("\n[2/4] Merging sources into panel...")

    if owid_df is None:
        print("  ERROR: OWID energy data is the base layer and is missing.")
        print("  Run: python src/data_pull.py  (or pull_owid_energy())")
        print("  Cannot build panel without base layer. Aborting.")
        return None

    panel = merge_panel(
        owid_df=owid_df,
        wb_df=wb_df,
        cofer_df=cofer_df,
        chinn_ito_df=chinn_ito_df,
        governance_df=governance_df,
    )

    # -----------------------------------------------------------------------
    # Step 3: Construct derived variables
    # -----------------------------------------------------------------------

    print("\n[3/4] Constructing derived variables...")

    try:
        from variables import (
            construct_net_energy_position,
            construct_energy_dominance_weighted,
            construct_lagged_variables,
        )

        from variables import construct_gdp_share, construct_energy_export_share
        construct_gdp_share_fn = construct_gdp_share

    except ImportError as e:
        print(f"  Warning: could not import from variables.py: {e}")
        print("  Skipping variable construction — panel will be merged-only.")
        _save_and_summarize(panel)
        return panel

    # Net Energy Position
    try:
        panel = construct_net_energy_position(panel)
        print("  net_energy_position computed.")
    except Exception as e:
        print(f"  construct_net_energy_position() failed: {e}")

    # GDP Share
    try:
        panel = construct_gdp_share_fn(panel)
        print("  gdp_share computed.")
    except Exception as e:
        print(f"  construct_gdp_share() failed: {e}")

    # Energy Dominance Weighted
    try:
        panel = construct_energy_dominance_weighted(panel)
        print("  energy_dominance_weighted computed.")
    except Exception as e:
        print(f"  construct_energy_dominance_weighted() failed: {e}")

    # Energy Export Leverage (robustness check)
    try:
        panel = construct_energy_export_share(panel)
        print("  export_leverage computed.")
    except Exception as e:
        print(f"  construct_energy_export_share() failed: {e}")

    # Lagged variables for net_energy_position at 10yr and 15yr
    if 'net_energy_position' in panel.columns:
        try:
            panel = construct_lagged_variables(panel, 'net_energy_position', lags=[10, 15])
            print("  net_energy_position_lag10 and _lag15 computed.")
        except Exception as e:
            print(f"  construct_lagged_variables() failed: {e}")

    # -----------------------------------------------------------------------
    # Step 4: Save
    # -----------------------------------------------------------------------

    _save_and_summarize(panel)
    return panel


def _save_and_summarize(panel: pd.DataFrame) -> None:
    """Save panel to CSV and print final coverage summary."""
    print("\n[4/4] Saving and summarizing...")

    out_path = os.path.join(DATA_PROCESSED, 'panel_model_ready.csv')
    panel.to_csv(out_path, index=False)
    print(f"  Saved: {out_path}")
    print(f"  Shape: {panel.shape}")

    # Coverage summary
    key_vars = [
        'net_energy_position', 'energy_dominance_weighted',
        'gdp_share', 'reserve_share',
        'trade_openness', 'inflation_cpi',
        'kaopen', 'net_energy_position_lag10', 'net_energy_position_lag15',
    ]
    present = [v for v in key_vars if v in panel.columns]

    print("\n  Variable coverage (non-null rows):")
    for var in present:
        n = panel[var].notna().sum()
        pct = 100 * n / len(panel)
        print(f"    {var:<35}: {n:>6} rows ({pct:.1f}%)")

    # Focal country check
    print("\n  Focal country year ranges:")
    focal_iso = ['CHN', 'IND', 'RUS', 'JPN', 'USA', 'DEU', 'GBR']
    for iso in focal_iso:
        sub = panel[panel['country_code'] == iso]
        if len(sub) > 0:
            nep_ok = sub['net_energy_position'].notna().sum() if 'net_energy_position' in sub.columns else 0
            print(f"    {iso}: {len(sub)} obs "
                  f"({sub['year'].min()}-{sub['year'].max()}), "
                  f"NEP non-null: {nep_ok}")
        else:
            print(f"    {iso}: NO DATA")

    print("\nPipeline complete.")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    df = run_full_pipeline()
