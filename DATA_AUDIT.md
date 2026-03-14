# Focal Country Data Audit
## What's available programmatically vs what requires manual collection

---

## CONFIRMED AVAILABLE — Pull automatically

### OWID Energy Dataset (1900–2024)
All four focal countries have 85–86 well-populated columns including:
- Coal, oil, gas production (TWh and per capita)
- Nuclear consumption and share of electricity
- Renewables consumption and share
- Net electricity imports
- Primary energy consumption
- All energy type shares

**Coverage:** CHN/IND/JPN from 1900, RUS from 1985

### World Bank WDI — Focal Country Indicators
All confirmed working for CHN, IND, RUS, JPN:

| Indicator | Coverage |
|-----------|----------|
| GDP (USD) | 1990–2023 |
| Trade openness | 1990–2023 |
| Inflation (CPI) | 1990–2023 |
| Energy imports (% of use) | 1990–2023 |
| Nuclear (% of electricity) | 1990–2023 |
| Fossil fuel (% of energy) | 1990–2023 |
| Fuel exports (% of merchandise) | 1990–2022 |
| Fuel imports (% of merchandise) | 1990–2022 |
| FDI inflows (% of GDP) | 1990–2023 |

### IMF DataMapper — Focal Countries
| Indicator | Coverage |
|-----------|----------|
| Current account (% GDP) | 1997–2030 |
| GDP growth | 1980–2030 |
| Inflation | 1981–2030 |

### OWID CO2 Dataset
- CO2 emissions by country and fuel type
- 254 countries, all four focal countries confirmed

---

## PARTIALLY AVAILABLE — Need workarounds

### IMF COFER (Reserve Currency Shares)
- Available 1999–present via CSV download
- **Gap:** China does not fully report to COFER
- **Workaround:** Use academic reconstructions (Eichengreen & Flandreau) for pre-1999 and supplement COFER with BIS locational banking statistics for China estimates

### IMF Direction of Trade Statistics (DOTS)
- API returning 503 (intermittent outage, not permanent block)
- **What it gives:** Bilateral trade flows between focal countries
- **Workaround:** Retry in session; or use UN Comtrade as backup
- **Critical for:** Russia-China, India-Russia bilateral energy trade post-2022

### EU ETS Carbon Price History
- Ember URL broken (403)
- EEA datahub has compliance data (confirmed working)
- **Gap:** Daily/monthly EUA spot price history for volatility analysis
- **Workaround:** 
  - Sandbag carbon price viewer (manual CSV download): https://sandbag.be/carbon-price-viewer/
  - ICAP Allowance Price Explorer (manual download): https://icapcarbonaction.com/en/ets-prices
  - Refinitiv/LSEG (requires subscription)

---

## NOT AVAILABLE PROGRAMMATICALLY — Manual collection required

These are important but require manual download or subscription:

### China-specific
| Data | Source | Format | Notes |
|------|--------|--------|-------|
| CIPS transaction volumes | BIS Quarterly Review (Table 1) | PDF/manual | Quarterly, 2015–present |
| Yuan-denominated oil trade volumes | IEA Oil Market Report | PDF/manual | Monthly |
| PBOC reserve composition (full) | PBOC Annual Report | PDF/manual | China partial reporter to COFER |
| SWIFT RMB tracker monthly | SWIFT website | PDF | Monthly share data |

### India-specific
| Data | Source | Format | Notes |
|------|--------|--------|-------|
| Thorium reserve estimates | IAEA/Atomic Minerals Directorate | PDF | Point estimates, occasional updates |
| Rupee-ruble settlement volumes | Reserve Bank of India Annual Report | PDF | From 2022 |
| Three-stage nuclear capacity | Atomic Energy Regulatory Board | PDF | Annual |

### Russia-specific
| Data | Source | Format | Notes |
|------|--------|--------|-------|
| SPFS adoption rate | CBR Annual Payment System Report | PDF | Annual |
| Russian crude discount post-2022 | IEA/Bruegel tracker | Web/manual | Bruegel updates regularly |
| Ruble-yuan settlement volumes | CBR + PBOC joint releases | PDF | Sporadic |
| Energy export destination shifts | IEA Russia energy tracker | Web | https://www.iea.org/countries/russia |

### Japan-specific
| Data | Source | Format | Notes |
|------|--------|--------|-------|
| Nuclear reactor restart timeline | IAEA PRIS | Web scrape | Site returns 503 intermittently |
| Historical energy import costs (¥) | METI (Japan Ministry of Economy) | PDF/Excel | Annual, 1970–present |

---

## STRATEGY RECOMMENDATION

### For the quantitative model (panel + VAR):
Use only automatically pullable data. This gives us:
- Full energy production/consumption profile (OWID, 1900–2024)
- GDP, trade, imports (World Bank)
- Macroeconomic controls (IMF DataMapper)
- Reserve currency shares (IMF COFER, 1999–present)

This is sufficient for the core panel regression and VAR.

### For the focal country case studies:
Supplement with manually collected data for the four key gaps:
1. EU ETS carbon price history (Sandbag/ICAP — free download)
2. SWIFT RMB monthly tracker (free PDF, manual extraction)
3. Bruegel Russia energy tracker (free web data)
4. Thorium reserve estimates (IAEA — point estimates, one-time lookup)

### What this means for the paper:
The quantitative model rests entirely on clean, reproducible, automated data.
The focal country narratives use supplementary manual data that enriches the
case studies without compromising model reproducibility.

---

## Manual Download Links

| Source | URL | What to download |
|--------|-----|-----------------|
| Sandbag EUA prices | https://sandbag.be/carbon-price-viewer/ | EUA price CSV 2008–2024 |
| ICAP price explorer | https://icapcarbonaction.com/en/ets-prices | EU ETS historical prices |
| SWIFT RMB tracker | https://www.swift.com/our-solutions/compliance-and-shared-services/business-intelligence/renminbi/rmb-tracker | Monthly PDF reports |
| Bruegel Russia tracker | https://www.bruegel.org/dataset/russian-fossil-fuel-tracker | Energy export data |
| IAEA PRIS | https://pris.iaea.org/PRIS/CountryStatistics | Japan/India/China nuclear capacity |
| India Atomic Minerals | https://amd.gov.in/thorium-resources | Thorium reserve estimates |
| IEA Russia | https://www.iea.org/countries/russia | Energy export destinations |
