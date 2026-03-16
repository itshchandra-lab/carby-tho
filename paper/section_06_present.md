# §6 — The Present Register: Energy Position and Reserve Currency Status

## 6.1 Design and Honest Framing

The present register tests whether Net Energy Position predicts reserve currency share with a generational lag. The empirical strategy is structured case comparison with time-series corroboration — not econometric panel analysis in the sense of identifying treatment effects. This distinction matters and must be stated clearly.

With only six reserve currency entities over thirty years, the data cannot support the kind of causal identification that contemporary quantitative social science standards demand. What the data can support is structured case comparison: two cases moving in opposite directions on both the independent variable (energy position) and the dependent variable (reserve share), with a natural experiment providing the cleanest identification, and boundary conditions confirming the mechanism's scope. This is historical political economy with falsifiable predictions, which is the correct epistemological register for this question.

The entity-specific time-series analysis confirms a long-run relationship between energy position and reserve share for the two primary cases. The heterogeneity in slopes across entities — I² above 90% — confirms that pooling them into a single panel regression is inappropriate. Pooled results are reported in the appendix for transparency; they are not the paper's finding. The leave-one-out jackknife analysis reveals that removing the United States reverses the pooled coefficient from +84 to −3; the result is USA-driven and is treated as such throughout.

## 6.2 The Two Primary Cases

The United States case provides the clearest confirmation. American energy position rose through the shale revolution: NEP increased from 0.143 in 2010 to 0.166 in 2019 as domestic oil and gas production surged. Applied to the prediction of reserve share effects a decade later — the estimated generational lag — this predicts stabilisation of USD reserve share in the 2020s. USD reserve share had been declining steadily from 73% in 2001. Since 2021, it has stabilised in the 58.5–59.0% range, approximately ten years after peak shale output. This is consistent with the mechanism counteracting the diversification trend that would otherwise have continued.

The ARDL bounds test (Pesaran, Shin, and Smith 2001) confirms cointegration between US energy position and reserve share — meaning the two series share a stable long-run equilibrium relationship rather than moving independently. The long-run DOLS coefficient on NEP is positive and significant: β=84.0 (SE=37.89, 95% CI: [9.8, 158.2], lag 10, entity-specific DOLS; n_eff≈10 after DOLS lag structure). Each +0.01 improvement in net energy position predicts approximately +0.84 percentage points of reserve share over the subsequent decade. The confidence interval is wide, reflecting the small effective sample size at T≈30 with the DOLS lag structure; the directional finding is robust but the magnitude is imprecisely estimated. The robustness decomposition is reported in §6.8.

The eurozone case provides confirmation in the opposite direction. Eurozone energy position declined from approximately 0.010 in 1999 to 0.005 in 2024 as North Sea reserves depleted and import dependence rose. EUR reserve share peaked at 24% in 2009 and declined to 19% by 2024. The correlation between lagged energy position and reserve share is r=0.864 over sixteen overlapping observations.

An important caveat: both series are declining and persistent, meaning a high correlation is partly mechanical. The time-series cointegration analysis provides the appropriate inference, controlling for the non-stationary character of both series. An additional confound: the eurozone sovereign debt crisis of 2010 to 2015 caused compositional shifts in central bank reserves for institutional reasons entirely separate from energy position. The correlation is consistent with the mechanism but does not distinguish it cleanly from the debt crisis alternative. This limitation is stated directly.

![Figure 2](../outputs/figures/figure_2_present_register.png)

**Figure 2.** Net Energy Position and reserve currency share, USA (left) and eurozone (right). Reserve share on right axis (%), NEP on left axis. Lag-adjusted correlation reported in §6.2.

## 6.3 Japan: The Natural Experiment

Japan provides the cleanest identification in the paper. If energy position explains reserve currency share, then an exogenous shock to energy position — one that leaves all other standard predictors unchanged — should affect reserve share in the predicted direction.

The March 2011 Tōhoku earthquake and the subsequent Fukushima Daiichi nuclear disaster provided exactly this shock. Japan's nuclear fleet was progressively shut down, collapsing NEP from 0.0084 in 2010 to 0.0028 in 2012 — a 67% decline in two years. This shock was exogenous to the variables the standard reserve currency literature deploys. It was driven by a natural disaster and the subsequent regulatory response, not by monetary policy decisions, trade patterns, financial market conditions, or institutional quality.

Japan commands every predictor the standard literature would use to forecast reserve currency status: the world's third-largest GDP, deep and liquid financial markets, stable monetary institutions, and the Bank of Japan's long record of credibility. On GDP grounds, the yen should hold 10–15% of global reserves. It holds 5–6%. The standard predictors have not deteriorated. The energy mechanism predicts stagnation. The data match the energy mechanism.

The framework also generates a forward prediction from the Japan case. Official Japanese energy policy targets 20% nuclear capacity by 2035. As nuclear capacity is restored, NEP improves. The MPI predicts a gradual recovery in yen reserve share from approximately 2025 to 2030, conditional on nuclear restart proceeding as planned.

![Figure 3](../outputs/figures/figure_3_japan_fukushima.png)

**Figure 3.** Japan's Net Energy Position, 2005–2018. The 2011 Fukushima Daiichi shutdown provides a natural experiment in energy sovereignty loss, reducing Japan's NEP by 67% over 2010–2012 (0.0084 to 0.0028).

## 6.4 Boundary Conditions

**Switzerland** holds 0.2–0.3% of global reserves with essentially zero energy position. This is not a falsification of the mechanism. Switzerland is an institutional substitution case: financial entrepôt status and monetary credibility built over two centuries generate reserve demand independently of energy position. The mechanism's absence confirms its theoretical scope — it operates where governance contestability creates leverage surfaces, not where institutional substitution operates independently.

**China** entered COFER reporting fully only in 2016. China's energy position is approximately zero at world scale despite large absolute production volumes. The mechanism predicts that without a positive and rising energy position, China's path to reserve currency status runs through institutional quality and capital account opening rather than energy position — which is consistent with the observed trajectory of gradual renminbi internationalisation.

**GBP institutional premium.** The United Kingdom provides the clearest quantification of how much financial entrepôt status is worth independent of energy position. Under the pure energy mechanism (β=84.0 × NEP_UK_lag10, no entity intercept), the model predicts approximately 0.7–1.6 percentage points of COFER reserve share for GBP over 2015–2024, consistent with a declining North Sea energy position. Actual GBP reserve share is approximately 4.5–5.2% over the same period. The institutional premium — actual minus pure-mechanism prediction — averages 3.7 percentage points (range: 3.3–4.3pp). This quantifies the value of the City of London's entrepôt infrastructure as a reserve demand generator independent of energy position. The mechanism's scope conditions are satisfied: GBP's reserve share substantially exceeds what the energy mechanism alone would predict, which is the defining feature of an institutional substitution case rather than a mechanism failure.

**Scope conditions.** The energy-governance mechanism activates when three conditions hold simultaneously: (a) the state's energy position is material to its current account balance — petroleum and gas imports constitute a significant share of total import expenditure, creating a direct channel from energy prices to monetary credibility; (b) the governance regime allocating energy entitlements is politically contestable rather than rule-bound — GS > 1 is the measurable signature of this condition; and (c) no institutional substitute operates independently — the state lacks the offshore financial infrastructure that generates reserve demand through channels independent of energy position (cf. Switzerland, United Kingdom, which generate reserve demand through entrepôt status). The mechanism's scope conditions are falsified if a major energy-sovereign state achieves reserve status while failing conditions (a) or (b), or if a state with a strong energy position fails to achieve reserve traction despite satisfying all three conditions without the security orbit filter operating.

## 6.5 Russia: Two Mechanisms

Russia's 2022 case is the most visible contemporary demonstration of the energy-monetary mechanism, but two distinct causal mechanisms are operating simultaneously and must not be conflated.

**Mechanism A — the thesis mechanism** — concerns the structural energy corridor. Russia's pre-existing dominance in Eurasian energy supply chains made bilateral monetary corridor formation structurally viable when sanctions forced it. The ruble-yuan energy settlement relationship traced hydrocarbon supply routes that had existed for decades. The ruble-rupee corridor traced Indian refinery dependence on Russian crude that predated the 2022 sanctions. These corridors did not emerge from nothing in February 2022. They emerged from a pre-existing energy geography.

**Mechanism B — the GS mechanism** — concerns what the SWIFT exclusion and EU ETS expulsion revealed: that Western monetary and carbon infrastructure is political weaponry, not neutral mechanism. This confirms the backward register's claim that governance infrastructure is politically constructed and excludable by political decision. But Mechanism B does not independently support the thesis. Corridor formation under coercion is consistent with many theoretical frameworks.

The distinction is what keeps the thesis falsifiable. If energy geography had not preceded the coercion, the corridors could not have formed at this speed or scale.

An important asymmetry in the falsification logic: if corridors dissolve post-sanctions-lift, Mechanism B is confirmed and Mechanism A weakened — energy geography was necessary but coercion was sufficient. If corridors persist, this is consistent with Mechanism A (geography is load-bearing) but does not uniquely confirm it; network switching costs from corridor formation could produce persistence independently. The strongest evidence for Mechanism A would be bilateral energy invoicing outperforming non-energy bilateral INR-RUB settlement by a measurable margin — a test not yet possible with available data.

An important empirical qualification: of the INR-RUB energy trade corridor, approximately 5–10% is settled in INR; the majority remains in non-convertible holdback accounts. The corridor demonstrates route creation and Channel 1 activation (trade invoicing in a bilateral context), but monetary power translation through Channels 2 and 3 has not yet followed. Central bank reserve accumulation in rupees by the Russian central bank has been minimal. The corridor is real; the monetary leverage is not yet materialised. This is consistent with the sequencing logic in §3.4 — Channel 1 has activated, but without Channel 2 (asset recycling) and Channel 3 (credibility establishment), reserve status does not follow.

## 6.6 Lag Sensitivity

| Entity | λ=5 years | λ=8 years | λ=10 years | λ=12 years | λ=15 years |
|--------|-----------|-----------|------------|------------|------------|
| USA | Positive | Positive | Positive** | Positive | Positive |
| Euro Area | Negative | Negative* | Negative** | Negative* | Negative |
| Japan | Not sig. | Not sig. | Not sig. | Not sig. | Not sig. |
| United Kingdom | Not sig. | Not sig. | Not sig. | Not sig. | Not sig. |

(** significant at 5%; * significant at 10%) Statistical significance is concentrated in the two primary cases. Japan and United Kingdom display directional consistency but no statistically significant lag relationship at any specification — a finding consistent with the boundary condition logic of §6.4 but one the present register cannot resolve. The natural experiment in §6.3 carries the identification burden for the Japan case.

## 6.7 Historical Out-of-Sample Validation: The Sterling Case

The US and eurozone cases establish the mechanism within the COFER era (1995–2024). A second, independent test is available in a different era entirely: the sterling-dollar transition of the twentieth century, which was simultaneously the coal-oil transition. The data, the currency, the energy type, and the time period are all different from the present-register cases. If the mechanism holds here, it is not US-specific.

**Data.** UK energy production share (coal + oil + gas + nuclear, as share of world total) from OWID and BP Statistical Review, 1900–1980. Sterling reserve share from Eichengreen and Flandreau (2009), eight observations across 1899–1980. Lag structure: λ=10 years applied as in the present register (production share in year *t* matched to reserve share in year *t*+10). Pre-1965 UK consumption data is unavailable; production share serves as the energy position proxy for the coal era. This understates the NEP concept slightly — UK was a net exporter through the coal era, so production share is a conservative measure.

**Result.** The lag-adjusted Pearson correlation between UK production share and sterling reserve share across eleven matched observations is **r = 0.9507 (p < 0.001)**. The relationship is monotonically declining throughout: UK production share fell from 24.7% of world energy in 1913 to 2.2% in 1980; sterling reserve share fell from 48% to 5% over the same ten-year-lagged window.

| Year (reserve share) | Sterling share | UK prod share (t−10) |
|---------------------|---------------|----------------------|
| 1913 | 48% | 24.7% (1903) |
| 1925 | 42% | 19.5% (1915) |
| 1930 | 40% | 15.8% (1920) |
| 1950 | 35% | 10.5% (1940) |
| 1960 | 22% | 7.7% (1950) |
| 1970 | 10% | 4.1% (1960) |
| 1980 | 5% | 2.2% (1970) |

**The residual is theoretically informative.** The OLS fit systematically underpredicts sterling reserve share before 1970 — actual demand consistently exceeded what UK production share alone would generate. This residual is precisely what Schenk (2010) documents: oil royalty payments from Kuwait, Nigeria, and Saudi Arabia arrived in sterling under colonial-era contracts, sustaining reserve demand through institutional inertia well beyond Britain's energy position. When dollar oil invoicing replaced sterling in 1974, the institutional premium evaporated and reserve share converged to the mechanistic prediction. The over-prediction *before* 1974 and the convergence *after* 1974 are both consistent with the MPI framework: energy position sets the floor; institutional architecture can sustain demand above it until the governance arrangement is severed.

**What this adds.** The sterling case provides an out-of-sample historical validation that the mechanism operated in the coal era, in a different currency, measured by a different data source, with a different β environment. It confirms that the US DOLS coefficient (β=84.0) is not an artefact of the shale revolution — the same directional mechanism is visible across a century of UK coal data. The coefficient magnitude is not directly comparable (different units, different era, no consumption data pre-1965), but the directional validation and the r=0.9507 correlation support the mechanism's generalisability beyond a single US data point.

**Data source note.** Sterling reserve share data from Eichengreen and Flandreau (2009), Table 1 and Figure 1. UK energy production from OWID (sourced from BP Statistical Review of World Energy). Full annual series saved to `data/raw/sterling_historical.csv`.

## 6.8 Limitations

Six limitations bound the present register's claims.

**First, the quantitative finding is USA-driven.** The entity-specific ARDL result (β=84.0, SE=37.89, 95% CI: [9.8, 158.2], lag 10, entity-specific DOLS; n_eff≈10 after lag structure) is robust within the US case. The leave-one-out jackknife analysis — reported in full in the appendix — reveals that removing the United States reverses the pooled coefficient from +84 to −3. The panel finding, reported in the appendix for transparency, is 2/8 specifications significant. This paper's claims do not rest on the panel finding; they rest on the structured case comparison and natural experiment established in §6.2–§6.4. But the sensitivity to the single US observation must be stated directly: the quantitative result is a US result, applied with explicit qualification to the India forward prediction through the transmission chain in §7.5. The wide confidence interval on the DOLS coefficient reflects the small effective sample size (n_eff≈10) inherent in DOLS estimation at T≈30; the directional result is robust across specifications but the magnitude is imprecisely estimated.

**Second, EUA price data from Phase I (2005–2007) is an academic reconstruction.** Primary exchange data was not retained by the EU EUTL for this period. The backward register's GS calculation relies on Ellerman and Buchner (2008), Koch et al. (2014), and Bayer and Aklin (2020) to reconstruct Phase I prices. The CV=0.818 and GS=2.87 figures (monthly bootstrap; annual-price calculation yields GS=2.79, see note at §5.3) are as reliable as the underlying reconstruction. Bootstrapped confidence intervals on GS (1,000 resamples from 36 monthly Phase I observations) yield a 95% CI of [2.06, 4.28] — all substantially above 1.0, meaning the core claim (GS > 1, energy governance is politically constructed) is robust to resampling uncertainty. Readers who wish to challenge the GS result should begin with primary Phase I data from Sandbag's Carbon Price Viewer or the ICAP Allowance Price Explorer, if those sources have since archived the relevant series.

**Third, the Zivot-Andrews structural break test at T=20 cannot establish formal significance.** Bootstrapped empirical critical values (5,000 pure random walk simulations at T=20) yield an empirical 5% critical value of approximately −30.7 — far more extreme than the asymptotic −5.08. The observed statistic of −6.248 does not reach this empirical critical value, meaning the ZA result does not carry formal significance at T=20. The backward register's claim to have identified a structural break at 2014 rests on the documented political event and the GS=2.87 volatility ratio, not on formal ZA inference. The ZA test is used solely to confirm the break location matches the politically-documented event, which it does; the formal significance claim is withdrawn.

**Fourth, China's COFER data begins in 2016Q4** when China commenced reporting to the IMF. The apparent rise in CNY reserve allocation since 2016 reflects reporting inclusion as well as new demand — these cannot be separated within the COFER data alone. Prior to 2016, Chinese renminbi reserves were recorded in the COFER "unallocated" category rather than absent from the global system; the 2016 change made some existing reserve demand visible, not only created new demand. This creates a structural break in CNY reserve share data unrelated to energy governance, and any analysis of China's reserve currency trajectory using COFER must be confined to post-2016 data or supplemented with PBOC balance-sheet data.

**Fifth, Granger causality tests for China, India, and Russia fail due to insufficient COFER data** rather than absence of causal relationship. These entities lack the minimum observation count required for reliable Granger test inference. The paper does not claim Granger causality for these countries and does not rest empirical weight on those tests.

**Sixth, the β coefficient is estimated from COFER reserve share data but applied to predict BIS FX turnover share.** These track different populations: COFER measures official central bank reserve holdings; BIS FX turnover measures private foreign exchange market activity. The relationship between them varies by currency (GBP: 4.5% COFER / 13% BIS; JPY: 5.7% / 8%; USD: 58.5% / 44%). Applying β estimated from the COFER regression to a BIS turnover prediction is a first approximation that understates model uncertainty. A direct BIS turnover regression would require sufficient observations from currencies that have gained reserve status from low baselines — a sample that does not yet exist. The India prediction should be read as indicating the direction and order of magnitude of BIS share gains rather than a precise quantitative point estimate. An additional COFER methodology caveat applies throughout: COFER measures *shares* of allocated reserves, not total reserve demand in absolute terms. A currency's COFER share can rise passively as other currencies' shares decline, without any new demand being generated for that currency specifically. The India prediction requires active new reserve demand, not merely passive share gain from dollar/euro retreat.

---
