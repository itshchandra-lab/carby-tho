# Peer Review — Carbon Science and Policy Expert
## "The Carbon-Thorium Standard: Energy-Backed Currencies and the Architecture of Monetary Failure in a Multipolar World"

**Reviewer specialisation:** Emissions trading system design and carbon market governance
**Journal:** *Climate Policy* / *Energy Policy*
**Recommendation:** Major Revisions Required
**Score:** 4/10

---

## Prefatory Note

This is a technically ambitious paper that deploys carbon market evidence as an empirical foundation for a broader monetary architecture argument. The ambition is commendable. The EU ETS analysis in §5 contains genuine insights — the over-allocation story is real, the Phase I collapse is real, the MSR reform story is real. But the technical execution of the backward register has four serious problems that must be corrected before the argument can bear the weight the paper asks it to carry.

---

## 1. The EUA Price Reconstruction: Source Reliability and Archival Gaps

The paper cites Ellerman and Buchner (2008), Koch et al. (2014), and Bayer and Aklin (2020) as sources for Phase I EUA price reconstruction. This tripartite citation creates a misleading impression of independent corroboration.

**Ellerman and Buchner (2008)** is a foundational institutional analysis of Phase I, but it is not a primary price data source. Ellerman and Buchner report price series they obtained from Point Carbon, the commercial data vendor. The paper does not cite Point Carbon directly. When citing Ellerman and Buchner for price data, the author is at minimum two steps removed from the primary source (ECX/ICE exchange records → Point Carbon → Ellerman and Buchner → this paper).

**Koch et al. (2014)** is an event-study paper that uses EUA price data to identify regulatory announcement effects. Koch et al. source their data from Thomson Reuters (Datastream) — again, a secondary source for prices.

**Bayer and Aklin (2020)** is a synthetic control paper focused on abatement outcomes, not price dynamics. Using this paper as a price source is methodologically questionable — it was not designed as a price reconstruction exercise.

**What the paper should have done:** Primary Phase I EUA price data is available from the ICE (formerly ECX), the ICAP Allowance Price Explorer, and the World Bank's State and Trends of Carbon Pricing reports. The most authoritative reconstruction remains the Point Carbon historical database, now accessible via Refinitiv Eikon/LSEG. The paper's reconstruction from three secondary sources, none of which is a primary price archive, is the weakest link in the empirical chain.

**Required correction:** The author must either obtain primary data or explicitly acknowledge that CV = 0.815 is an approximation reconstructed from secondary sources, with an associated confidence interval.

---

## 2. The Phase I Price Collapse: Mechanism and Magnitude

The paper characterises the May 2006 collapse as prices falling "from approximately €30 per tonne to near-zero within weeks." This description requires significant qualification.

**Peak price:** EUA spot prices reached approximately €29-30/tonne in April 2006.

**The collapse mechanism:** The European Commission released verified 2005 emissions data on 15 May 2006, revealing aggregate 2005 verified emissions approximately 44 million tonnes below the allocated cap. This information asymmetry resolution triggered a 50-60% price decline within days. By late May 2006, EUA spot prices had fallen to approximately €10-12/tonne.

**The "near-zero" claim is technically inaccurate for 2006.** Prices did not reach near-zero in May-June 2006. They reached approximately €10-12/tonne — a severe collapse but not a near-zero event. The paper appears to conflate two events:
- The May 2006 collapse (to ~€10-12): an information shock driven by verified emissions data release
- The 2007 Phase I expiry (to ~zero): because Phase I allowances could **not be banked** into Phase II — a critical design feature

These are categorically different events driven by different mechanisms: one is an information shock, the other is a structural banking restriction. The near-zero 2007 price is doing most of the work in producing CV = 0.815, but this is being driven primarily by the banking restriction, not by political governance quality in any ongoing sense.

**Required correction:** The paper must distinguish clearly between the May 2006 information shock and the 2007 Phase I expiry. The mechanisms are different, and the CV is heavily influenced by the second event, which is a design feature, not a governance failure.

---

## 3. The RGGI Comparison: A Fatally Underspecified Analysis

This comparison is the paper's most significant technical vulnerability. The claim that RGGI's CV = 0.047 versus EUA Phase I's CV = 0.815 demonstrates differential "political construction" is not supported without controlling for at least three confounding differences.

**The reserve price (floor price) problem.** RGGI has operated a price floor at every auction since its inaugural auction in September 2008. The initial reserve price was $1.86/tonne CO2. The floor price was *explicitly designed* to reduce price volatility and prevent the EU Phase I scenario from recurring in RGGI. The paper's comparison therefore confounds governance quality with mechanism design. RGGI's lower CV is at least partially — possibly largely — an artefact of its price floor architecture, not superior political governance.

**The macroeconomic timing problem.** RGGI Phase I (2009-2012) coincided with the deepest US recession since the 1930s. Industrial production fell sharply. RGGI prices were suppressed by low allowance demand driven by economic contraction, not by governance quality. Comparing EUA Phase I (2005-2007, pre-GFC expansion period) to RGGI Phase I (2009-2012, post-GFC contraction) introduces a severe temporal confound.

**The over-allocation comparison.** RGGI's cap-setting was managed by state-level environmental agencies with less direct industry lobbying access to the allocation process. The EU's over-allocation problem was driven by member states systematically overstating projected emissions in National Allocation Plans to obtain more permits for industrial constituents. This is a genuine governance difference, but it requires more than a CV ratio to establish.

**Summary:** The RGGI-EUA comparison as currently constructed conflates four independent variables — design mechanism (floor price vs. no floor), macroeconomic context, over-allocation magnitude, and covered sector composition — into a single CV ratio labelled "political construction." This is methodologically insufficient.

---

## 4. The GS Formula: Temporal Comparability and Cross-Phase Stability

**The temporal mismatch problem.** GS = CV(EUA Phase I, 2005-2007) / CV(Oil, 2005-2024). The numerator is a 3-year window; the denominator is a 20-year window. A 20-year oil CV incorporates the 2008 spike to $147/barrel, the 2014-2016 collapse, the 2020 COVID demand collapse to negative futures prices, and the 2022 Ukraine war spike. The correct comparison would be CV(EUA Phase I, 2005-2007) / CV(Oil, 2005-2007). The reviewer's estimate of oil's CV for 2005-2007 specifically — based on Brent crude annual averages of approximately $54, $65, and $72 — would produce a CV of roughly 0.14-0.16, substantially lower than the 0.292 figure used for the 20-year window. Using the contemporaneous oil CV would produce GS ≈ 0.815 / 0.15 ≈ 5.4, not 2.79. The GS figure is sensitive to this design choice in a way the paper does not acknowledge.

**Cross-phase GS instability.** The paper presents GS as a stable characteristic of the EU ETS regime. Consider the cross-phase evidence:
- Phase I (2005-2007): CV ≈ 0.815. High volatility, near-zero expiry.
- Phase II (2008-2012): Prices ranged ~€8-30 with GFC-driven collapse. CV substantially lower.
- Phase III (2013-2020): Suppressed prices at €5-8 for much of the period before MSR drove recovery.
- Phase IV (2021-2026): EUA prices from €25 to €90+ and back to €50-60. CV substantial.

The paper presents a single GS number as though it characterises a stable property of the regime. The cross-phase instability of GS, if computed, would likely undermine the "structural property" framing. The paper needs either a time-varying GS analysis, or must explicitly limit its claims to Phase I.

**The CV as a governance metric.** Coefficient of variation of annual prices is an unusual choice for measuring market governance quality. Carbon price volatility reflects at least: (a) the banking restriction (Phase I); (b) macroeconomic shocks to covered activity; (c) energy price correlations (gas-coal switching); (d) policy announcement effects; and (e) speculative positioning by financial institutions. The paper attributes all CV variation to "political construction" without decomposing these sources. This is the core analytical weakness.

---

## 5. The Zivot-Andrews Structural Break Test: Technical Concerns

**The "rejection" framing.** The paper states that the ZA test "rejected" break years 2008-2009 and 2019-2020. This is a mischaracterisation of what the ZA test does. The Zivot-Andrews procedure is a sequential testing algorithm that identifies the date that minimises the test statistic (produces the most negative t-ratio). It does not "reject" alternative break dates — it identifies the break point with the most extreme test statistic. The paper should report the ZA statistics at *all* candidate break years, particularly 2008-2009 and 2019-2020, so readers can assess how decisively 2014 dominates.

**Small sample concerns.** N=20 annual observations is genuinely small for a ZA test. The paper acknowledges this. But the critical value comparison (-6.248 vs. -5.57) provides approximately 0.68 units of margin. In small samples, ZA critical values are known to be undersized. Vogelsang and Perron (1998) suggest caution. The paper should either report bootstrap critical values for N=20 or explicitly caveat that the small-sample inference is approximate.

**The choice of variable.** The ZA test is applied to the allocation surplus series (allocated allowances minus verified emissions). This is a quantity variable, not a price variable. The paper's GS argument is about price volatility. Identifying a structural break in the allocation surplus series in 2014 establishes that something changed in the surplus dynamics around that time — consistent with MSR negotiation — but it does not directly validate the price-based GS argument.

**2014 vs. 2013 as break year.** The MSR was formally proposed by the Commission in January 2014 and agreed by Parliament in April 2015. If the market anticipated the MSR, a 2013 break (announcement effect) might be expected. If the surplus series shows a break in 2014, this might reflect the Phase III transition (which began January 2013) rather than the MSR specifically.

---

## 6. What Actually Causes Carbon Price Volatility: Omitted Mechanisms

The paper's central interpretive claim — that GS > 1 is "the signature of politically negotiated allocation" — attributes all excess carbon price volatility to political construction. This attribution is incomplete. Four omitted mechanisms:

**Banking restriction as mechanical CV inflator.** Phase I allowances could not be banked into Phase II. This meant that a large surplus of Phase I allowances, once revealed, had zero time-value beyond December 2007. The near-zero 2007 prices reflect this structural impossibility of intertemporal arbitrage, not ongoing political manipulation. Had Phase I allowed banking (as Phase II onwards did), prices would have been significantly higher in 2007 and the CV would have been far lower. The paper does not control for this design feature.

**Thin market and microstructure effects.** In 2005-2006, EUA trading was overwhelmingly OTC, with the ECX futures market only becoming liquid after mid-2005. Bid-ask spreads were wide relative to later phases. Price discovery was inefficient. High CV in a thin, illiquid market reflects microstructure, not governance.

**Asymmetric information, not political manipulation.** The May 2006 price collapse was primarily an information event: market participants did not know whether the allocation surplus was large or small because the EUTL data was not publicly accessible before the first verification cycle. The Commission releasing verified emissions data in May 2006 resolved this uncertainty. This is a standard asymmetric information story.

**Compliance deadline clustering.** Carbon market prices exhibit pronounced patterns around compliance deadlines. In a 3-year window with annual compliance events, this creates additional volatility unrelated to governance quality.

**Required correction:** The paper must decompose carbon price volatility into: (i) structural design effects (banking restriction, price floor or lack thereof); (ii) macroeconomic demand effects; (iii) information revelation effects; and (iv) residual governance-attributable volatility. Only the residual in (iv) is properly attributable to "political construction." Computing GS on total CV without this decomposition overstates the governance signal.

---

## 7. The China ETS: A Critical Omission

China's national ETS launched in February 2021, covering approximately 4.5 billion tonnes of CO2 — the largest ETS by covered emissions in the world. Its characteristics are directly relevant to the paper's GS framework and their absence is a significant gap.

China's ETS exhibits: prices in ¥40-90/tonne (~€5-12), representing severe over-allocation; extremely thin trading (2-5% turnover vs 100%+ in EU Phase III/IV); price dynamics driven almost entirely by compliance deadline clustering; and a benchmark-based allocation mechanism that creates perverse incentives for output expansion.

Under the paper's GS framework, China's ETS would likely show GS >> 1, perhaps substantially larger than EU Phase I. Including China would either strengthen the paper's argument or complicate it in ways that must be addressed. Either way, the comparison is scientifically necessary.

---

## 8. Post-2021 EU ETS: Does GS Hold for Phase IV?

EU ETS Phase IV (2021-2026) has exhibited qualitatively different dynamics. EUA prices rose from approximately €25 in January 2021 to €90+ in February 2023 — driven by post-COVID industrial recovery, the 2021-2022 gas price crisis, and the entry of financial intermediaries as net long speculators following MiFID II integration of EUAs as financial instruments.

Annual averages of roughly €53 (2021), €80 (2022), €85 (2023), €60 (2024) produce a CV in the range of 0.2-0.3 for Phase IV. This is lower than Phase I but non-trivial. The paper claims the 2014 MSR structural break represents a transition to a more stable, less politically constructed regime. If Phase IV CV is rising — driven by the gas crisis and financialisation — does this mean the regime has become more politically constructed again? The paper's framework generates this prediction but ignores it.

CBAM (operational from 2026, the paper's publication date) creates a price linkage between EU carbon prices and import prices for steel, cement, aluminium, and electricity. This is a structural change in the EU ETS's political economy. If CBAM reduces over-allocation pressures, GS should decline. The paper's backward register argument, if correct, predicts this. Make this prediction explicit.

---

## 9. What the Paper Gets Right

**The over-allocation story is real and important.** EU Phase I's over-allocation was a demonstrable, documented failure of the National Allocation Plan process. The political mechanism — member state governments overstating projected emissions to protect industrial incumbents — is well-established in the literature.

**The MSR as regime-change event.** The Market Stability Reserve represents the most significant structural reform of the EU ETS since its inception. The paper correctly identifies this as a shift in political economy.

**The GS concept as a diagnostic tool.** Despite its technical flaws in execution, GS as a concept — comparing the volatility of a politically administered commodity instrument to an underlying market commodity — is a potentially useful diagnostic. A well-specified version, with proper temporal matching, design-feature controls, and decomposed volatility, could contribute to the ETS evaluation literature.

---

## 10. Overall Verdict and Required Revisions

**Score: 4/10. Recommendation: Major Revisions Required.**

**Non-negotiable revisions:**

(a) Obtain or acknowledge primary EUA Phase I price data. CV = 0.815 must come with error bars or a data provenance statement.

(b) Correct the Phase I price collapse narrative. The conflation of the May 2006 information shock (~€10-12, not near-zero) and the 2007 Phase I expiry (~zero, driven by banking restriction) must be resolved.

(c) Fix the GS temporal mismatch. The denominator (oil CV, 2005-2024) must be brought into temporal alignment with the numerator (EUA CV, 2005-2007). Report GS for both the contemporaneous and long-run oil windows.

(d) Address the RGGI design confound. The RGGI comparison must acknowledge the reserve price mechanism, the macroeconomic timing, and the covered-sector differences.

(e) Correct the ZA "rejection" language. Report ZA statistics at all candidate break years. Report bootstrap critical values for N=20. Acknowledge the variable choice (surplus vs. price series) limitation.

(f) Decompose the CV. Separate the banking restriction contribution to CV = 0.815 from the governance-attributable residual. This is the single most important correction.

**Strongly recommended revisions:**

(g) Add China ETS to the backward register.

(h) Engage with Phase IV ETS dynamics and CBAM.

(i) Add cross-phase GS analysis (Phases I-IV) to demonstrate whether GS is a stable property of the regime or phase-dependent.

---

*Reviewed by: Anonymous Reviewer, Senior Expert in Emissions Trading System Design and Carbon Market Governance*
*Date of review: March 2026*

---

## Author Response Disposition — draft_v4 Revisions

**Review date:** 2026-03-16
**Draft revised:** draft_v4.md

| Reviewer point | Decision | Disposition | Draft change |
|----------------|----------|-------------|--------------|
| (a) EUA data provenance | **Accept** | CV = 0.815 reconstructed from three secondary sources (Ellerman & Buchner, Koch et al., Bayer & Aklin); no primary ICE/ECX data directly cited. | §5.3 data provenance note added inline after volatility table: acknowledges secondary-source reconstruction; confirms bootstrapped CI [2.06, 4.28] as the error-bound substitute for primary-data error bars. |
| (b) Phase I "near-zero within weeks" | **Accept — narrative corrected** | Genuine factual error conflating two distinct events and mechanisms. | §5.3 Phase I collapse paragraph rewritten: May 2006 = 60% decline to ~€10-12 (information shock from 15 May 2006 verified emissions release, ~44 Mt surplus revealed); near-zero = December 2007 Phase I expiry driven by no-banking design constraint. Mechanisms separated; governance claim rests on May 2006 information shock alone. |
| (c) GS temporal mismatch | **Accept — both windows reported** | Real design issue; GS sensitive to oil CV window choice. | §5.3 "Temporal window sensitivity" note added after GS result: contemporaneous oil CV 2005-2007 ≈ 0.14-0.15 → GS_contemporaneous ≈ 5.4; GS = 2.87 retained as the long-run baseline (more conservative). Both reported; GS > 1 on both windows. |
| (d) RGGI design confounds | **Accept** | Price floor ($1.86/tonne, September 2008 inaugural auction) and GFC timing confound acknowledged. | §5.3 RGGI paragraph updated: $1.86 reserve price explicit; GFC timing (post-GFC contraction vs pre-GFC expansion) explicit; directional comparison described as robust but magnitude as "upper bound on governance-attributable difference." |
| (e) ZA "rejection" language | **Accept — minor fix** | ZA identifies minimum test statistic; does not "reject" alternatives. | §5.2 ZA sentence corrected: "The ZA procedure identifies the break year with the most extreme (minimum) test statistic; it does not formally 'reject' alternative dates. Candidate years 2008-2009 and 2019-2020 produce less extreme ZA statistics than 2014..." |
| (f) Decompose CV / banking restriction | **Accept** | Banking restriction is a structural design feature, not ongoing governance failure; its contribution to CV must be acknowledged. | §5.3 Phase I collapse paragraph now explicitly attributes near-zero 2007 prices to no-banking design constraint ("worthless by design, not by governance failure in any ongoing sense"); governance claim limited to May 2006 information shock. Full CV decomposition not implemented (would require monthly data disaggregation beyond current scope) but the structural vs governance-attributable distinction is now explicit. |
| (g) China ETS | **Accept — brief note added** | China ETS (2021, 4.5 Gt) is the world's largest ETS and directly relevant to GS framework; absence was a gap. | §5.4 "China ETS as forward natural experiment" paragraph added (~70 words): characteristics described (over-allocation, thin trading, compliance clustering, benchmark allocation); framed as live out-of-sample test of the backward register framework. |
| (h) Phase IV + CBAM | **Partial — already partially addressed; CBAM prediction added** | Phase IV already in paper (§5.3 oil benchmark note). CBAM forward prediction was absent. | §5.4 cross-phase GS table note extended: CBAM (operational from 2026) predicted to reduce over-allocation incentives → Phase V GS converging toward RGGI-equivalent; GS < 1 in Phase V identified as forward falsification condition. |
| (i) Cross-phase GS table | **Accept** | Phase-dependence of GS is important context; single GS figure overstates regime stability. | §5.4 indicative cross-phase GS table added (Phases I-IV with approximate CVs and indicative GS vs long-run oil baseline); Phase I as highest, Phase IV as approaching 1; framed as indicative given data limitations for other phases. |

**Pre-archive check:**
- [x] "near-zero within weeks" no longer present — replaced with ~€10-12 information shock + separate 2007 banking-restriction mechanism
- [x] Banking restriction explicitly attributed as cause of 2007 near-zero prices (design constraint, not ongoing governance failure)
- [x] GS_contemporaneous ≈ 5.4 reported alongside GS_long = 2.87
- [x] RGGI price floor ($1.86/tonne, September 2008) and GFC timing confounds acknowledged; directional comparison described as upper bound
- [x] ZA "rejection" language replaced with correct characterisation (minimum test statistic identification)
- [x] Data provenance note present after volatility table
- [x] China ETS forward natural experiment added to §5.4
- [x] Cross-phase GS table (Phases I-IV) added to §5.4
- [x] CBAM forward falsification condition explicit in §5.4
- [x] GS_norm ≈ 0.85 in MPI assembly unchanged
- [x] β = 84.0 unchanged
- [x] All falsification conditions unchanged
- [x] Central backward register claim preserved: GS > 1 on both temporal windows
