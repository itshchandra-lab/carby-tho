# §4 — Data and Measurement

The paper draws on six data sources, each corresponding to a component of the MPI framework.

**Reserve currency share** comes from the IMF's Currency Composition of Official Foreign Exchange Reserves (COFER) database, 1995 to 2024. Six entities are included: the US dollar, euro, British pound, Japanese yen, Chinese renminbi, and Swiss franc. The renminbi entered full COFER reporting in 2016; earlier observations are reconstructions and are treated with appropriate caution.

**Net Energy Position** is constructed from World Bank World Development Indicators extended with the Our World in Data and BP Statistical Review of World Energy data. The formula is a state's share of world energy production minus its net import share of world production. The lag of ten years applied throughout the paper is estimated from the US case and tested at five, eight, twelve, and fifteen years in the robustness analysis.

**EU ETS data** — annual freely allocated allowances and verified emissions by sector, 2005 to 2024 — comes from the European Commission's European Union Transaction Log, downloaded via the Sandbag Carbon Price Viewer. EUA spot prices are reconstructed from academic sources including Ellerman and Buchner (2008), Koch et al. (2014), and Bayer and Aklin (2020). RGGI auction clearing prices come from RGGI Inc.'s quarterly results.

**Thorium reserve data** comes from the World Nuclear Association and the 2024 USGS Mineral Commodity Summaries. Nuclear energy share comes from OWID and the BP Statistical Review. **Institutional quality** is the World Governance Indicators composite — the unweighted average of the six WGI dimensions — normalised to a zero-to-one scale.

**BIS Triennial Central Bank Survey** data on foreign exchange turnover by currency, from 2004 through 2022, provides the cross-validation for the present-register findings and the primary baseline for the forward predictions.

| Variable | Source | Period | Notes |
|----------|--------|--------|-------|
| Reserve share (%) | IMF COFER | 1995–2024 | 6 entities; allocated reserves only |
| Net Energy Position | World Bank / OWID / BP | 1900–2024 | Primary spec: λ=10 lag |
| ETS allocation surplus | EC EUTL / Sandbag | 2005–2024 | Structural break test variable |
| EUA price (EUR/tCO2) | Academic reconstruction | 2005–2024 | Annual averages; see note |
| RGGI price (USD/tCO2) | RGGI Inc. | 2009–2024 | Volatility comparison |
| Thorium reserves | WNA / USGS 2024 | Cross-section | 12 countries; thousand tonnes |
| Nuclear energy share (%) | OWID / BP 2024 | 1965–2024 | Primary energy share |
| Institutional quality | World Bank WGI | 1996–2024 | Unweighted avg of 6 dimensions |
| FX turnover share (%) | BIS Triennial Survey | 2004–2022 | Forward prediction baseline |
| Sterling reserve share (%) | Eichengreen and Flandreau (2009) | 1899–1980 | Historical validation; §6.7 |
| UK energy production share | OWID / BP Statistical Review | 1900–1980 | Historical NEP proxy; §6.7 |

---
