"""
data_pull.py
Functions for pulling each data source.
Run this first before any notebooks.
"""

import requests
import pandas as pd
import wbdata
import json
import os
from datetime import datetime

DATA_RAW = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')


def pull_world_bank(indicators: dict, start_year: int = 1960, end_year: int = 2024) -> pd.DataFrame:
    """
    Pull World Bank WDI data for given indicators.
    
    indicators = {
        'NY.GDP.MKTP.CD': 'gdp_usd',
        'NE.TRD.GNFS.ZS': 'trade_openness',
        'EG.USE.PCAP.KG.OE': 'energy_use_per_capita',
        'EG.IMP.CONS.ZS': 'energy_imports_pct',
        'EG.ELC.NUCL.ZS': 'nuclear_pct_electricity',
    }
    """
    date_range = (datetime(start_year, 1, 1), datetime(end_year, 12, 31))
    df = wbdata.get_dataframe(indicators, date=date_range)
    df = df.reset_index()
    df.columns = ['country', 'date'] + list(indicators.values())
    df['year'] = pd.to_datetime(df['date']).dt.year
    df = df.drop(columns=['date'])
    
    path = os.path.join(DATA_RAW, 'world_bank.csv')
    df.to_csv(path, index=False)
    print(f"World Bank data saved: {len(df)} rows → {path}")
    return df


def pull_imf_cofer() -> pd.DataFrame:
    """
    Pull IMF COFER data on reserve currency composition.
    Returns annual data from 1999 onward.

    The direct CSV URL now returns HTML (IMF changed their download system).
    Use the IMF Data API (SDMX-JSON) as primary source.
    Manual fallback: https://data.imf.org/regular.aspx?key=41175
      → Download → CSV → save as data/raw/imf_cofer.csv

    API returns currency-level allocated reserves in USD millions.
    We pivot to wide format matching the original COFER CSV structure
    so construct_reserve_share() in variables.py can parse it.
    """
    # IMF SDMX-JSON API for COFER
    # Currencies: USD=US, EUR=U2, JPY=JP, GBP=GB, CNY=CN, CHF=CH
    currency_areas = {
        'USD': '111',  # United States
        'EUR': '163',  # Euro area
        'GBP': '112',  # United Kingdom
        'JPY': '158',  # Japan
        'CNY': '924',  # China
        'CHF': '146',  # Switzerland
    }
    results = []
    base = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/COFER/A"
    for currency, area_code in currency_areas.items():
        url = f"{base}.{area_code}..RAFA_USD?startPeriod=1999&endPeriod=2025"
        try:
            r = requests.get(url, timeout=20)
            data = r.json()
            series = data.get('CompactData', {}).get('DataSet', {}).get('Series', {})
            if isinstance(series, list):
                series = series[0] if series else {}
            obs_list = series.get('Obs', [])
            if isinstance(obs_list, dict):
                obs_list = [obs_list]
            for obs in obs_list:
                val = obs.get('@OBS_VALUE')
                period = obs.get('@TIME_PERIOD')
                if val and period:
                    results.append({
                        'currency': currency,
                        'year': int(str(period)[:4]),
                        'value_usd_bn': float(val) / 1000,
                    })
        except Exception as e:
            print(f"  COFER API failed for {currency}: {e}")

    if not results:
        print("IMF COFER API unavailable.")
        print("Manual download: https://data.imf.org/regular.aspx?key=41175")
        print("  → Export → CSV → save as data/raw/imf_cofer.csv")
        return None

    df = pd.DataFrame(results)

    # Compute reserve shares from totals
    totals = df.groupby('year')['value_usd_bn'].sum().reset_index()
    totals.columns = ['year', 'total_allocated']
    df = df.merge(totals, on='year')
    df['reserve_share'] = df['value_usd_bn'] / df['total_allocated']
    df = df.rename(columns={'currency': 'country_code'})

    path = os.path.join(DATA_RAW, 'imf_cofer.csv')
    df.to_csv(path, index=False)
    print(f"IMF COFER data saved: {len(df)} rows → {path}")
    print(df[df['year'] == df['year'].max()][['country_code', 'reserve_share']].to_string(index=False))
    return df


def pull_owid_energy() -> pd.DataFrame:
    """
    Our World in Data — Energy dataset.
    Incorporates Energy Institute Statistical Review of World Energy (formerly BP).
    Clean, panel format, directly downloadable. No manual steps required.
    
    Coverage: 1900-present, ~200 countries
    Key columns: primary_energy_consumption, fossil_fuel_consumption,
                 coal_production, oil_production, gas_production,
                 nuclear_electricity, renewables_electricity,
                 energy_imports (where available)
    
    Source: https://github.com/owid/energy-data
    Codebook: https://github.com/owid/energy-data/blob/master/owid-energy-codebook.csv
    """
    url = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    
    try:
        df = pd.read_csv(url)
        path = os.path.join(DATA_RAW, 'owid_energy.csv')
        df.to_csv(path, index=False)
        print(f"OWID energy data saved: {len(df)} rows, {len(df.columns)} columns → {path}")
        print(f"Countries: {df['country'].nunique()}, Years: {df['year'].min()}-{df['year'].max()}")
        return df
    except Exception as e:
        print(f"OWID energy pull failed: {e}")
        print("Manual fallback: https://github.com/owid/energy-data")
        return None


def pull_eu_ets() -> pd.DataFrame:
    """
    EU ETS data from EEA via datahub.io.
    Contains verified emissions, allocations, and compliance data by country/sector.
    Coverage: 2005-present.
    
    Note: For carbon PRICE data (EUA spot price history), use pull_carbon_prices().
    This dataset covers the structural/compliance dimension of the ETS.
    """
    url = "https://datahub.io/core/eu-emissions-trading-system/r/eu-ets.csv"
    
    try:
        df = pd.read_csv(url)
        path = os.path.join(DATA_RAW, 'eu_ets_compliance.csv')
        df.to_csv(path, index=False)
        print(f"EU ETS compliance data saved: {len(df)} rows → {path}")
        print(f"Columns: {list(df.columns)}")
        return df
    except Exception as e:
        print(f"EU ETS pull failed: {e}")
        print("Manual fallback: https://www.eea.europa.eu/en/datahub/datahubitem-view/98f04097-26de-4fca-86c4-63834818c0c0")
        return None


def pull_owid_co2() -> pd.DataFrame:
    """
    OWID CO2 and greenhouse gas emissions dataset.
    Contains CO2 emissions by country, sector, and fuel type.
    Used to construct carbon intensity measures and emission trends.
    
    Source: https://github.com/owid/co2-data
    """
    url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    
    try:
        df = pd.read_csv(url)
        path = os.path.join(DATA_RAW, 'owid_co2.csv')
        df.to_csv(path, index=False)
        print(f"OWID CO2 data saved: {len(df)} rows, {df['country'].nunique()} countries → {path}")
        return df
    except Exception as e:
        print(f"OWID CO2 pull failed: {e}")
        return None


def pull_chinn_ito() -> pd.DataFrame:
    """
    Chinn-Ito Capital Account Openness Index (KAOPEN).
    Measures degree of capital account openness for 182 countries.
    Critical control: China/India capital controls suppress RMB/INR
    internationalisation independent of energy position.

    Coverage: 1970-2023
    Source: https://web.pdx.edu/~ito/Chinn-Ito_website.htm
    """
    url = "https://web.pdx.edu/~ito/kaopen_2023.xls"
    try:
        import io
        r = requests.get(url, timeout=20)
        df = pd.read_excel(io.BytesIO(r.content))
        df.columns = ['cn', 'ccode', 'country_name', 'year', 'kaopen', 'ka_open']
        path = os.path.join(DATA_RAW, 'chinn_ito_kaopen.csv')
        df.to_csv(path, index=False)
        print(f"Chinn-Ito saved: {len(df)} rows, years {df.year.min()}-{df.year.max()} → {path}")
        return df
    except Exception as e:
        print(f"Chinn-Ito pull failed: {e}")
        return None


def pull_shambaugh_fx_regimes() -> pd.DataFrame:
    """
    Shambaugh Exchange Rate Regime Classification.
    Binary peg classification for 180 countries.
    Controls for whether a currency CAN serve as reserve currency
    (pegged currencies generally cannot).

    Coverage: 1960-2014
    Source: Shambaugh (2004) via NBER
    """
    url = "https://data.nber.org/international-finance/shambaugh-exchange-rate-regimes.dta"
    try:
        import io
        r = requests.get(url, timeout=15)
        df = pd.read_stata(io.BytesIO(r.content))
        path = os.path.join(DATA_RAW, 'shambaugh_fx_regimes.csv')
        df.to_csv(path, index=False)
        print(f"Shambaugh FX regimes saved: {df.shape} → {path}")
        return df
    except Exception as e:
        print(f"Shambaugh pull failed: {e}")
        return None


def pull_jst_macrohistory() -> pd.DataFrame:
    """
    Jorda-Schularick-Taylor Macrohistory Database.
    Long-run macroeconomic and financial data for 18 advanced economies.
    Used for historical validation of coal/pound and oil/dollar transitions.

    Coverage: 1870-2020, 18 countries (UK, USA, Japan, Germany, France etc.)
    Note: Does NOT include China, India, Russia — used for historical cases only.
    Source: https://www.macrohistory.net/database/
    """
    url = "https://www.macrohistory.net/app/download/9834512569/JSTdatasetR6.csv"
    try:
        import io
        r = requests.get(url, timeout=20)
        # The file is served as .csv but is actually an Excel workbook (PK header)
        if r.content[:4] == b'PK\x03\x04':
            df = pd.read_excel(io.BytesIO(r.content))
        else:
            df = pd.read_csv(io.BytesIO(r.content), encoding='latin-1')
        path = os.path.join(DATA_RAW, 'jst_macrohistory.csv')
        df.to_csv(path, index=False)
        print(f"JST Macrohistory saved: {df.shape}, years {df.year.min()}-{df.year.max()} → {path}")
        print(f"Countries: {sorted(df.country.unique())}")
        return df
    except Exception as e:
        print(f"JST pull failed: {e}")
        return None


def pull_financial_depth() -> pd.DataFrame:
    """
    World Bank financial market depth indicators for focal countries.
    Reserve holders need liquid, deep markets to park reserves.
    Controls for why Japan underperforms despite GDP size.

    Indicators:
    - Domestic credit to private sector (% GDP)
    - Stock market capitalisation (% GDP)

    Coverage: 1995-2024
    """
    indicators = {
        'FS.AST.PRVT.GD.ZS': 'domestic_credit_private_pct_gdp',
        'CM.MKT.LCAP.GD.ZS': 'stock_market_cap_pct_gdp',
    }
    results = []
    for code, name in indicators.items():
        url = (f"https://api.worldbank.org/v2/country/all/indicator/{code}"
               f"?format=json&per_page=2000&mrv=35")
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = r.json()
            if data[1]:
                for x in data[1]:
                    if x['value'] is not None:
                        results.append({
                            'country_code': x['countryiso3code'],
                            'country': x['country']['value'],
                            'year': int(x['date']),
                            'indicator': name,
                            'value': x['value']
                        })
    df = pd.DataFrame(results)
    path = os.path.join(DATA_RAW, 'financial_depth.csv')
    df.to_csv(path, index=False)
    print(f"Financial depth saved: {len(df)} rows → {path}")
    return df


def pull_imf_ifs(series_codes: list) -> pd.DataFrame:
    """
    Pull IMF International Financial Statistics.
    Used for inflation data.

    series_codes examples:
    - 'PCPI_IX' : Consumer Price Index
    - 'ENDA_XDC_USD_RATE' : Exchange rate
    """
    base_url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/A."
    results = []

    for code in series_codes:
        url = f"{base_url}...{code}?startPeriod=1960&endPeriod=2023"
        try:
            r = requests.get(url, timeout=30)
            data = r.json()
            series = data['CompactData']['DataSet']['Series']
            if isinstance(series, dict):
                series = [series]
            for s in series:
                country = s.get('@REF_AREA', 'Unknown')
                obs = s.get('Obs', [])
                if isinstance(obs, dict):
                    obs = [obs]
                for o in obs:
                    results.append({
                        'country_code': country,
                        'year': int(o.get('@TIME_PERIOD', 0)),
                        'indicator': code,
                        'value': float(o.get('@OBS_VALUE', 0))
                    })
        except Exception as e:
            print(f"IMF IFS pull failed for {code}: {e}")

    df = pd.DataFrame(results)
    path = os.path.join(DATA_RAW, 'imf_ifs.csv')
    df.to_csv(path, index=False)
    print(f"IMF IFS data saved: {len(df)} rows → {path}")
    return df


def pull_governance_indicators() -> pd.DataFrame:
    """
    World Bank Worldwide Governance Indicators (WGI).
    Used in Thorium Monetary Potential Index.

    Four indicators:
    - Political stability (PV.EST)
    - Rule of law (RL.EST)
    - Government effectiveness (GE.EST)
    - Regulatory quality (RQ.EST)

    Coverage: 1996-2023, ~200 countries (paginated)
    """
    gov_indicators = {
        'PV.EST': 'political_stability',
        'RL.EST': 'rule_of_law',
        'GE.EST': 'gov_effectiveness',
        'RQ.EST': 'regulatory_quality',
    }
    results = []
    for code, name in gov_indicators.items():
        for page in [1, 2]:
            url = (f"https://api.worldbank.org/v2/country/all/indicator/{code}"
                   f"?format=json&per_page=5000&date=1996:2024&page={page}")
            try:
                r = requests.get(url, timeout=20)
                data = r.json()
                if data[1]:
                    for x in data[1]:
                        if x['value'] is not None:
                            results.append({
                                'country_code': x['countryiso3code'],
                                'year': int(x['date']),
                                'indicator': name,
                                'value': x['value']
                            })
                if data[0]['pages'] <= page:
                    break
            except Exception as e:
                print(f"Governance p{page} {name}: {e}")

    df = pd.DataFrame(results)
    df_wide = df.pivot_table(
        index=['country_code', 'year'],
        columns='indicator',
        values='value'
    ).reset_index()
    df_wide.columns.name = None

    path = os.path.join(DATA_RAW, 'governance_indicators.csv')
    df_wide.to_csv(path, index=False)
    print(f"Governance indicators saved: {df_wide.shape} → {path}")
    return df_wide


def pull_thorium_reserves() -> pd.DataFrame:
    """
    Thorium reserve data from USGS Mineral Commodity Summaries 2024.
    Source: https://pubs.usgs.gov/periodicals/mcs2024/mcs2024-thorium.pdf

    Point estimates — no API. Data extracted from official PDF.
    Updated every ~2 years. World total: ~6,200,000 metric tonnes.

    Note: India's Atomic Minerals Directorate (AMD) reports ~10.7M mt
    total resources vs USGS ~1.0M mt economically recoverable reserves.
    USGS figure used for international comparability. AMD figure noted.
    """
    data = [
        {'country_code': 'IND', 'country': 'India',
         'reserves_mt': 1_000_000, 'world_share': 0.161,
         'note': 'AMD estimates 10.7M mt total resources'},
        {'country_code': 'BRA', 'country': 'Brazil',
         'reserves_mt': 830_000,  'world_share': 0.134},
        {'country_code': 'AUS', 'country': 'Australia',
         'reserves_mt': 780_000,  'world_share': 0.126},
        {'country_code': 'USA', 'country': 'United States',
         'reserves_mt': 670_000,  'world_share': 0.108},
        {'country_code': 'EGY', 'country': 'Egypt',
         'reserves_mt': 380_000,  'world_share': 0.061},
        {'country_code': 'TUR', 'country': 'Turkey',
         'reserves_mt': 344_000,  'world_share': 0.056},
        {'country_code': 'VEN', 'country': 'Venezuela',
         'reserves_mt': 300_000,  'world_share': 0.048},
        {'country_code': 'CAN', 'country': 'Canada',
         'reserves_mt': 172_000,  'world_share': 0.028},
        {'country_code': 'RUS', 'country': 'Russia',
         'reserves_mt': 155_000,  'world_share': 0.025},
        {'country_code': 'ZAF', 'country': 'South Africa',
         'reserves_mt': 148_000,  'world_share': 0.024},
        {'country_code': 'CHN', 'country': 'China',
         'reserves_mt': 131_000,  'world_share': 0.021},
        {'country_code': 'NOR', 'country': 'Norway',
         'reserves_mt': 132_000,  'world_share': 0.021},
        {'country_code': 'DNK', 'country': 'Greenland/Denmark',
         'reserves_mt': 117_000,  'world_share': 0.019},
    ]
    df = pd.DataFrame(data)
    df['world_total_mt'] = 6_200_000
    df['source'] = 'USGS MCS 2024'
    df['source_url'] = 'https://pubs.usgs.gov/periodicals/mcs2024/mcs2024-thorium.pdf'

    path = os.path.join(DATA_RAW, 'thorium_reserves_usgs2024.csv')
    df.to_csv(path, index=False)
    print(f"Thorium reserves saved: {len(df)} countries → {path}")
    return df


def pull_bis_fx_turnover() -> pd.DataFrame:
    """
    BIS Triennial Central Bank Survey — OTC FX Turnover by Currency.
    Survey years: 2010, 2013, 2016, 2019, 2022.

    Used as reserve currency proxy for CAN/AUS/BRA — countries not
    covered in COFER but whose currencies serve nontraditional reserve roles.

    Key finding:
    - AUD: 7.6%-8.6%-6.9%-6.8%-6.4% — nontraditional reserve currency
    - CAD: 5.3%-4.6%-5.1%-5.0%-6.2% — nontraditional reserve currency
    - BRL: 0.7%-1.1%-1.0%-1.1%-0.9% — NOT a reserve currency

    AUD and CAD confirmed as nontraditional reserve currencies per
    Arslanalp, Eichengreen & Simpson-Bell (2022).
    BRL blocked by capital controls (Chinn-Ito = -1.254).

    Source: BIS Triennial Survey 2022, Sheet 4
    https://www.bis.org/statistics/rpfx22_fx_tables.xlsx
    """
    fx_data = {
        'USD': {2010: 84.9, 2013: 87.0, 2016: 87.6, 2019: 88.3, 2022: 88.4},
        'EUR': {2010: 39.0, 2013: 33.4, 2016: 31.4, 2019: 32.3, 2022: 30.5},
        'JPY': {2010: 19.0, 2013: 23.0, 2016: 21.6, 2019: 16.8, 2022: 16.7},
        'GBP': {2010: 12.9, 2013: 11.8, 2016: 12.8, 2019: 12.8, 2022: 12.9},
        'CNY': {2010: 0.9,  2013: 2.2,  2016: 4.0,  2019: 4.3,  2022: 7.0},
        'AUS': {2010: 7.6,  2013: 8.6,  2016: 6.9,  2019: 6.8,  2022: 6.4},
        'CAN': {2010: 5.3,  2013: 4.6,  2016: 5.1,  2019: 5.0,  2022: 6.2},
        'CHF': {2010: 6.3,  2013: 5.2,  2016: 4.8,  2019: 5.0,  2022: 5.2},
        'BRA': {2010: 0.7,  2013: 1.1,  2016: 1.0,  2019: 1.1,  2022: 0.9},
        'IND': {2010: 0.9,  2013: 1.0,  2016: 1.1,  2019: 1.7,  2022: 1.6},
        'JPN': {2010: 19.0, 2013: 23.0, 2016: 21.6, 2019: 16.8, 2022: 16.7},
        'CHN': {2010: 0.9,  2013: 2.2,  2016: 4.0,  2019: 4.3,  2022: 7.0},
    }

    rows = []
    for iso, year_data in fx_data.items():
        for year, share in year_data.items():
            rows.append({
                'country_code': iso,
                'year': year,
                'fx_turnover_share_pct': share,
            })

    df = pd.DataFrame(rows)
    path = os.path.join(DATA_RAW, 'bis_fx_turnover.csv')
    df.to_csv(path, index=False)
    print(f"BIS FX turnover saved: {len(df)} rows → {path}")
    latest = df[df['year']==2022].sort_values('fx_turnover_share_pct', ascending=False)
    print(f"\nFX turnover share 2022:\n{latest.to_string(index=False)}")
    return df


def pull_bis_fx_turnover_expanded() -> pd.DataFrame:
    """
    BIS Triennial Central Bank Survey — OTC FX Turnover by Currency (EXPANDED).
    Full ~40 currency breakdown across all Triennial survey years: 2001-2022.

    This is the key N expansion: from 6 reserve currencies to 40+ currencies
    as the dependent variable (FX turnover share as proxy for currency
    internationalisation / reserve currency status).

    Data source: BIS Triennial Central Bank Survey results tables.
    - https://www.bis.org/statistics/rpfx22.htm (2022)
    - https://www.bis.org/publ/rpfx19.htm (2019)
    - https://www.bis.org/publ/rpfx16.htm (2016)
    - Earlier surveys: bis.org/publ/rpfx13.htm, rpfx10.htm, rpfx07.htm, etc.

    BIS reports shares summing to 200% (each FX transaction involves two
    currencies). We store the raw BIS share (out of 200%) in fx_share_pct_200
    and also provide fx_share_pct normalised to sum to 100%.

    Currency code -> ISO3 country code mapping provided for panel merge.
    EUR maps to EMU (Euro Monetary Union) consistent with COFER treatment.

    Returns DataFrame with columns:
        year, currency_code, country_code, fx_turnover_daily_bn, fx_share_pct
    """

    # -----------------------------------------------------------------------
    # Currency code -> ISO3 country code mapping
    # Consistent with clean.py CURRENCY_TO_ISO3 but expanded for all BIS currencies
    # -----------------------------------------------------------------------
    CURRENCY_TO_COUNTRY = {
        'USD': 'USA', 'EUR': 'EMU', 'JPY': 'JPN', 'GBP': 'GBR',
        'CNY': 'CHN', 'AUD': 'AUS', 'CAD': 'CAN', 'CHF': 'CHE',
        'HKD': 'HKG', 'SGD': 'SGP', 'SEK': 'SWE', 'KRW': 'KOR',
        'NOK': 'NOR', 'NZD': 'NZL', 'INR': 'IND', 'MXN': 'MEX',
        'TWD': 'TWN', 'ZAR': 'ZAF', 'BRL': 'BRA', 'DKK': 'DNK',
        'PLN': 'POL', 'THB': 'THA', 'ILS': 'ISR', 'IDR': 'IDN',
        'CZK': 'CZE', 'AED': 'ARE', 'TRY': 'TUR', 'HUF': 'HUN',
        'CLP': 'CHL', 'SAR': 'SAU', 'PHP': 'PHL', 'MYR': 'MYS',
        'COP': 'COL', 'RUB': 'RUS', 'RON': 'ROU', 'PEN': 'PER',
        'BHD': 'BHR', 'BGN': 'BGR',
    }

    # -----------------------------------------------------------------------
    # BIS Triennial Survey data: FX turnover share by currency (% of 200%)
    # Source: BIS Table 1 "Foreign exchange turnover by currency"
    #
    # Each dict maps currency_code -> share (out of 200%).
    # "Other" and residual currencies are excluded; only individually
    # reported currencies are included.
    #
    # Note: BIS did not report all currencies in early surveys.
    # Pre-2004 coverage is narrower (~20 currencies). Coverage expanded
    # from 2007 onward to ~40 currencies.
    # -----------------------------------------------------------------------

    # 2001 BIS Triennial (total daily turnover: $1,239 bn)
    # Source: BIS Triennial Survey 2001, Table E.3
    bis_2001 = {
        'USD': 89.9, 'EUR': 37.9, 'JPY': 23.5, 'GBP': 13.0,
        'CHF': 6.0, 'CAD': 4.5, 'AUD': 4.3, 'SEK': 2.5,
        'HKD': 2.2, 'NOK': 1.5, 'NZD': 0.6, 'MXN': 0.8,
        'SGD': 1.1, 'KRW': 0.8, 'ZAR': 0.9, 'DKK': 1.2,
        'INR': 0.2, 'BRL': 0.5, 'CNY': 0.0, 'PLN': 0.5,
        'THB': 0.2, 'TWD': 0.3, 'CZK': 0.2, 'HUF': 0.0,
        'IDR': 0.0, 'TRY': 0.0, 'CLP': 0.2, 'SAR': 0.2,
        'RUB': 0.3, 'ILS': 0.1, 'PHP': 0.0, 'MYR': 0.1,
    }

    # 2004 BIS Triennial (total daily turnover: $1,934 bn)
    # Source: BIS Triennial Survey 2004, Table E.3
    bis_2004 = {
        'USD': 88.0, 'EUR': 37.4, 'JPY': 20.8, 'GBP': 16.5,
        'CHF': 6.0, 'AUD': 6.0, 'CAD': 4.2, 'SEK': 2.2,
        'HKD': 1.8, 'NOK': 1.4, 'NZD': 1.1, 'MXN': 1.1,
        'SGD': 0.9, 'KRW': 1.1, 'ZAR': 0.7, 'DKK': 0.9,
        'INR': 0.3, 'BRL': 0.3, 'CNY': 0.1, 'PLN': 0.4,
        'THB': 0.2, 'TWD': 0.4, 'CZK': 0.2, 'HUF': 0.2,
        'IDR': 0.1, 'TRY': 0.1, 'CLP': 0.1, 'SAR': 0.1,
        'RUB': 0.6, 'ILS': 0.1, 'PHP': 0.0, 'MYR': 0.1,
    }

    # 2007 BIS Triennial (total daily turnover: $3,324 bn)
    # Source: BIS Triennial Survey 2007, Table E.4
    bis_2007 = {
        'USD': 85.6, 'EUR': 37.0, 'JPY': 17.2, 'GBP': 14.9,
        'CHF': 6.8, 'AUD': 6.6, 'CAD': 4.3, 'SEK': 2.7,
        'HKD': 2.7, 'NOK': 2.1, 'NZD': 1.9, 'MXN': 1.3,
        'SGD': 1.2, 'KRW': 1.2, 'ZAR': 0.9, 'DKK': 0.8,
        'INR': 0.7, 'BRL': 0.4, 'CNY': 0.5, 'PLN': 0.8,
        'THB': 0.2, 'TWD': 0.4, 'CZK': 0.2, 'HUF': 0.3,
        'IDR': 0.1, 'TRY': 0.2, 'CLP': 0.1, 'SAR': 0.1,
        'RUB': 0.7, 'ILS': 0.2, 'PHP': 0.1, 'MYR': 0.1,
        'COP': 0.0, 'RON': 0.0, 'PEN': 0.0,
    }

    # 2010 BIS Triennial (total daily turnover: $3,981 bn)
    # Source: BIS Triennial Survey 2010, Table 3
    bis_2010 = {
        'USD': 84.9, 'EUR': 39.0, 'JPY': 19.0, 'GBP': 12.9,
        'AUD': 7.6, 'CHF': 6.3, 'CAD': 5.3, 'HKD': 2.4,
        'SEK': 2.2, 'NZD': 1.6, 'KRW': 1.5, 'SGD': 1.4,
        'NOK': 1.3, 'MXN': 1.3, 'INR': 0.9, 'CNY': 0.9,
        'RUB': 0.9, 'ZAR': 0.7, 'TRY': 0.7, 'BRL': 0.7,
        'PLN': 0.8, 'TWD': 0.5, 'DKK': 0.6, 'THB': 0.2,
        'MYR': 0.3, 'IDR': 0.2, 'CZK': 0.2, 'HUF': 0.4,
        'ILS': 0.2, 'CLP': 0.2, 'PHP': 0.2, 'COP': 0.1,
        'SAR': 0.1, 'PEN': 0.1, 'RON': 0.1, 'AED': 0.1,
    }

    # 2013 BIS Triennial (total daily turnover: $5,345 bn)
    # Source: BIS Triennial Survey 2013, Table 1
    bis_2013 = {
        'USD': 87.0, 'EUR': 33.4, 'JPY': 23.0, 'GBP': 11.8,
        'AUD': 8.6, 'CHF': 5.2, 'CAD': 4.6, 'MXN': 2.5,
        'CNY': 2.2, 'NZD': 2.0, 'SEK': 1.8, 'RUB': 1.6,
        'HKD': 1.4, 'NOK': 1.4, 'SGD': 1.4, 'TRY': 1.3,
        'KRW': 1.2, 'ZAR': 1.1, 'BRL': 1.1, 'INR': 1.0,
        'DKK': 0.8, 'TWD': 0.5, 'PLN': 0.7, 'THB': 0.3,
        'MYR': 0.4, 'IDR': 0.2, 'CZK': 0.4, 'HUF': 0.4,
        'ILS': 0.3, 'CLP': 0.3, 'PHP': 0.1, 'COP': 0.1,
        'SAR': 0.2, 'PEN': 0.1, 'RON': 0.1, 'AED': 0.1,
        'BHD': 0.0, 'BGN': 0.0,
    }

    # 2016 BIS Triennial (total daily turnover: $5,067 bn)
    # Source: BIS Triennial Survey 2016, Table 1
    bis_2016 = {
        'USD': 87.6, 'EUR': 31.4, 'JPY': 21.6, 'GBP': 12.8,
        'AUD': 6.9, 'CAD': 5.1, 'CHF': 4.8, 'CNY': 4.0,
        'SEK': 2.2, 'NZD': 2.1, 'MXN': 1.9, 'KRW': 1.7,
        'SGD': 1.8, 'NOK': 1.7, 'TRY': 1.4, 'INR': 1.1,
        'RUB': 1.1, 'HKD': 1.7, 'BRL': 1.0, 'ZAR': 1.0,
        'DKK': 0.8, 'TWD': 0.6, 'PLN': 0.7, 'THB': 0.4,
        'MYR': 0.4, 'IDR': 0.2, 'CZK': 0.3, 'HUF': 0.3,
        'ILS': 0.3, 'CLP': 0.3, 'PHP': 0.2, 'COP': 0.2,
        'SAR': 0.2, 'PEN': 0.1, 'RON': 0.1, 'AED': 0.2,
        'BHD': 0.0, 'BGN': 0.0,
    }

    # 2019 BIS Triennial (total daily turnover: $6,595 bn)
    # Source: BIS Triennial Survey 2019, Table 1
    bis_2019 = {
        'USD': 88.3, 'EUR': 32.3, 'JPY': 16.8, 'GBP': 12.8,
        'AUD': 6.8, 'CAD': 5.0, 'CHF': 5.0, 'CNY': 4.3,
        'HKD': 3.5, 'SGD': 1.8, 'SEK': 2.0, 'KRW': 2.0,
        'NOK': 1.8, 'NZD': 2.1, 'INR': 1.7, 'MXN': 1.7,
        'TWD': 0.9, 'ZAR': 1.0, 'BRL': 1.1, 'DKK': 0.6,
        'PLN': 0.6, 'THB': 0.5, 'ILS': 0.3, 'IDR': 0.4,
        'CZK': 0.3, 'AED': 0.2, 'TRY': 1.1, 'HUF': 0.4,
        'CLP': 0.3, 'SAR': 0.2, 'PHP': 0.2, 'MYR': 0.4,
        'COP': 0.2, 'RUB': 1.1, 'RON': 0.1, 'PEN': 0.1,
        'BHD': 0.0, 'BGN': 0.0,
    }

    # 2022 BIS Triennial (total daily turnover: $7,508 bn)
    # Source: BIS Triennial Survey 2022, Table 1
    # https://www.bis.org/statistics/rpfx22_fx.htm
    bis_2022 = {
        'USD': 88.4, 'EUR': 30.5, 'JPY': 16.7, 'GBP': 12.9,
        'CNY': 7.0, 'AUD': 6.4, 'CAD': 6.2, 'CHF': 5.2,
        'HKD': 2.6, 'SGD': 2.4, 'SEK': 2.2, 'KRW': 1.9,
        'NOK': 1.7, 'NZD': 1.7, 'INR': 1.6, 'MXN': 1.5,
        'TWD': 1.1, 'ZAR': 1.0, 'BRL': 0.9, 'DKK': 0.7,
        'PLN': 0.7, 'THB': 0.5, 'ILS': 0.5, 'IDR': 0.4,
        'CZK': 0.4, 'AED': 0.4, 'TRY': 0.4, 'HUF': 0.4,
        'CLP': 0.3, 'SAR': 0.2, 'PHP': 0.2, 'MYR': 0.2,
        'COP': 0.2, 'RUB': 0.2, 'RON': 0.1, 'PEN': 0.1,
        'BHD': 0.0, 'BGN': 0.0,
    }

    # Total daily turnover in USD billions per survey year
    # Used to compute absolute turnover per currency
    total_turnover_bn = {
        2001: 1239, 2004: 1934, 2007: 3324,
        2010: 3981, 2013: 5345, 2016: 5067,
        2019: 6595, 2022: 7508,
    }

    all_surveys = {
        2001: bis_2001, 2004: bis_2004, 2007: bis_2007,
        2010: bis_2010, 2013: bis_2013, 2016: bis_2016,
        2019: bis_2019, 2022: bis_2022,
    }

    # -----------------------------------------------------------------------
    # Build long-format DataFrame
    # -----------------------------------------------------------------------
    rows = []
    for year, survey in all_surveys.items():
        total_bn = total_turnover_bn[year]
        # BIS shares sum to 200%; normalise to 100%
        raw_sum = sum(survey.values())
        for ccy, share_200 in survey.items():
            country = CURRENCY_TO_COUNTRY.get(ccy)
            if country is None:
                continue
            share_100 = share_200 / raw_sum * 100  # normalised to 100%
            turnover_bn = share_200 / 100 * total_bn / 2  # per-currency daily avg
            rows.append({
                'year': year,
                'currency_code': ccy,
                'country_code': country,
                'fx_turnover_daily_bn': round(turnover_bn, 2),
                'fx_share_pct': round(share_100, 4),
                'fx_share_pct_200': share_200,
            })

    df = pd.DataFrame(rows)

    # Sort for readability
    df = df.sort_values(['year', 'fx_share_pct'], ascending=[True, False]).reset_index(drop=True)

    path = os.path.join(DATA_RAW, 'bis_fx_turnover_expanded.csv')
    df.to_csv(path, index=False)

    n_currencies = df['currency_code'].nunique()
    n_years = df['year'].nunique()
    print(f"BIS FX turnover (expanded) saved: {len(df)} rows "
          f"({n_currencies} currencies x {n_years} survey years) -> {path}")

    # Print 2022 summary
    latest = df[df['year'] == 2022].sort_values('fx_share_pct', ascending=False)
    print(f"\n2022 FX turnover share (normalised to 100%):")
    print(latest[['currency_code', 'country_code', 'fx_share_pct',
                   'fx_turnover_daily_bn']].to_string(index=False))

    return df


def pull_commodity_prices() -> pd.DataFrame:
    """
    Pull annual commodity price data for Bartik (shift-share) instrument.

    Returns DataFrame with columns:
        year, oil_price, coal_price, gas_price,
        oil_price_shock, coal_price_shock, gas_price_shock

    Price shock = log(P_t / P_{t-1}), i.e. log-change in price.

    Tries World Bank Commodity Price API first, falls back to hardcoded
    values from World Bank Pink Sheet data.

    Sources:
    - Crude oil: Brent, USD/barrel (World Bank Pink Sheet)
    - Coal: Newcastle thermal coal, USD/tonne (World Bank Pink Sheet)
    - Natural gas: Henry Hub, USD/MMBtu (World Bank Pink Sheet)
    """
    import numpy as np

    # ------------------------------------------------------------------
    # Hardcoded fallback data (World Bank Pink Sheet, verified values)
    # ------------------------------------------------------------------
    oil_data = {
        1965: 1.80, 1970: 1.80, 1973: 3.29, 1974: 11.58, 1975: 11.53,
        1980: 36.83, 1985: 27.56, 1990: 23.73, 1995: 17.02,
        2000: 28.50, 2001: 24.44, 2002: 25.02, 2003: 28.83, 2004: 38.27,
        2005: 54.52, 2006: 65.14, 2007: 72.39, 2008: 97.26, 2009: 61.67,
        2010: 79.50, 2011: 111.26, 2012: 111.67, 2013: 108.56, 2014: 98.97,
        2015: 52.32, 2016: 43.73, 2017: 54.19, 2018: 71.31, 2019: 64.21,
        2020: 41.96, 2021: 70.68, 2022: 99.04, 2023: 82.49, 2024: 80.75,
    }

    coal_data = {
        2000: 26, 2001: 37, 2002: 27, 2003: 29, 2004: 54,
        2005: 47, 2006: 49, 2007: 65, 2008: 128, 2009: 72,
        2010: 99, 2011: 121, 2012: 97, 2013: 84, 2014: 70,
        2015: 58, 2016: 66, 2017: 89, 2018: 107, 2019: 77,
        2020: 60, 2021: 139, 2022: 360, 2023: 174, 2024: 140,
    }

    gas_data = {
        2000: 4.32, 2001: 4.07, 2002: 3.33, 2003: 5.47, 2004: 5.85,
        2005: 8.69, 2006: 6.72, 2007: 6.97, 2008: 8.86, 2009: 3.94,
        2010: 4.37, 2011: 4.00, 2012: 2.75, 2013: 3.73, 2014: 4.37,
        2015: 2.61, 2016: 2.52, 2017: 2.99, 2018: 3.15, 2019: 2.56,
        2020: 2.03, 2021: 3.89, 2022: 6.45, 2023: 2.54, 2024: 2.19,
    }

    # ------------------------------------------------------------------
    # Try World Bank API for crude oil (Brent) as a connectivity test
    # If it works, we could get more granular data; but the hardcoded
    # Pink Sheet data is authoritative, so we use it as primary source.
    # ------------------------------------------------------------------
    api_oil = {}
    try:
        url = ("https://api.worldbank.org/v2/country/WLD/indicator/"
               "COMMODITY_PRICE_OIL_BRENT"
               "?format=json&per_page=200&date=1960:2024")
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if len(data) > 1 and data[1]:
                for obs in data[1]:
                    if obs['value'] is not None:
                        api_oil[int(obs['date'])] = float(obs['value'])
                if len(api_oil) > 20:
                    print(f"  World Bank API returned {len(api_oil)} years of oil prices")
                    oil_data.update(api_oil)  # API values override hardcoded
    except Exception as e:
        print(f"  World Bank API unavailable ({e}), using hardcoded Pink Sheet data")

    # ------------------------------------------------------------------
    # Build DataFrame from the union of all years with any data
    # ------------------------------------------------------------------
    all_years = sorted(set(oil_data.keys()) | set(coal_data.keys()) | set(gas_data.keys()))

    df = pd.DataFrame({'year': all_years})
    df['oil_price'] = df['year'].map(oil_data)
    df['coal_price'] = df['year'].map(coal_data)
    df['gas_price'] = df['year'].map(gas_data)

    # ------------------------------------------------------------------
    # Compute log-change price shocks: shock_t = ln(P_t / P_{t-1})
    # Only computed where consecutive years exist
    # ------------------------------------------------------------------
    df = df.sort_values('year').reset_index(drop=True)

    for commodity in ['oil', 'coal', 'gas']:
        price_col = f'{commodity}_price'
        shock_col = f'{commodity}_price_shock'
        df[shock_col] = np.log(df[price_col] / df[price_col].shift(1))
        # Only valid where year gap is 1
        year_gap = df['year'].diff()
        df.loc[year_gap != 1, shock_col] = np.nan

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------
    path = os.path.join(DATA_RAW, 'commodity_prices.csv')
    df.to_csv(path, index=False)

    n_oil = df['oil_price'].notna().sum()
    n_coal = df['coal_price'].notna().sum()
    n_gas = df['gas_price'].notna().sum()
    year_range = f"{df['year'].min()}-{df['year'].max()}"
    print(f"Commodity prices saved: {len(df)} rows, {year_range} -> {path}")
    print(f"  Oil: {n_oil} years, Coal: {n_coal} years, Gas: {n_gas} years")
    print(f"  Columns: {list(df.columns)}")

    return df


def validate_pull(df, name: str, min_rows: int = 10,
                  required_cols: list = None) -> bool:
    """
    Validate a pulled DataFrame. Call after every pull in __main__.
    Returns True on pass, False on any failure.
    Prevents silently running models on empty or malformed data.
    """
    if df is None:
        print(f"  [FAIL] {name}: pull returned None")
        return False
    if df.empty:
        print(f"  [FAIL] {name}: DataFrame is empty")
        return False
    if len(df) < min_rows:
        print(f"  [FAIL] {name}: only {len(df)} rows (expected >= {min_rows})")
        return False
    if required_cols:
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            print(f"  [FAIL] {name}: missing columns {missing}")
            return False
    print(f"  [PASS] {name}: {len(df)} rows, {len(df.columns)} columns")
    return True


if __name__ == "__main__":
    print("Pulling World Bank data...")
    wb_indicators = {
        'NY.GDP.MKTP.CD': 'gdp_usd',
        'NY.GDP.MKTP.KD.ZG': 'gdp_growth',
        'NE.TRD.GNFS.ZS': 'trade_openness',
        'EG.IMP.CONS.ZS': 'energy_imports_pct',
        'EG.USE.PCAP.KG.OE': 'energy_use_per_capita',
        'EG.ELC.NUCL.ZS': 'nuclear_pct_electricity',
        'FP.CPI.TOTL.ZG': 'inflation_cpi',
        'TX.VAL.FUEL.ZS.UN': 'fuel_exports_pct_merchandise',
        'TM.VAL.FUEL.ZS.UN': 'fuel_imports_pct_merchandise',
    }
    wb_df = pull_world_bank(wb_indicators)
    validate_pull(wb_df, 'World Bank WDI', min_rows=1000,
                  required_cols=['gdp_usd', 'trade_openness', 'inflation_cpi'])

    print("\nPulling IMF COFER data...")
    cofer_df = pull_imf_cofer()
    validate_pull(cofer_df, 'IMF COFER', min_rows=50)

    print("\nPulling Chinn-Ito capital account openness...")
    ci_df = pull_chinn_ito()
    validate_pull(ci_df, 'Chinn-Ito KAOPEN', min_rows=500, required_cols=['kaopen'])

    print("\nPulling Shambaugh FX regime classifications...")
    sh_df = pull_shambaugh_fx_regimes()
    validate_pull(sh_df, 'Shambaugh FX Regimes', min_rows=500)

    print("\nPulling JST Macrohistory (1870-2020)...")
    jst_df = pull_jst_macrohistory()
    validate_pull(jst_df, 'JST Macrohistory', min_rows=500)

    print("\nPulling financial depth indicators...")
    fd_df = pull_financial_depth()
    validate_pull(fd_df, 'Financial Depth', min_rows=100)

    print("\nPulling governance indicators (WGI)...")
    gov_df = pull_governance_indicators()
    validate_pull(gov_df, 'WGI Governance', min_rows=200,
                  required_cols=['political_stability'])

    print("\nLoading thorium reserves (USGS 2024)...")
    th_df = pull_thorium_reserves()
    validate_pull(th_df, 'Thorium Reserves', min_rows=10,
                  required_cols=['country_code', 'world_share'])

    print("\nLoading BIS FX turnover by currency (2010-2022)...")
    bis_df = pull_bis_fx_turnover()
    validate_pull(bis_df, 'BIS FX Turnover', min_rows=40,
                  required_cols=['country_code', 'year', 'fx_turnover_share_pct'])

    print("\nLoading BIS FX turnover EXPANDED (2001-2022, 38 currencies)...")
    bis_exp_df = pull_bis_fx_turnover_expanded()
    validate_pull(bis_exp_df, 'BIS FX Turnover Expanded', min_rows=200,
                  required_cols=['country_code', 'year', 'currency_code', 'fx_share_pct'])

    print("\nPulling EU ETS compliance data...")
    ets_df = pull_eu_ets()
    validate_pull(ets_df, 'EU ETS Compliance', min_rows=100)

    print("\nPulling OWID CO2 emissions data...")
    co2_df = pull_owid_co2()
    validate_pull(co2_df, 'OWID CO2', min_rows=5000,
                  required_cols=['country', 'year'])

    print("\nPulling IMF IFS inflation data...")
    ifs_df = pull_imf_ifs(['PCPI_IX'])
    validate_pull(ifs_df, 'IMF IFS', min_rows=100)

    print("\nPulling OWID energy data (Energy Institute Statistical Review)...")
    owid_df = pull_owid_energy()
    validate_pull(owid_df, 'OWID Energy', min_rows=5000,
                  required_cols=['country', 'year', 'primary_energy_consumption'])

    print("\nPulling commodity prices (oil, coal, gas) for Bartik instrument...")
    cp_df = pull_commodity_prices()
    validate_pull(cp_df, 'Commodity Prices', min_rows=20,
                  required_cols=['year', 'oil_price', 'coal_price', 'gas_price',
                                 'oil_price_shock', 'coal_price_shock', 'gas_price_shock'])

    print("\nAll automated pulls complete.")
    print("\nManual downloads still required (see DATA_AUDIT.md):")
    print("  1. EU ETS carbon prices → sandbag.be/carbon-price-viewer")
    print("  2. SWIFT RMB tracker → swift.com RMB tracker PDFs")
    print("  3. Russia energy export shifts → bruegel.org/dataset/russian-fossil-fuel-tracker")
