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

*See separate explanation.*

Thorium presents four structural obstacles that rule out most ML:

1. **No historical training data.** No country has ever converted thorium reserves into monetary power. Supervised ML requires labeled outcomes to learn from. There are no labeled outcomes here — the causal chain (thorium endowment → nuclear deployment → energy sovereignty → monetary leverage) has never been observed end-to-end.

2. **Cross-section is too small.** TMPI covers ~12–15 countries. Even simple OLS is underpowered. ML with hyperparameters would overfit immediately and produce meaningless rankings.

3. **The key input is geological stock, not a dynamic process.** Thorium reserves don't change year to year. There is no time variation to exploit with sequence models (LSTM, transformer, BSTS over the thorium dimension). The data is fundamentally cross-sectional.

4. **Theory-driven ranking is the appropriate tool.** TMPI is deliberately a construct — reserves × nuclear capacity × institutional quality — because the outcome being predicted is a future state that doesn't yet exist. GP regression (recommended above) is appropriate precisely because it is principled about uncertainty over this construct. More aggressive ML would produce false precision from a near-empty data space.

The one ML extension that *could* add value for thorium is **transfer learning from uranium**: using the historical relationship between uranium endowment → nuclear energy share → balance-of-payments outcomes (for existing nuclear powers: France, USA, Canada) to construct empirical priors for thorium's analogous chain. This is speculative but theoretically grounded. It would function as an auxiliary validation of the TMPI weights rather than a replacement for the cross-sectional ranking.
