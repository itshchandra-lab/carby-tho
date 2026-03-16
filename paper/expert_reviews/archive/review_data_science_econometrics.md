# Expert Review: Data Science / Econometrics
**Reviewer profile:** Top-1% applied econometrician; publications in Journal of Applied Econometrics, Econometric Reviews; expertise in time-series econometrics, structural break testing, cointegration, small-sample inference.
**Standard applied:** Journal of Applied Econometrics technical referee

---

## VERDICT: Working paper, not ready for peer review — quantitative apparatus has severe problems

---

## DISPOSITION (2026-03-16)

| # | Concern | Status | Note |
|---|---------|--------|------|
| 1 | ARDL at T≈30 — asymptotic critical values unreliable | ✓ ADDRESSED | ARDL demoted to directional evidence only; §6.8 explicitly withdraws formal inferential weight; paper relies on structured case comparison, not bounds-test inference |
| 2 | ZA at T=20 — small-sample critical value problem | ✓ ADDRESSED | Bootstrapped empirical CV = −30.7 (5,000 simulations at T=20); observed −6.248 does not reach it; formal ZA significance withdrawn in §6.8 |
| 3 | β=84.0 — no standard error or CI reported | ✓ ADDRESSED | β=84.0 (SE=37.89, 95% CI [9.8, 158.2]) now in §6.2 and §6.8; wide CI and n_eff≈10 explicitly disclosed |
| 4 | LOO jackknife sign-flip — coefficient USA-driven | ✓ ADDRESSED | §6.8 explicitly: "quantitative result is a US result"; India forward prediction framed as conditional scenario, not structural extrapolation from β |
| 5 | GS=2.79 — no CI on CV estimates; oil denominator | ✓ ADDRESSED / PUSH BACK | GS bootstrapped 95% CI [2.06, 4.28] in §6.8 — all above 1.0. Oil denominator: **PUSH BACK** — GS measures political construction of carbon governance relative to commodity markets; RGGI is the well-functioning baseline the EU ETS failed to resemble, which is the point; using RGGI would eliminate the contrast that makes GS informative |
| 6 | TMPI weights ad hoc — no sensitivity analysis | ✓ ADDRESSED | Weight sensitivity across four schemes (reserves-heavy, capacity-heavy, institutions-heavy, equal) in §7.7. Result is NOT invariant — India drops out under capacity-heavy weighting and enters second under reserves-heavy. This is disclosed directly in the paper: India's binding constraint IS nuclear capacity deployment, and the sensitivity reflects that actual empirical situation. The concern is addressed because the paper honestly maps where the result holds and where it doesn't, rather than claiming false robustness. Cross-reference added to §7.2. |
| 7 | WGI composite not ideal for nuclear capacity | PUSH BACK | WGI is standard in IPE and the paper discloses its limitations explicitly; TMPI rankings are driven by thorium reserves and nuclear share, not WGI noise; the sensitivity analysis (§7.7) shows WGI variation does not shift top-3 ranking — the binding constraint is nuclear capacity, not institutional quality measurement error |

**RETIREMENT STATUS:** ✓ RETIRED — all material concerns addressed or adjudicated with documented reasoning

---

## 1. ARDL Bounds Testing at T≈30

The paper runs ARDL on the US case with approximately 30 annual observations to test cointegration between energy position and reserve share. This is deeply problematic.

Pesaran-Shin-Smith (2001) derived critical values for T=500–5000. At T=30, the test is severely undersized. The critical value table in PSS shows that at T=25, size distortions can exceed 15–20% depending on model specification. The paper's one caveat — "the sample size caveat deserves transparency" — is insufficient.

The correct statement is: *At T≈30 with a lag structure, the bounds test is essentially uninterpretable.* The asymptotic critical values are unreliable. No bootstrap or small-sample correction is reported. The paper cites the −6.248 statistic against a critical value of −5.57 as sufficient margin for "minor size corrections," but PSS critical values at T=30 are not known — this is a claim without empirical support.

**Verdict:** The ARDL result should be flagged as directional evidence only, with no inferential weight attached. The true relevance of US energy position cannot be adjudicated through this test at this sample size.

---

## 2. Zivot-Andrews at T=20

The backward register applies the ZA test to 20 annual EUA price observations (2005–2024), identifying 2014 as a structural break. The caveat in §6.8 states the asymptotic critical values were derived for larger samples. This understates the problem.

ZA has extremely poor small-sample behaviour. Perron (1997) and Vogelsang-Perron (2006) demonstrate that at T=20, the ZA test can have size inflation above 20%. The empirical critical value at T=20 may be several units more negative than the tabulated asymptotic value of −5.57. The reported statistic of −6.248 might not exceed even the correct small-sample critical value.

Critically, ZA is designed to test *whether* a break exists, not *when*. Applied post-hoc to a known event (Phase III MSR reform in 2014), the test is vulnerable to look-ahead bias. The paper acknowledges "researchers cannot choose the break date after observing the data" but then applies ZA to 20 observations spanning exactly the period when the reform occurred. This is a test run on data where you already know the answer.

**Verdict:** Either bootstrap the critical value on the actual sample size, or acknowledge that the test is purely narrative support — not formal statistical evidence — for the 2014 break.

---

## 3. The β=84.0 Coefficient

The paper reports a DOLS estimate of β=84.0 with lag=10. This specification is indefensible as presented.

NEP ranges from approximately 0.005 to 0.166 (euro and US cases respectively) — a range of 0.161. The coefficient β=84.0 implies that moving across the full empirical range of NEP (a change of 0.161) would shift reserve share by 13.4 percentage points. The US reserve share ranges from roughly 58–73%, so the NEP coefficient is projecting economically implausible sensitivity.

More fundamentally: with T≈30 and a lag structure of ±10 lags in DOLS, the effective degrees of freedom collapse to approximately 10–12. A coefficient of 84.0 at this effective n is a point estimate with enormous uncertainty. **No standard error or confidence interval is reported.** The paper states β=84.0 as fact, but at n_eff≈10, the 95% CI likely spans from negative to >200.

The "robustness decomposition" promised in §6.8 is not provided in the text. The main paper gives no uncertainty quantification on the result the entire forward prediction (India's transmission chain) depends on.

**Verdict:** Report the standard error. At n_eff≈10, the coefficient is too noisy to carry quantitative weight. Reframe as directional evidence, not a point estimate for counterfactual simulation.

---

## 4. Leave-One-Out Jackknife: The Sign-Flip Problem

The paper discloses that dropping the US reverses the pooled coefficient from +84 to −3. The response in §6.8 is: "The quantitative result is a US result, applied with explicit qualification to the India forward prediction."

This is not adequate. A sign-flip under jackknife deletion is not a "robustness issue" — it indicates the paper has not identified a mechanism, it has identified a data point. If the finding holds only because one observation is extreme, the causal claim fails.

The paper claims its forward claims rest on "structured case comparison and natural experiment established in §6.2–§6.4." But the India forward prediction in §7 *explicitly relies on* the quantitative magnitude of β=84.0: "the NEP improvement over the 2025–2035 period is large enough to produce the predicted FX share change under the model."

This is a counterfactual simulation using β=84.0. If that coefficient is USA-driven and reverses sign when the USA is removed, the forward prediction is US-fitted extrapolation — not a structural prediction.

**Verdict:** The paper should acknowledge: "We have identified a strong energy-position mechanism in the United States and found directional consistency in the eurozone. The quantitative magnitude cannot be generalized beyond these cases, and the India forward prediction is a conditional scenario *if* the US mechanism generalises."

---

## 5. Governance Sensitivity (GS=2.79)

The paper calculates GS as CV(EUA Phase I) / CV(Oil) = 0.815 / 0.292 = 2.79. Two problems:

**First:** EUA Phase I prices (2005–2007) are reconstructed from academic sources. No confidence intervals are provided on the CV estimate. If CV(EUA) has a true 95% CI of [0.65, 1.0], then GS ranges from 2.2 to 3.4. This uncertainty is not propagated.

**Second:** Using Brent crude as the denominator is problematic. RGGI is explicitly offered as an alternative (CV=0.047, GS ratio of 0.16), implying that *different carbon regimes* produce different governance sensitivities. Using Brent crude as the baseline conflates governance regime quality with commodity market volatility. Oil markets have their own governance structure (OPEC, geopolitical risk premia). A more defensible baseline is RGGI Phase I (a functioning carbon market), not oil.

**Verdict:** Report confidence intervals on CV estimates. Clarify whether GS measures (a) the EU ETS's inefficiency relative to a functioning carbon market, or (b) relative volatility of carbon vs oil. These are different claims requiring different baselines.

---

## 6. TMPI Construction

The TMPI formula combines thorium reserve share × nuclear share of energy × institutional quality (WGI composite). Several problems:

- **Weights:** The three components are multiplied with equal implicit weight (coefficient of 1 on each). This is ad hoc. No economic theory or calibration justifies equal weights.

- **Institutional quality measure:** WGI composite (unweighted average of six dimensions) treats "rule of law" and "voice and accountability" as equally relevant to nuclear fuel-cycle autonomy. A state with poor governance but independent nuclear technical capacity (e.g., China) may convert reserves faster than a state with good governance but no indigenous reactor design.

- **Static vs. time-varying:** India's TMPI uses 2024 nuclear share (3.2%), not the policy target (20% by 2035). The index is static. A time-varying TMPI forward projection would be more appropriate for generating trajectories.

- **No peer review:** The TMPI appears ad hoc to this paper. No external validation or robustness to alternative weightings is reported.

**Verdict:** The TMPI is a useful conceptual tool but insufficient for quantitative predictions. Sensitivity analysis over alternative weights is required.

---

## 7. Top Three Data/Methods Problems

**1. Identification failure at n_eff≈10.** The DOLS coefficient of 84.0 is too noisy to carry quantitative weight, and the jackknife sign-flip reveals USA-dependence. The forward prediction is circular: it uses a coefficient not robust beyond the US case.

**2. Small-sample tests reported without correction.** ARDL at T≈30 and ZA at T=20 are statistically underpowered. Critical values are known to be unreliable at these sizes. Label these as narrative support, not formal tests, unless bootstrapped.

**3. GS denominator conflates governance regime failure with commodity volatility.** Using Brent crude as the baseline for the EU ETS's governance quality is economically incoherent. Use RGGI or a constructed "well-functioning carbon market" baseline.

---

**Recommendation:** Apply bootstrap small-sample critical values to ARDL and ZA. Report standard errors and confidence intervals on all coefficients and derived quantities. Reframe the India prediction as a scenario *conditional on* US-mechanism generalisation. Justify TMPI weights or show robustness to alternatives.

*The paper's greatest strength — the structured case comparison (US positive, eurozone negative, Japan natural experiment) — does not require defeating small-sample asymptotics. Lead with that and demote the quantitative results to supporting evidence rather than the load-bearing wall.*
