"""
viz.py
Visualization functions for the Carbon-Thorium Standard paper.
All functions return matplotlib Figure objects and optionally save to outputs/figures/.

Usage:
    from viz import plot_reserve_share_history, plot_nep_vs_reserve_share, ...
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

sns.set_theme(style='whitegrid', font_scale=1.1)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'figures')

CURRENCY_COLORS = {
    'USD': '#1f77b4',
    'EUR': '#ff7f0e',
    'GBP': '#2ca02c',
    'JPY': '#d62728',
    'CNY': '#9467bd',
    'CHF': '#8c564b',
    'AUD': '#e377c2',
    'CAD': '#7f7f7f',
}

COUNTRY_COLORS = {
    'CHN': '#d62728',
    'IND': '#ff7f0e',
    'RUS': '#1f77b4',
    'JPN': '#2ca02c',
    'AUS': '#9467bd',
    'CAN': '#8c564b',
    'BRA': '#e377c2',
    'USA': '#7f7f7f',
    'GBR': '#bcbd22',
    'DEU': '#17becf',
}

CASE_COLORS = {
    'rising_producer':              '#d62728',
    'thorium_reserve_holder':       '#ff7f0e',
    'forced_fragmentation':         '#1f77b4',
    'control_case':                 '#2ca02c',
    'reserves_without_capacity':    '#9467bd',
    'modest_reserves_strong_institutions': '#8c564b',
    'reserves_without_institutions': '#e377c2',
}


def _save(fig, filename: str):
    os.makedirs(FIGURES_DIR, exist_ok=True)
    path = os.path.join(FIGURES_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches='tight')
    print(f"Saved: {path}")


def plot_reserve_share_history(df: pd.DataFrame,
                                currencies: list = None,
                                save: bool = False) -> plt.Figure:
    """
    Line plot of reserve_share over time for selected currencies.
    Uses IMF COFER data (processed by construct_reserve_share).

    df must have columns: country_code, year, reserve_share
    """
    if currencies is None:
        currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY']

    fig, ax = plt.subplots(figsize=(11, 6))

    for ccy in currencies:
        sub = df[df['country_code'] == ccy].sort_values('year')
        if sub.empty:
            continue
        color = CURRENCY_COLORS.get(ccy, None)
        ax.plot(sub['year'], sub['reserve_share'] * 100,
                label=ccy, color=color, linewidth=2, marker='o', markersize=3)

    ax.set_xlabel('Year')
    ax.set_ylabel('Share of Allocated Reserves (%)')
    ax.set_title('Global Reserve Currency Composition\nIMF COFER, 1999–present')
    ax.legend(title='Currency', bbox_to_anchor=(1.02, 1), loc='upper left')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}%'))
    ax.set_xlim(df['year'].min(), df['year'].max())
    fig.tight_layout()

    if save:
        _save(fig, 'reserve_share_history.png')
    return fig


def plot_nep_vs_reserve_share(df: pd.DataFrame,
                               country_codes: list = None,
                               lag: int = 10,
                               save: bool = False) -> plt.Figure:
    """
    Scatter plot: lagged Net Energy Position vs reserve_share.
    Each point is a country-year. Regression line over all points.
    Colored by country.

    df must have: country_code, year, reserve_share,
                  net_energy_position_lag{lag}
    """
    lag_col = f'net_energy_position_lag{lag}'
    if lag_col not in df.columns:
        print(f"Column {lag_col} not found. Run construct_lagged_variables first.")
        return None

    plot_df = df.dropna(subset=[lag_col, 'reserve_share']).copy()
    if country_codes:
        plot_df = plot_df[plot_df['country_code'].isin(country_codes)]

    fig, ax = plt.subplots(figsize=(9, 6))

    for code, grp in plot_df.groupby('country_code'):
        color = COUNTRY_COLORS.get(code, '#aaaaaa')
        ax.scatter(grp[lag_col], grp['reserve_share'] * 100,
                   label=code, color=color, alpha=0.7, s=30)

    # OLS regression line
    x = plot_df[lag_col].values
    y = plot_df['reserve_share'].values * 100
    if len(x) > 2:
        m, b = np.polyfit(x, y, 1)
        x_line = np.linspace(x.min(), x.max(), 100)
        ax.plot(x_line, m * x_line + b, 'k--', linewidth=1.5,
                label=f'OLS fit (β={m:.3f})')

    ax.set_xlabel(f'Net Energy Position (lagged {lag}yr)')
    ax.set_ylabel('Reserve Share (%)')
    ax.set_title(f'Net Energy Position (t−{lag}) vs Reserve Currency Share\n'
                 f'Pooled country-years')
    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=8)
    fig.tight_layout()

    if save:
        _save(fig, f'nep_vs_reserve_share_lag{lag}.png')
    return fig


def plot_focal_country_panel(df: pd.DataFrame,
                              country_code: str,
                              variables: list = None,
                              save: bool = False) -> plt.Figure:
    """
    Multi-panel time series for a single focal country.
    Shows net_energy_position, reserve_share, and gdp_share on stacked subplots.
    Key events annotated with vertical dashed lines.

    df must have: country_code, year, and the requested variables.
    """
    if variables is None:
        variables = ['net_energy_position', 'reserve_share', 'gdp_share']

    sub = df[df['country_code'] == country_code].sort_values('year')
    available = [v for v in variables if v in sub.columns and sub[v].notna().any()]

    if not available:
        print(f"No data for {country_code}")
        return None

    # Key events per country (from variables.py FOCAL_COUNTRIES)
    KEY_EVENTS = {
        'CHN': {2001: 'WTO', 2015: 'SDR', 2018: 'Yuan oil futures', 2022: 'De-dollarization'},
        'IND': {2008: 'Civil Nuclear Agmt', 2022: 'Rupee-Ruble corridor'},
        'RUS': {2014: 'SWIFT threat', 2022: 'SWIFT exclusion'},
        'JPN': {1973: 'Oil shock', 1985: 'Plaza Accord', 2011: 'Fukushima'},
        'AUS': {2022: 'AUKUS'},
        'CAN': {1971: 'CANDU'},
        'BRA': {1982: 'Angra 1'},
    }
    events = KEY_EVENTS.get(country_code, {})

    n = len(available)
    fig, axes = plt.subplots(n, 1, figsize=(11, 3 * n), sharex=True)
    if n == 1:
        axes = [axes]

    labels = {
        'net_energy_position': 'Net Energy Position\n(world share)',
        'reserve_share': 'Reserve Currency Share (%)',
        'gdp_share': 'GDP Share of World Output (%)',
        'energy_dominance_weighted': 'Era-Weighted Energy Dominance',
        'export_leverage': 'Energy Export Leverage',
    }

    color = COUNTRY_COLORS.get(country_code, '#1f77b4')

    for ax, var in zip(axes, available):
        y = sub[var] * (100 if 'share' in var and sub[var].max() < 2 else 1)
        ax.plot(sub['year'], y, color=color, linewidth=2)
        ax.fill_between(sub['year'], y, alpha=0.15, color=color)
        ax.set_ylabel(labels.get(var, var), fontsize=9)
        ax.axhline(0, color='black', linewidth=0.5, linestyle=':')

        for yr, label in events.items():
            if sub['year'].min() <= yr <= sub['year'].max():
                ax.axvline(yr, color='gray', linewidth=1, linestyle='--', alpha=0.7)
                ax.text(yr, ax.get_ylim()[1] * 0.9, label,
                        rotation=90, fontsize=7, color='gray',
                        va='top', ha='right')

    axes[-1].set_xlabel('Year')
    fig.suptitle(f'{country_code} — Energy & Monetary Position', fontsize=13,
                 fontweight='bold')
    fig.tight_layout()

    if save:
        _save(fig, f'focal_panel_{country_code.lower()}.png')
    return fig


def plot_tmpi_ranking(tmpi_df: pd.DataFrame,
                      year: int = 2023,
                      save: bool = False) -> plt.Figure:
    """
    Horizontal bar chart of TMPI scores by country.
    Colored by case_type. Shows the three TMPI components stacked.

    tmpi_df must have: country_code, tmpi_scaled (or tmpi),
    and ideally thorium_reserve_share, nuclear_share_energy,
    institutional_quality, case_type.
    """
    cols_needed = ['country_code', 'tmpi_scaled']
    if not all(c in tmpi_df.columns for c in cols_needed):
        if 'tmpi' in tmpi_df.columns:
            tmpi_df = tmpi_df.copy()
            tmpi_max = tmpi_df['tmpi'].max()
            tmpi_df['tmpi_scaled'] = tmpi_df['tmpi'] / tmpi_max * 100 if tmpi_max > 0 else 0
        else:
            print("tmpi_scaled or tmpi column not found.")
            return None

    plot_df = (tmpi_df[tmpi_df['tmpi_scaled'] > 0]
               .sort_values('tmpi_scaled', ascending=True)
               .tail(15))

    fig, ax = plt.subplots(figsize=(9, 7))

    colors = [CASE_COLORS.get(ct, '#aaaaaa')
              for ct in plot_df.get('case_type', [''] * len(plot_df))]

    bars = ax.barh(plot_df['country_code'], plot_df['tmpi_scaled'],
                   color=colors, alpha=0.85, edgecolor='white')

    ax.set_xlabel('TMPI Score (0–100, normalised)')
    ax.set_title(f'Thorium Monetary Potential Index — {year}\n'
                 f'TMPI = Reserves × Nuclear Capacity × Institutional Quality')
    ax.axvline(50, color='gray', linewidth=0.8, linestyle='--', alpha=0.5,
               label='Midpoint')

    # Annotate bars with scores
    for bar, val in zip(bars, plot_df['tmpi_scaled']):
        ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2,
                f'{val:.1f}', va='center', fontsize=8)

    ax.text(0.98, 0.02,
            'High TMPI = positioned for monetary leverage\n'
            'in a thorium-dominant energy era.\n'
            'Falsifiable prediction: check by 2035.',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=8, color='gray',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    fig.tight_layout()

    if save:
        _save(fig, 'tmpi_ranking.png')
    return fig


def plot_carbon_capture(phase_stats_df: pd.DataFrame,
                        annual_stats_df: pd.DataFrame,
                        save: bool = False) -> plt.Figure:
    """
    Two-panel figure:
      Top: EUA price time series (annual mean) with ETS phase boundaries.
      Bottom: Coefficient of variation by ETS phase (bar chart).

    Illustrates the sovereign capture mechanism — high CV in Phase I
    reflects political over-allocation, not commodity fundamentals.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))

    # Panel 1: price time series
    if 'year' in annual_stats_df.columns and 'mean' in annual_stats_df.columns:
        ax1.plot(annual_stats_df['year'], annual_stats_df['mean'],
                 color='#1f77b4', linewidth=2, label='EUA mean price (€)')
        ax1.fill_between(annual_stats_df['year'],
                         annual_stats_df['mean'] - annual_stats_df.get('std', 0),
                         annual_stats_df['mean'] + annual_stats_df.get('std', 0),
                         alpha=0.2, color='#1f77b4', label='±1 std')

    phase_boundaries = {2008: 'Phase II', 2013: 'Phase III', 2021: 'Phase IV'}
    for yr, label in phase_boundaries.items():
        ax1.axvline(yr, color='gray', linewidth=1, linestyle='--', alpha=0.7)
        ax1.text(yr + 0.1, ax1.get_ylim()[1] * 0.9, label,
                 fontsize=8, color='gray', va='top')

    ax1.set_ylabel('EUA Price (€/tonne CO₂)')
    ax1.set_title('EU ETS Carbon Price History by Phase\n'
                  'Phase I collapse = political over-allocation (documented)')
    ax1.legend()

    # Panel 2: CV by phase
    if not phase_stats_df.empty and 'cv' in phase_stats_df.columns:
        colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4']
        bars = ax2.bar(phase_stats_df['label'], phase_stats_df['cv'],
                       color=colors[:len(phase_stats_df)], alpha=0.8)

        # Benchmark lines
        ax2.axhline(0.15, color='green', linewidth=1.2, linestyle='--',
                    label='Gold CV benchmark (~0.15)')
        ax2.axhline(0.25, color='orange', linewidth=1.2, linestyle='--',
                    label='Oil CV benchmark (~0.25)')

        for bar, val in zip(bars, phase_stats_df['cv']):
            ax2.text(bar.get_x() + bar.get_width() / 2, val + 0.01,
                     f'{val:.2f}', ha='center', fontsize=9, fontweight='bold')

    ax2.set_ylabel('Coefficient of Variation (σ/μ)')
    ax2.set_title('EUA Price Volatility by Phase\n'
                  'High CV = politically constructed price, not commodity fundamentals')
    ax2.legend()
    plt.setp(ax2.get_xticklabels(), rotation=15, ha='right')

    fig.tight_layout()

    if save:
        _save(fig, 'carbon_capture_mechanism.png')
    return fig


def plot_era_energy_weights(save: bool = False) -> plt.Figure:
    """
    Stacked bar chart showing era weight assumptions.
    Makes model assumptions explicit — essential for transparency.
    Source: OWID / Energy Institute Statistical Review.
    """
    eras = ['Coal Era\n(pre-1950)', 'Oil Era\n(1950–1999)', 'Transition Era\n(2000–present)']
    fuels = ['coal_production', 'oil_production', 'gas_production',
             'nuclear_consumption', 'renewables_consumption']
    fuel_labels = ['Coal', 'Oil', 'Gas', 'Nuclear', 'Renewables']
    fuel_colors = ['#3d3d3d', '#636363', '#969696', '#ffcc44', '#4daf4a']

    weights = {
        'coal_production':        [0.85, 0.28, 0.27],
        'oil_production':         [0.10, 0.45, 0.32],
        'gas_production':         [0.03, 0.18, 0.25],
        'nuclear_consumption':    [0.00, 0.06, 0.05],
        'renewables_consumption': [0.02, 0.03, 0.11],
    }

    fig, ax = plt.subplots(figsize=(9, 5))
    bottoms = np.zeros(3)

    for fuel, label, color in zip(fuels, fuel_labels, fuel_colors):
        vals = weights[fuel]
        ax.bar(eras, vals, bottom=bottoms, label=label, color=color,
               alpha=0.9, edgecolor='white')
        for i, (v, b) in enumerate(zip(vals, bottoms)):
            if v > 0.04:
                ax.text(i, b + v / 2, f'{v:.0%}', ha='center', va='center',
                        fontsize=9, color='white', fontweight='bold')
        bottoms += np.array(vals)

    ax.set_ylabel('Share of World Primary Energy')
    ax.set_title('Era Energy Mix Weights Used in Model\n'
                 'Source: OWID / Energy Institute Statistical Review of World Energy')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0%}'))
    ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
    ax.set_ylim(0, 1.05)
    ax.text(0.01, 0.01, 'Verify with compute_era_weights_from_owid(owid_df)',
            transform=ax.transAxes, fontsize=8, color='gray')

    fig.tight_layout()

    if save:
        _save(fig, 'era_energy_weights.png')
    return fig
