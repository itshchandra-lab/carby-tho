# The Carbon-Thorium Standard
## Energy-Monetary Transitions: An Empirical Model

**Working paper project — empirical research supporting:**
*"The Carbon-Thorium Standard: Energy-Backed Currencies and the Architecture of Monetary Failure in a Multipolar World"*

---

## Core Hypothesis

A sustained shift in a nation's net energy position (production share minus import dependency) is followed by a statistically significant change in that nation's currency share of global foreign exchange reserves within a measurable lag window, controlling for GDP share, trade openness, financial market depth, political stability, and inflation history.

---

## Project Structure

```
carby-tho/
│
├── data/
│   ├── raw/              # Original downloaded data — never modified
│   └── processed/        # Cleaned, merged datasets ready for modeling
│
├── notebooks/
│   ├── 01_data_pull.ipynb        # API pulls from IMF, World Bank, EU
│   ├── 02_data_cleaning.ipynb    # Merging, filling gaps, constructing variables
│   ├── 03_eda.ipynb              # Exploratory analysis, visualizations
│   ├── 04_panel_model.ipynb      # Panel regression with fixed effects
│   ├── 05_var_model.ipynb        # VAR model for directionality
│   └── 06_carbon_capture.ipynb   # Carbon price volatility + political calendar
│
├── src/
│   ├── data_pull.py      # Functions for pulling each data source
│   ├── variables.py      # Variable construction logic
│   ├── models.py         # Model specifications
│   └── viz.py            # Visualization functions
│
├── outputs/
│   ├── figures/          # All charts and visualizations
│   └── tables/           # Regression output tables
│
├── paper/
│   └── working_paper.md  # The paper itself, updated as model develops
│
├── requirements.txt
└── README.md
```

---

## Data Sources

| Variable | Source | Coverage |
|----------|--------|----------|
| Reserve currency share | IMF COFER | 1999–present |
| Reserve currency share (historical) | Eichengreen & Flandreau reconstruction | 1900–1999 |
| Primary energy production by country | World Bank WDI | 1960–present |
| Coal production (historical) | BP Statistical Review | 1900–present |
| Energy imports/exports | World Bank WDI | 1960–present |
| GDP share of world output | World Bank WDI | 1960–present |
| Trade openness | World Bank WDI | 1960–present |
| Financial market depth | BIS / World Bank | 1960–present |
| Political stability | World Bank Governance Indicators | 1996–present |
| Inflation history | IMF IFS | 1960–present |
| Carbon prices (EU ETS) | EU ETS registry / Refinitiv | 2005–present |
| Thorium reserves | IAEA / national geological surveys | Point estimates |

---

## Model Architecture

### Model 1 — Panel Regression (Fixed Effects)
**Question:** Does net energy position predict reserve currency share?

```
ReservShare_it = α_i + β1(NetEnergyPos_it) + β2(GDPShare_it) + 
                 β3(TradeOpen_it) + β4(FinDepth_it) + 
                 β5(PolStab_it) + β6(Inflation_it) + 
                 Σ(lag_windows: 5,10,15,20yr) + ε_it
```

### Model 2 — VAR (Vector Autoregression)
**Question:** Does energy dominance *cause* monetary dominance, or vice versa?

Tests directionality of the relationship. Granger causality tests between energy position and reserve share.

### Model 3 — Carbon Capture Regression
**Question:** Does carbon price volatility correlate with political calendar events?

```
CarbonPriceVariance_t = α + β1(ElectionYear_t) + β2(PolicyChange_t) + 
                         β3(LobbyingIntensity_t) + ε_t
```

High correlation = empirical evidence of sovereign capture.

---

## Key Variables to Construct

**Net Energy Position:**
```
NetEnergyPos_it = (DomesticProduction_it / WorldProduction_t) - (EnergyImports_it / GDP_it)
```

**Energy Dominance Weighted Share:**
Weight each energy type by its share of global primary energy consumption in that period. Coal-weighted for 1900-1950, oil-weighted for 1950-2000, transition-weighted for 2000-present.

**Carbon Capture Index:**
Variance of monthly carbon price / mean carbon price, measured around political calendar events (elections ±6 months, major policy announcements).

---

## Time Period

- **Full model:** 1900–present (three transition periods)
- **Data-rich model:** 1960–present (cleaner data, more controls)
- **Carbon capture model:** 2005–present (EU ETS data)

---

## Focal Country Cases

Four countries serve as deep case studies within the panel model. Each tests a different dimension of the energy-monetary hypothesis.

| Country | Case Type | Core Test |
|---------|-----------|-----------|
| China | Rising energy producer | Monetary ambition tracks improving net energy position |
| India | Concentrated reserve holder | Thorium geography directly shapes monetary strategy |
| Russia | Forced fragmentation | Bloc formation under duress — natural experiment post-2022 |
| Japan | Chronic energy importer | Energy dependency suppresses monetary ambition despite GDP size |

### Why These Four

**China** — Energy importer becoming producer. Massive renewable buildout, TMSR thorium reactor operational 2023, active de-dollarization via CIPS and yuan-denominated oil trades. If the model works, China should show rising reserve currency ambition correlating with improving net energy position over time.

**India** — Holds ~25% of global thorium reserves. Runs a three-stage nuclear program explicitly designed to exploit domestic thorium. Simultaneously building rupee-based energy corridors with Russia post-2022. The clearest case of energy geography directly shaping monetary strategy. Primary test of the thorium leg.

**Russia** — The natural experiment. Post-2022 SWIFT exclusion forced overnight monetary fragmentation. Ruble-yuan and ruble-rupee energy corridors emerged by necessity, not design. This is the fragmented bloc thesis playing out in real time under external shock. Tests whether energy relationships determine monetary corridor formation under duress.

**Japan** — The control case. Third largest economy. Near-zero domestic energy production. Structural energy importer for over a century. Despite GDP size, the yen never achieved deep reserve currency status. If net energy position is predictive, Japan should consistently underperform what its GDP share alone would predict. The strongest test of the model against the null hypothesis that GDP is all that matters.

### Data Requirements by Country

**China**
- PBOC reserve data (supplementary to COFER)
- CIPS transaction volume (BIS quarterly review)
- Yuan-denominated oil trade volumes (IEA)
- Renewable energy capacity additions (OWID/IEA)
- TMSR reactor operational status (IAEA)

**India**
- Thorium reserve estimates (IAEA/Atomic Minerals Directorate)
- Three-stage nuclear programme capacity (AERB)
- Rupee-ruble/rupee-yuan bilateral trade settlement data (RBI)
- Energy import dependency over time (World Bank)

**Russia**
- Pre/post-2022 SWIFT transaction volumes (BIS)
- Ruble-yuan settlement volumes (PBOC/CBR joint data)
- Energy export destinations and currencies (IEA)
- SPFS (Russian SWIFT alternative) adoption (CBR)

**Japan**
- Energy import dependency (World Bank — longest series available)
- Yen reserve share vs GDP share divergence (IMF COFER)
- Historical energy mix (OWID — back to 1900)
- Current nuclear restart programme status (IAEA)

```bash
pip install -r requirements.txt
```

---

## Status

- [ ] Data pull scripts
- [ ] Data cleaning
- [ ] Variable construction
- [ ] EDA
- [ ] Panel model
- [ ] VAR model
- [ ] Carbon capture model
- [ ] Paper draft
