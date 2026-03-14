# §4 — Data and Measurement

## 4.1 Panel Construction

The present-leg panel covers six reserve currency entities — United States (USD),
Euro Area (EMU), United Kingdom (GBR), Japan (JPN), China (CHN), and Switzerland
(CHE) — over 1995–2024, yielding a maximum of 180 entity-year observations. Effective
observations after missing-data listwise deletion are approximately 155 for the main
specifications.

The Euro Area is constructed as a single entity from 1999, with NEP calculated as a
GDP-weighted average of the five largest eurozone members by economic weight:
Germany, France, Italy, Spain, and the Netherlands. This construction captures the
aggregate energy import dependence that affects the EUR's structural position while
avoiding the fragmentation problems of treating each member state separately.

## 4.2 Reserve Currency Share

Reserve currency share is sourced from the IMF Currency Composition of Official Foreign
Exchange Reserves (COFER) database, which reports the share of allocated global
reserves held in each major currency. COFER data has two limitations that the paper
accounts for explicitly. First, reporting is voluntary; the allocated share was only
~55% of total reserves in the early 2000s, rising to ~95% by 2024. Second, China's
renminbi was added to the SDR basket in 2016 and COFER reporting improved subsequently;
CNY reserve share data before 2016 are reconstructions.

## 4.3 Net Energy Position

Net Energy Position (NEP) measures a country's energy sovereignty as its share of
world primary energy production minus its net energy import share:

```
NEP_{i,t} = (production_{i,t} / world_production_t) - (net_imports_{i,t} / world_production_t)
```

A positive NEP indicates a net energy exporter (the country contributes more to the
world energy supply than it draws from it); a negative NEP indicates a net importer.
The normalisation to world production shares — rather than domestic consumption shares
— ensures comparability across countries of different sizes and across time as world
energy volumes grow.

Data are sourced from the World Bank World Development Indicators (energy production
and use, ktoe) extended with Our World in Data (OWID) which aggregates BP Statistical
Review of World Energy data to 2024. The two series are spliced at 2021 using a linear
adjustment factor to correct for methodological differences in primary energy accounting.

**The λ=10 lag.** The generational lag between energy position and reserve currency
status is estimated from the USA case: the correlation between NEP and reserve share
is maximised at lag 10 in the ARDL bounds specification. The same lag is applied to
all entities for consistency, though entity-specific lag estimation would be a
refinement. The economic rationale: monetary trust accumulates through decades of
stable exchange, not years; a country's energy position in 2010 affects its monetary
credibility as perceived by central banks making reserve allocation decisions in 2020.

## 4.4 EU ETS Data

EU ETS compliance data — annual freely allocated allowances and verified emissions by
sector, 2005–2024 — are sourced from the European Commission's European Union
Transaction Log (EUTL), downloaded via the Sandbag Carbon Price Viewer. Allocation
surplus (freely allocated minus verified) is the governance variable on which the
Zivot-Andrews test is run.

EUA spot prices (2005–2024) used in the coefficient of variation analysis are
reconstructed from academic sources: Ellerman and Buchner (2008) for Phase I dynamics,
Koch et al. (2014) for Phase II and the 2013 collapse, Bayer and Aklin (2020) for
cross-phase reconstruction, and European Commission monitoring reports for Phase III
and IV annual averages. These are annual average prices; intra-year high-frequency
data from Sandbag or ICAP would provide a more precise CV estimate for Phase I in
particular. The data note in the backward leg notebook flags this limitation
explicitly.

RGGI auction clearing prices (2009–2024) are sourced from RGGI Inc. quarterly auction
results, which are publicly available. Annual averages are used to match the EU ETS
annual frequency.

## 4.5 Thorium Reserves and TMPI Components

Thorium reserve data are sourced from the World Nuclear Association (WNA) and USGS
Mineral Commodity Summaries (2024 edition), which reports identified thorium resources
by country in thousand tonnes. World shares are computed from these totals.

Nuclear energy share (nuclear consumption as a fraction of primary energy consumption)
is from OWID/BP Statistical Review of World Energy, 2024 edition.

Institutional quality is the World Governance Indicators (WGI) composite, computed
as the unweighted average of the six WGI dimensions (Voice and Accountability, Political
Stability, Government Effectiveness, Regulatory Quality, Rule of Law, Control of
Corruption). The composite is normalised to [0,1] for use in the multiplicative TMPI.

TMPI is constructed multiplicatively:

```
TMPI_i = thorium_reserve_share_i × nuclear_share_energy_i × institutional_quality_i
```

Scores are then normalised to a 100-point scale with USA=100 for presentation.

**The static TMPI limitation.** TMPI is a snapshot of structural endowments; it does
not model the dynamic accumulation of nuclear capacity over the transition period.
Trajectory adjustment columns are reported in `outputs/tables/tmpi_rankings.csv`
using CAGR-based projections to 2035, with Japan using its official policy target
(20% nuclear by 2035) rather than an extrapolation from near-zero post-Fukushima
levels. These trajectory scores are addenda; the static TMPI is the primary cross-
section result.

## 4.6 Governance Sensitivity Measurement

GS is defined as the ratio of energy governance volatility to commodity benchmark
volatility:

```
GS_{i,t} = CV(EG_{i,era}) / CV(commodity_benchmark_{era})
```

For the backward leg, EG is the EU ETS allocation surplus (annual, 2005–2024) and the
benchmark is Brent crude oil (annual average, same period). For the CV comparison of
carbon prices, EG is the annual average EUA spot price by phase; the benchmark is
Brent crude oil 2005–2024 (CV=0.292) and RGGI allowance prices by period.

GS is estimated for the EU carbon era only in this paper. Cross-country GS — using
domestic energy price regulation data or regulatory stringency indices — is identified
as the primary extension for future work. In the MPI assembly (Section 7), all
entities receive the EU ETS GS value of 2.83 as a common governance benchmark; Russia
post-2022 is assigned GS=0.05 to reflect exclusion from Western monetary convertibility
infrastructure under sanctions.

## 4.7 BIS FX Turnover Data

BIS Triennial Central Bank Survey data on FX turnover by currency (2004, 2007, 2010,
2013, 2016, 2019, 2022) are used to cross-validate reserve share findings and as the
primary data source for forward predictions. INR FX turnover share (1.6% in 2022) is
the baseline against which the BIS 2028 and 2031 predictions are benchmarked.

## 4.8 Summary Statistics

Full summary statistics, variable definitions, and data sources are reported in the
supplementary appendix. The panel dataset (`data/processed/panel_model_ready.csv`) is
available in the replication archive.

| Variable | Source | Period | N entities | Notes |
|----------|--------|--------|-----------|-------|
| Reserve share (%) | IMF COFER | 1995–2024 | 6 | Allocated reserves only |
| NEP | World Bank / OWID/BP | 1900–2024 | 180+ | λ=10 lag used in main spec |
| ETS surplus (Mt CO2) | EC EUTL / Sandbag | 2005–2024 | EU only | ZA test variable |
| EUA price (EUR/tCO2) | Academic reconstruction | 2005–2024 | EU only | CV comparison; see data note |
| RGGI price (USD/tCO2) | RGGI Inc. | 2009–2024 | US NE only | CV benchmark |
| Thorium reserves | WNA / USGS 2024 | Cross-section | 12 | Thousand tonnes |
| Nuclear share (%) | OWID/BP 2024 | 1965–2024 | 12 | Primary energy share |
| WGI composite | World Bank | 1996–2024 | 12 | Unweighted avg of 6 dims |
