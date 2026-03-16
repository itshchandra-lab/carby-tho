# ML Applications for The Carbon-Thorium Standard
*Internal memo | 2026-03-16*

---

## Bottom Line

The paper's econometric foundation is already sophisticated and appropriate for its data constraints. ML is not a replacement — it's a targeted amplifier at three specific points where current methods leave credibility gaps.

---

## The Binding Constraint

**N=6 reserve currencies.** Most ML methods need N in the hundreds. This rules out neural networks, random forests, and gradient boosting for the panel itself — you'd be fitting noise and reviewers will know it. Any ML application here must work *around* this by either (a) operating on the time dimension only, or (b) working on the larger cross-sections in the data (12–15 countries in TMPI, 20-year ETS price series).

---

## High-Value Recommendations

### 1. Hidden Markov Models — Backward Register

**What:** HMM learns the number of volatility regimes and their dates from the EUA price series alone, without imposing the ETS phase structure exogenously.

**Why it helps:** Zivot-Andrews and Bai-Perron tests find breaks but require specifying the model structure. If HMM endogenously recovers breaks near 2007 and 2014, it is powerful data-driven validation of the GS finding. If it recovers different breaks, that is equally informative — it shows where political construction of the regime diverges from data patterns.

**Data constraint:** Operates purely on the time series (T≈20 years of EUA prices). N=6 is not a binding constraint here.

**Implementation:** `hmmlearn` (Python) or `depmixS4` (R). Two-state and three-state models; compare via BIC.

---

### 2. Double Machine Learning — Present Register (Causal Identification)

**What:** DML (Chernozhukov et al. 2018, *Econometrica*) uses LASSO/ridge to select high-dimensional controls without inflating standard errors, providing a semi-parametric causal estimate of NEP → reserve share.

**Why it helps:** The Bartik IV has a contestable exclusion restriction. DML with entity-level residualization would directly address the USA-driven concern — it isolates whether NEP→reserve share holds after partialling out USA's disproportionate influence. It does not require specifying the functional form of nuisance parameters.

**Caveat:** Most demanding implementation given N=6. Works better with the longer time dimension. Best suited for a revision round.

**Implementation:** `DoubleML` (Python/R). Use LASSO for nuisance estimation; cross-fit with leave-one-entity-out folds.

---

### 3. Gaussian Process Regression — Forward Register (TMPI)

**What:** GP regression over the TMPI cross-section (~12–15 countries), replacing OLS on log-transformed reserves × nuclear share × WGI.

**Why it helps:** Provides a calibrated uncertainty surface over the ranking space, handles non-linearity in the thorium→monetary power conversion. Critically, allows formal quantification of whether India's ranking is genuinely *discontinuous* from the next-ranked country (USA=100, IND=15.8) or within estimation uncertainty. That discontinuity claim is central to the paper's forward predictions.

**Implementation:** `GPy` or `scikit-learn GaussianProcessRegressor`. RBF kernel; fit on thorium reserve mass, nuclear share, WGI composite.

---

### 4. Bayesian Structural Time Series — Forward Register (11 Predictions)

**What:** BSTS replaces CAGR-based forward projections with full posterior distributions over trajectories, with uncertainty bands that widen appropriately as the prediction horizon extends toward 2037.

**Why it helps:** Enables formal probability statements rather than point estimates: *"P(INR FX turnover > 3% by 2031) = 0.34 under base scenario."* This is a much stronger stake in the ground for the falsificationist framing than a CAGR band.

**Implementation:** `tfp.sts` (TensorFlow Probability) or `bsts` (R). Include structural breaks as known changepoints; use three scenarios (Low/Base/High) as separate model runs.

---

## Medium Value

### 5. Synthetic Control — Japan Fukushima (Present Register)

**What:** Synthetic control (Abadie et al. 2010, *JASA*) constructs a counterfactual Japan from a weighted combination of other countries that matched Japan's NEP trajectory before 2011.

**Why it helps:** The current pre/post comparison for Fukushima is descriptively compelling but identification is loose. Synthetic Japan tightens it considerably. This is standard practice in political economy journals and reviewers will expect it for a natural experiment claim of this magnitude.

**Implementation:** `Synth` (R) or `pysynth` (Python). Donor pool: USA, Germany, France, Canada. Match on NEP, GDP per capita, trade openness, 2001–2010.

---

## What to Avoid

| Method | Why |
|---|---|
| Neural networks / deep learning | N too small; uninterpretable to IR/geoeconomics audience |
| Gradient boosting for panel | ML-washing risk; no genuine advantage over ARDL/ECM at N=6 |
| LLM-based policy sentiment indices | Tangential to core causal claims; would distract the paper |
| Any black-box method | Audience requires auditable inference with tractable standard errors |

---

## Priority Order

| Priority | Method | Register | Rationale |
|---|---|---|---|
| 1 | **HMM** | Backward | Data-driven validation of GS; easy to implement; strong rhetorical payoff |
| 2 | **BSTS** | Forward (predictions) | Converts point estimates to calibrated probabilities; supports falsificationist framing |
| 3 | **Synthetic Control** | Present (Japan) | Clean natural experiment; expected by reviewers in political economy |
| 4 | **DML** | Present (causal) | Strongest methodological contribution; addresses USA-driven concern; hardest to implement |
| 5 | **GP Regression** | Forward (TMPI) | Formalizes India discontinuity claim; N is manageable |

---

## Framing Principle

None of these replace the existing econometrics — they sit alongside them as robustness and uncertainty-quantification layers. Present ML as *validation and uncertainty quantification*, not as the primary identification strategy. That framing is essential for credibility with both economics and IR reviewers.

---

## Why Not More ML for Thorium Specifically?

Thorium presents four structural obstacles that rule out most ML approaches:

**1. No labeled training data exists.**
Supervised ML learns from historical outcomes. No country has ever converted thorium reserves into monetary power — the full causal chain (thorium endowment → nuclear deployment → energy sovereignty → reserve currency leverage) has never been observed end-to-end. There is nothing to train on. You'd be building a model with zero positive examples of the thing you're predicting.

**2. The cross-section is fatally small.**
TMPI covers 12–15 countries. Even OLS is underpowered. Any ML model with tunable hyperparameters would overfit immediately and produce rankings that are pure noise dressed as precision. The curse of dimensionality runs in reverse here — you have more potential features (reserves, nuclear share, WGI, deployment pathway, capital account openness) than observations.

**3. The input is a geological stock, not a dynamic process.**
Thorium reserves don't move year to year. There is no time variation to exploit with sequence models — no LSTM, no transformer, no BSTS over the thorium dimension makes sense. The data is irreducibly cross-sectional, which eliminates the entire class of methods where ML genuinely outperforms econometrics.

**4. The construct is doing theoretical work, not empirical work.**
TMPI is deliberately a *measurement instrument* for a future state that doesn't yet exist. The appropriate tool for that is a theoretically grounded index with calibrated uncertainty — which is exactly what GP regression gives you. More aggressive ML would produce false precision from a near-empty data space, which is worse than transparent index construction.

**The one legitimate ML extension for thorium** would be *transfer learning from uranium*: use the historical relationship between uranium endowment → nuclear energy share → balance-of-payments outcomes (observed for France, USA, Canada) to build empirical priors for thorium's analogous chain. This would function as an auxiliary validation of TMPI weights, not a replacement for the cross-sectional ranking. It is speculative but theoretically defensible — uranium and thorium are close substitutes in the fuel cycle and the institutional conversion logic is identical.

---

## Carbon-as-Material: A New Dimension Where ML Becomes Tractable

### The Conceptual Extension

Carbon does not exit the monetary-power story when fossil fuels do. It re-enters as a *material input* — graphene, carbon fiber, carbon nanotubes, carbon black, synthetic diamond, CCU-derived chemical feedstocks — powering advanced manufacturing, aerospace, semiconductors, composites, and green infrastructure. Thorium-era energy doesn't replace carbon; it *powers the industries that process carbon as a strategic material*.

The carbon-thorium nexus is therefore not sequential (carbon era, then thorium era) but **layered**: thorium energy enables carbon-material dominance, which is the actual source of monetary leverage in the 2040–2060 timeframe. The current forward register treats thorium energy as the terminal output. This extension treats it as an *intermediate input* — cheap thorium-powered electricity enables energy-intensive carbon-material processing (graphene synthesis, carbon fiber autoclaving, DAC-to-feedstock conversion) at competitive scale.

This is theoretically a deepening of the forward register's GS term: in the material era, governance sensitivity is measured not over energy allocation rules but over *carbon-material market governance* — export controls on graphite, trade policy on carbon fiber precursors, IP regimes over graphene production processes.

### Why ML Constraints Don't Apply Here

The three obstacles that blocked ML for thorium-as-energy are absent here:

| Constraint | Thorium-as-energy | Carbon-as-material |
|---|---|---|
| Training data | None — outcome never observed | Decade-long price/trade series for carbon fiber, graphene, carbon black |
| Sample size | N=12–15 countries | N=100+ countries in trade data; thousands of patent records |
| Time variation | Geological stocks don't move | Dynamic markets with supply shocks, policy events, tech adoption cycles |

---

### ML Applications for the Carbon-Material Dimension

#### 1. NLP / Patent Analysis — Knowledge Structure Mapping

**What:** Apply ML over patent corpora (USPTO, EPO, WIPO) tagged to graphene, carbon nanotube, carbon fiber, and CCU technologies. Track geographic concentration of carbon-material innovation over time using topic modelling (LDA) and citation network analysis.

**Why it matters:** This directly operationalizes Strange's *knowledge structure* for the carbon-material era. Which countries hold the IP moats that convert material endowment into durable industrial leverage? China's graphene patent share vs. USA vs. EU is already geopolitically loaded; ML can track its trajectory and flag when concentration crosses thresholds that imply structural chokepoint control.

**Data:** Google Patents, WIPO PatStat, Lens.org. All open-access with API access.

**Implementation:** `spaCy` + `BERTopic` for patent classification; `networkx` for citation graph centrality. Time-window the corpus by filing year to produce a panel of innovation concentration indices.

---

#### 2. Graph Neural Networks on Input-Output Tables — Supply Chain Chokepoint Detection

**What:** Apply GNNs to World Input-Output Database (WIOD) or OECD TiVA tables to identify which countries sit at *chokepoints* in the carbon-material supply chain — controlling precursor feedstocks (acrylonitrile for carbon fiber, methane for graphene CVD), processing capacity, or end-use manufacturing.

**Why it matters:** Countries at network chokepoints have leverage; countries at the periphery have exposure. This is the material-era analogue to your GS measure: instead of measuring political construction of energy governance, you're measuring structural dependency in material production networks. A country that controls acrylonitrile supply to the global carbon fiber industry has a coercive lever analogous to Saudi Arabia's control of oil invoicing.

**Implementation:** `PyTorch Geometric`. Nodes = country-sector pairs; edges = value-added flows. Node embedding captures centrality; GNN learns which structural positions predict trade leverage (measured against historical export restriction events as ground truth).

---

#### 3. Demand Forecasting Under Transition Scenarios — Carbon-Material-Energy Nexus

**What:** LSTM or gradient boosting on carbon-material demand (carbon fiber in wind turbine blades, graphene in EV battery anodes, carbon black in tire manufacturing, carbon composites in aerospace) as a function of energy transition speed, industrial output, and technology adoption rates.

**Why it matters:** Run this under your three transition scenarios (Low/Base/High thorium deployment). The output shows how carbon-material demand evolves differently depending on which countries have access to cheap thorium-powered electricity for energy-intensive processing. Countries with both thorium energy and carbon-material processing capacity occupy a double structural advantage that the current TMPI does not capture.

**Data:** IEA material demand projections, USGS mineral commodity data, BloombergNEF technology adoption curves.

**Implementation:** `LightGBM` with scenario-indexed features; uncertainty quantification via quantile regression. Three scenario runs feed directly into the existing Low/Base/High framework.

---

#### 4. HMM on Carbon-Material Price Series — Material-Era GS Analogue

**What:** Parallel to the ETS backward-register analysis: run HMM on graphene spot prices, carbon fiber contract prices, and carbon black indices to detect volatility regime shifts.

**Why it matters:** If those regimes correlate with trade policy events (US-China tech decoupling, EU Critical Raw Materials Act, export controls on graphite), you have a material-era GS measure — quantifying how politically constructed carbon-material markets are, relative to a physical commodity benchmark. This extends the paper's core GS logic from energy governance to material governance, connecting backward and forward registers through a common measurement framework.

**Implementation:** `hmmlearn` (same toolkit as backward-register HMM). Two-state and three-state models on monthly price series; BIC model selection; overlay regime dates against policy event timeline.

---

#### 5. Synthetic Control for CCU Policy Experiments

**What:** When a country launches a major direct air capture or carbon utilization programme (Norway Longship, USA IRA §45Q provisions, EU Innovation Fund DAC projects), synthetic control estimates the effect on downstream carbon-material industrial output.

**Why it matters:** Builds empirical evidence for the transmission chain: thorium energy → cheap electricity → DAC/CCU at scale → carbon-material feedstock production → manufacturing monetary leverage. Each policy experiment is a natural experiment in the material-energy nexus. Synthetic control makes the identification credible.

**Implementation:** `Synth` (R). Outcome: carbon-material manufacturing value added as % of GDP. Donor pool: comparable economies without the policy. Match on pre-period industrial structure, energy prices, trade openness.

---

### Theoretical Implication for the MPI

If this extension holds, the MPI forward state needs a second term alongside TMPI:

```
Forward state = TMPI_i · GS_energy_{i,t+τ}  +  CMPI_i · GS_material_{i,t+τ}
```

Where **CMPI** (Carbon Material Power Index) captures a country's position in carbon-material supply chains — precursor control, processing capacity, IP concentration, end-use manufacturing depth — and **GS_material** measures the political construction of carbon-material governance regimes (export controls, IP enforcement, standards-setting power).

Countries that score high on both TMPI and CMPI — thorium-rich AND carbon-material-capable — occupy the structural sweet spot for the 2040–2060 monetary order. The preliminary answer on current data: **USA, India, China**. The governance sensitivity term then determines which of these converts structural position into durable monetary leverage — a question where the existing GS framework applies directly.

### Priority Order for Carbon-Material ML

| Priority | Method | What It Establishes |
|---|---|---|
| 1 | **Patent NLP** | Knowledge structure concentration; Strange's fourth pillar operationalized |
| 2 | **HMM on material prices** | Material-era GS measure; connects to existing backward-register framework |
| 3 | **GNN on IO tables** | Supply chain chokepoint map; identifies leverage positions |
| 4 | **Demand forecasting (LSTM/GBM)** | Scenario-linked carbon-material demand; feeds existing Low/Base/High structure |
| 5 | **Synthetic control (CCU)** | Empirical evidence for energy→material→monetary transmission chain |
