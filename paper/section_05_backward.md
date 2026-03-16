# §5 — The Backward Register: Energy Governance Is Politically Constructed

## 5.1 The Claim

The MPI framework's first premise is that energy governance regimes are politically constructed rather than geologically determined. If this is wrong — if energy allocation merely tracked commodity fundamentals — then energy position would be an exogenous endowment, and the entire framework would reduce to a claim that geology predicts monetary power. That is not the argument. The argument is that states choose their energy positions through governance, and that the political contestability of those governance regimes is itself measurable.

The EU Emissions Trading System is the test case. It is the world's largest carbon market and the most documented case of an energy governance regime whose allocation rules were explicitly negotiated through political processes. The question is not whether the EU ETS was politically contested — that is well established in the literature. The question is whether that political construction is visible quantitatively in the price series.

## 5.2 The Structural Break

The Zivot-Andrews (1992) endogenous structural break test identifies whether a time series contains a single large break — a point where the underlying relationship changes — without requiring the researcher to specify in advance when that break occurred. Applied to the EU ETS allocation surplus series from 2005 to 2024, the test identifies 2014 as the break year (ZA statistic = −6.248; note: at T=20 asymptotic p-values are unreliable — see §6.8).

The break aligns with the Phase III structural reform of the EU ETS, which introduced the Market Stability Reserve mechanism — a political decision negotiated over 2013 to 2015 that fundamentally altered the allocation rules. The test rejected two alternative break years that would have undermined the interpretation: 2008 to 2009 (when the global financial crisis reduced verified emissions) and 2019 to 2020 (COVID lockdowns). Both would have indicated the series responds to macroeconomic fundamentals rather than political governance decisions. Neither was identified.

**Bai-Perron multiple break robustness.** The Zivot-Andrews test assumes a single structural break. Applied to the EUA price series (rather than the allocation surplus), Bai-Perron sequential break detection identifies 2021 as the dominant price-series break (F=122.4), with a secondary break at 2018 (F(2|1)=5.5). The 2021 break corresponds to the Fit for 55 regulatory surge that drove prices from ~€25 to ~€80. These findings are complementary: the allocation surplus series captures the 2014 governance reform (ZA break); the price series captures the 2021 demand shock. Both are politically-documented events, both confirm the mechanism that ETS dynamics are governance-driven rather than commodity-driven. The 2021 price break does not compete with the 2014 allocation break; they operate on different variables.

**Small-sample caveat — formal significance cannot be claimed.** The test runs on twenty annual observations. Bootstrapped empirical critical values at T=20 (5,000 pure random walk simulations) yield an empirical 5% critical value of approximately −30.7 and an empirical 1% critical value of approximately −77.1 — far more extreme than the asymptotic values of −5.08 and −5.57. The observed statistic of −6.248 does not reach either empirical critical value, meaning formal statistical significance at conventional levels cannot be claimed at this sample size. The ZA result is therefore treated not as an independent statistical finding but as corroboration of the politically-documented break at 2014: the test identifies the break in the correct location relative to the documented governance event, which is the evidentiary use made of it. The backward register's quantitative claim rests on the GS=2.87 volatility ratio — not on the formal ZA inference.

## 5.3 Price Volatility: The Quantitative Signature of Political Construction

The Governance Sensitivity measure requires a second piece of evidence: not just that the allocation surplus breaks at a political event, but that the resulting carbon price is more volatile than the underlying physical commodity it nominally governs. The coefficient of variation — the ratio of standard deviation to mean, a measure of relative volatility — provides this comparison.

| Series | Period | CV (volatility) | Ratio to Oil |
|--------|--------|-----------------|--------------|
| Brent crude oil | 2005–2024 | 0.292 | 1.00 (baseline) |
| RGGI allowances (US carbon) | 2009–2012 | 0.047 | 0.16 |
| EU ETS Phase I (European carbon) | 2005–2007 | 0.818 | 2.87 |

The RGGI comparison is the most informative finding in the backward register. RGGI — the Regional Greenhouse Gas Initiative, a northeastern US carbon market — and EU ETS Phase I are the same asset class: synthetic carbon permits, both in their first compliance period, both facing similar initial over-allocation problems. RGGI Phase I was more stable than the oil market itself, with a CV of 0.047 against oil's 0.292. EU ETS Phase I was nearly three times more volatile than oil and seventeen times more volatile than RGGI.

The difference cannot be attributed to the asset class. Both are synthetic carbon permits. It is attributable to the EU's politically constructed allocation rules. EU member states lobbied aggressively for generous permit allocations; the resulting over-allocation was so severe that when it became transparent in May 2006 — when the first actual emissions data was released — prices collapsed from approximately €30 per tonne to near-zero within weeks. No commodity with a fixed physical supply exhibits a near-total price collapse driven by a political accounting revelation. This is what GS significantly greater than 1 looks like.

The Governance Sensitivity score for the EU ETS Phase I regime:

```
GS = CV(EUA Phase I monthly) / CV(Oil 2005–2024) = 0.818 / 0.285 ≈ 2.87
    (bootstrapped 95% CI: [2.06, 4.28]; annual-price calculation: 0.815/0.292 ≈ 2.79)
```

This means the EU carbon governance regime was approximately 2.8–2.9 times more politically constructed than the underlying commodity market. The bootstrapped confidence interval excludes 1.0 at its lower bound, confirming GS > 1 regardless of resampling variation. Normalised for use in the MPI assembly: GS_norm ≈ 0.85.

![Figure 1](../outputs/figures/figure_1_ets_break.png)

**Figure 1.** EU ETS annual carbon price, 2005–2024. The Zivot-Andrews structural break test identifies 2014 as the break year (ZA stat = −6.248; asymptotic p-value unreliable at T=20 — see §6.8), coinciding with the Phase III Market Stability Reserve reform.

## 5.4 What the Backward Register Proves

Three claims are established. First, the allocation surplus breaks at a political event — Phase III reform — not a supply shock or macroeconomic development. Second, EU ETS price volatility substantially exceeds both the commodity benchmark and the RGGI equivalent, confirming that GS greater than 1 is real and measurable. Third, a governance regime with GS of this magnitude cannot function as a credible rule-based allocator. Political incumbents will renegotiate the allocation rules whenever they impose material costs.

Three claims are not established. The backward register does not prove intentional capture by identifiable actors. It does not prove that all energy governance exhibits GS greater than 1 — the RGGI finding demonstrates the same asset class can be governed with far lower political sensitivity. And it does not test whether the EU carbon era produced monetary outcomes — the ETS is too young and the sample too small for a monetary test. That is what the present register is for.

---
