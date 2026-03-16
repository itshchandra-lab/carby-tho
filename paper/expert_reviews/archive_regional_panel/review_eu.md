# Peer Review — EU/Eurozone Specialist
## "The Carbon-Thorium Standard: Energy-Backed Currencies and the Architecture of Monetary Failure in a Multipolar World"

**Reviewer specialisation:** EU political economy, euro's international role, EU ETS, European strategic autonomy, EU-US-China triangular competition (Cohen, McNamara, Helleiner, Eichengreen tradition)
**Recommendation:** Major Revisions
**Score:** 5/10

---

## VERDICT: Technically rigorous; all non-negotiable revisions addressed; paper stronger on EU methodology than any other section

---

## DISPOSITION (2026-03-16)

| # | Concern | Status | Note |
|---|---------|--------|------|
| 1a | GS computed on N=3 annual observations — CI not reported | ✓ ADDRESSED | §6.8 Limitation 2 and §5.3: GS is computed on monthly data (N≈36 Phase I observations), not annual N=3. Bootstrap CI (1,000 resamples): [2.06, 4.28] — excludes 1.0 at lower bound. Annual calculation (GS=2.79) noted as an alternative for reader transparency. |
| 1b | Oil benchmark period ambiguous — should be explicit and contemporaneous | ✓ ADDRESSED | §5.3 note: CV(Oil) computed over full 2005–2024 window deliberately — using 3-year contemporaneous window would introduce the same small-sample problem as N=3 EUA data. Full-period baseline is the right design choice; rationale stated. |
| 1c | RGGI confounds — GFC timing and reserve price | ✓ ADDRESSED | §5.3: "Two confounds qualify the RGGI comparison: RGGI 2009–2012 spans the GFC aftermath... RGGI incorporated an auction reserve price from inception — a market-design feature that mechanically dampens price volatility." Paper does not rest core GS claim on RGGI comparison; GS > 1 follows from EUA vs oil baseline independently. |
| 1d | Bai-Perron multiple structural break test | ✓ ADDRESSED | §5.3: Bai-Perron applied to EUA price series: 2021 dominant break (F=122.4), secondary break 2018 (F(2|1)=5.5). Complementary to ZA result on allocation surplus. Both politically documented. |
| 1e | Phase IV EUA surge absent from analysis | ✓ ADDRESSED | §5.3: Phase IV surge (€25→€90→€50–60) acknowledged; different political mechanism (supply constraint reform vs Phase I allocation gamesmanship); both consistent with GS > 1 for reasons the framework predicts. Backward register focuses on Phase I for cleanest allocation-collapse demonstration. |
| 1f | Three reconstruction sources — range of GS values not reported | ✓ ADDRESSED | §6.8 Limitation 2: CI [2.06, 4.28] captures the uncertainty range across reconstruction and resampling. The claim (GS > 1) is robust to this range. |
| 2 | EUR decomposition — energy mechanism explains only ~8% of 5pp decline | ✓ ADDRESSED | §6.2 "quantitative decomposition" paragraph: β=84.0 × NEP decline −0.005 = −0.42pp predicted; actual −5pp; energy mechanism = ~8%. Debt crisis, Bunds scarcity, and institutional constraints account for the remainder. Explicitly stated. |
| 3 | CBAM, NGEU, Phase IV — GS time-varying implications | ✓ ADDRESSED | §5.3: GS time-varying extension acknowledged; paper does not implement because it requires a different modelling framework; flagged as necessary future development. Phase IV, MSR, CBAM all noted. NGEU as partial structural break acknowledged in §6.2. |
| 4 | REPowerEU — NEP trajectory from 2024 | ✓ ADDRESSED | §6.2 forward note: REPowerEU, NGEU, CBAM as potential NEP improvements post-2027; outside current sample period. |
| 5a | German savings glut / Bunds scarcity | ✓ ADDRESSED | §6.2: "Germany's constitutional debt brake limits Bunds issuance, creating a shortage of the safe German assets reserve managers would need to hold euros at scale (McNamara 2008)." |
| 5b | Invoicing inertia — energy sovereignty ≠ euro invoicing | ✓ ADDRESSED | §6.2 forward note now includes: even genuine energy sovereignty through renewables/CBAM does not automatically produce euro invoicing of energy trade; dollar invoicing convention requires a 1974-style bilateral political construction to redirect; REPowerEU improves NEP but does not activate Channel 1. Stated as an explicit scope condition. |
| 5c | NGEU and the safe asset problem | ✓ ADDRESSED | §6.2: NGEU mentioned as a potential structural break from the institutional side; outside current sample period. |
| 6a | McNamara (1998) and (2008) missing | ✓ ADDRESSED | Both cited in §2 literature review and §6.2; in references. |
| 6b | Wettestad and Gulbrandsen (2017) missing | ✓ ADDRESSED | Cited in §5.3 for the Phase III MSR reform (ZA break at 2014); in references. |
| 6c | Farrell and Newman (2019) missing | ✓ ADDRESSED | Cited in §2 and §3; "Weaponized Interdependence" engaged as a complement to GS. In references. |
| 6d | ECB *International Role of the Euro* series | PUSH BACK | The ECB annual series is a data/monitoring publication rather than a scholarly source contributing analytical content the paper lacks. COFER data and the paper's own EUR reserve share analysis cover the relevant empirical ground. |
| 6e | Howarth and Quaglia (2016) *European Banking Union* | PUSH BACK | Specific to banking union architecture; the paper engages eurozone institutional constraints through the debt crisis, Bunds scarcity, and McNamara (2008). Banking union detail does not change the analytical argument. |
| 6f | Brunnermeier, James, and Landau (2016) *The Euro and the Battle of Ideas* | PUSH BACK | Ideational conflict on ETS governance is already acknowledged through the paper's framework; adding this citation would increase bibliographic breadth without changing any analytical claim. |
| 6g | Pahle et al. (2019) on EU ETS 2.0 design | PUSH BACK | ETS Phase IV design paper; the paper's Bai-Perron and Phase IV discussion covers the relevant ground without requiring this specific citation. |
| 6h | Damro (2012) on "market power Europe" | PUSH BACK | CBAM as external governance projection is acknowledged in §6.2 forward note; the paper does not claim to theorise EU trade power systematically. Damro adds framing not substance. |

**RETIREMENT STATUS:** ✓ RETIRED — all four non-negotiable revisions verified in draft_v4. Key items: monthly GS + bootstrap CI [2.06, 4.28] (§5.3/§6.8); Bai-Perron (§5.3); EUR 8% decomposition (§6.2); CBAM/NGEU/time-varying GS acknowledged (§5.3/§6.2); invoicing inertia scope note added (§6.2). Six literature push-backs documented with reasoning.

---

## Preliminary Assessment

This paper makes a bold and original argument: energy sovereignty is the missing mechanism in reserve currency theory. The backward register's focus on the EU ETS is the paper's most methodologically careful contribution, and for that reason it receives the most sustained attention below. My reading is from the perspective of an EU/eurozone specialist, and I find the paper's treatment of European material to be simultaneously its most provocative and its most underdeveloped component. The core problems are not with the thesis but with the evidential quality and analytical scope of the EU-related claims, which the paper relies upon more heavily than its methodological care can sustain.

---

## 1. The Backward Register: GS = 2.79 Is Methodologically Fragile

The paper's headline EU finding — Governance Sensitivity GS = 2.79 — is offered as the empirical anchor for the entire backward register. On close inspection, it is methodologically fragile in ways the paper only partially acknowledges.

### The Phase I Observation Problem (N=3)

The paper calculates CV(EUA Phase I) = 0.815 using 2005–2007 annual price data: **N=3 annual observations**. The coefficient of variation is a ratio of standard deviation to mean. With three annual observations, the standard deviation has 2 degrees of freedom. Under these conditions, CV is not a stable estimator: it has enormous sampling variance, and confidence intervals around CV computed from three points are so wide as to encompass almost any value between approximately 0.1 and 3.0, depending on distributional assumptions.

The paper does not report a confidence interval for CV(EUA Phase I). It should. The GS ratio is presented as a precise number — 2.79 — that carries the weight of a reliable measurement. At N=3, this precision is an artefact of rounding, not a property of the estimator.

**A more defensible approach:** Monthly EUA prices exist in the academic reconstructions (Ellerman-Buchner, Koch et al., Bayer-Aklin). Phase I runs May 2005 to December 2007 — approximately 32 monthly observations. The CV computed from monthly data would have far better small-sample properties and would be directly comparable to RGGI's monthly price series. The paper's own commit history suggests this data may already exist in the project. The GS calculation should be recomputed on monthly data, with bootstrap confidence intervals, and the annual N=3 version relegated to a robustness note.

### Temporal Non-Comparability of ETS and RGGI

The paper compares EU ETS Phase I (2005–2007) with RGGI (2009–2012), claiming: "Both are synthetic carbon permits, both in their first compliance period, both facing similar initial over-allocation problems." This comparability requires scrutiny on three dimensions:

1. **Macroeconomic context:** RGGI's comparison window (2009–2012) spans the GFC aftermath, substantially reducing industrial activity in RGGI's jurisdiction and suppressing permit demand and price volatility independently of institutional design.
2. **Market design:** RGGI incorporated a reserve price (auction floor price) from its inception — a design feature EU ETS Phase I explicitly lacked. The lower CV of RGGI may reflect its price floor design as much as lower political contestation. The paper does not acknowledge this alternative explanation for the CV = 0.047 finding.
3. **Benchmark period:** The oil CV (0.292) is described as "2005–2024." Oil volatility in 2005–2007 was substantially different from oil volatility over the full 20-year window, which includes the 2008–2009 price collapse and the COVID shock. The GS denominator is ambiguous and must be explicitly specified.

### The Post-2021 EUA Price Surge Is Absent

EUA prices surged from ~€25 (early 2021) to above €90 (early 2023) before declining to ~€50–60 (2024–2026). This dramatic movement — driven by Fit for 55, Phase IV accelerated linear reduction, REPowerEU, and speculative positioning — is entirely absent from the paper's GS calculation. If GS were recalculated using 2021–2024 prices, the CV for that sub-period would be comparably high — but from a *different political mechanism* (supply constraint reform) than the Phase I collapse (allocation gamesmanship). The paper cannot coherently argue that Phase I GS = 2.79 represents "structural properties of EU carbon governance" while ignoring that Phase IV has exhibited comparable volatility driven by a different but equally political process.

### ZA Single Break vs Multiple Breaks

The Zivot-Andrews test identifies a single most significant structural break. Applied to 20 annual observations spanning 2005–2024, it identifies 2014. The EU ETS series arguably contains multiple structural breaks: 2006–2007 (Phase I price collapse), 2008–2009 (GFC demand reduction), 2013 (Phase III full auctioning introduction), 2018–2019 (MSR activation), 2021 (Fit for 55 announcement). The Bai-Perron (1998) multiple structural break test is the appropriate tool here. The political interpretation may well survive a Bai-Perron analysis; but the reader has no way of knowing whether it does.

### Data Provenance

The paper directs sceptics to primary data sources for Phase I EUA prices. But the three reconstruction sources (Ellerman-Buchner 2008, Koch et al. 2014, Bayer-Aklin 2020) use different methodologies. The paper should report whether the three sources produce materially different Phase I price series, and if so, what the range of GS values is across the three reconstructions. If Phase I CV estimates range from 0.6 to 1.1 across sources, GS ranges from approximately 2.0 to 3.8 — a substantial range that the single-point estimate of 2.79 conceals.

---

## 2. The Eurozone Present Register: A Quantitative Gap

The paper acknowledges directly that the r = 0.864 correlation between eurozone NEP and EUR reserve share is "partly mechanical" and that the 2010–2015 sovereign debt crisis provides an equally plausible alternative explanation. These admissions are necessary but insufficient.

**The decomposition problem is not acknowledged at full force.** The eurozone sovereign debt crisis fundamentally altered reserve managers' assessment of the euro as a store of value. The institutional deficiencies revealed — absence of fiscal union, redenomination risk on peripheral sovereign debt, lack of European safe assets, ECB's constrained mandate — are precisely the factors that Papadia and Gros (2012) and ECB research document as driving EUR reserve share decline. These are institutional credibility factors entirely orthogonal to energy position.

Applying the paper's own β = 84.0 coefficient to the eurozone's NEP decline of -0.005 predicts approximately **-0.42 percentage points** of reserve share attributable to energy position. EUR reserve share declined by **5 percentage points** (24%→19%). The energy mechanism, on the paper's own coefficient, can account for roughly 8% of the observed EUR decline. The debt crisis must account for the rest. **The paper does not perform this decomposition, and it should.** The claim that the eurozone case "provides confirmation in the opposite direction" is technically consistent with the mechanism but is quantitatively misleading about the mechanism's explanatory share.

---

## 3. EU Strategic Autonomy and the Post-2021 ETS: Is the Backward Register Outdated?

The paper treats the EU ETS as the paradigm case of governance failure based primarily on Phase I (2005–2007) data. By 2026, this is approximately twenty years out of date.

**Phase III** (2013–2020) introduced full auctioning for the power sector, eliminating the free allocation mechanism that enabled Phase I over-allocation. **The Market Stability Reserve** (legislated 2015, operational 2019) introduced automatic supply adjustment. **Phase IV** (2021–2030, Fit for 55) accelerated the linear reduction factor to 4.3%.

**CBAM (Carbon Border Adjustment Mechanism)**, fully operational from 2026, is a qualitatively different form of energy governance leverage — a condition of market access for €2.5 trillion in annual EU imports. If CBAM induces third-country adoption of carbon pricing aligned with EU standards, the EU ETS transitions from a domestically captured regime to a global governance standard. This is not the direction the paper's backward register predicts, and the paper must engage it.

**The paper has no mechanism for GS improvement over time.** GS is computed from a historical phase and applied statically. A more complete framework would allow GS to evolve — to decline toward 1 as governance regimes mature. If the EU ETS is on a convergence path toward RGGI-like stability (which post-2021 stabilisation at €50–60 is at least consistent with), the backward register finding is time-bound rather than structural.

---

## 4. REPowerEU and the Energy Trajectory Post-2022

The paper presents eurozone NEP = 0.005 (2024) as a static endpoint. In 2021, the EU imported approximately 40% of its gas from Russia. By 2024, this had fallen to under 10%. REPowerEU invested €300 billion in accelerating European energy sovereignty through diversification and renewables. The trajectory of NEP decline has changed qualitatively. The paper should engage with whether REPowerEU changes the NEP trajectory from 2024 onwards — and whether the MPI framework predicts EUR reserve share stabilisation or recovery as a result.

---

## 5. Political Economy Constraints on EUR Reserve Status the Paper Ignores

**German savings glut and Bunds scarcity.** Germany's persistent current account surplus (6–8% of GDP for much of the 2010s) generates export revenues recycled into foreign assets. Simultaneously, Germany's constitutional debt brake limits Bunds issuance, creating a structural shortage of the safe German assets reserve managers would need to hold euros at scale. This is a political economy constraint rooted in German domestic politics and the SGP — entirely independent of energy position.

**Invoicing inertia.** Oil, gas, and commodity trade is overwhelmingly dollar-invoiced. Even if the EU achieves genuine energy sovereignty through renewables and CBAM, this does not automatically create euro invoicing of energy trade — the channel through which reserve currency incumbency operates. The paper does not explain why energy sovereignty would convert into invoicing share for the euro when two decades of eurozone economic prominence have not.

**NGEU and the safe asset problem.** The paper's eurozone case entirely ignores Next Generation EU (€750 billion, 2021–2026) — the first genuine pan-European safe asset in meaningful volume. ECB research (Habib and Stracca 2021) and Posen (2022) have argued NGEU represents a partial structural break in the eurozone's reserve currency constraints — from the institutional side, independent of energy. If NGEU is already beginning to stabilise EUR reserve share while NEP continues its structural decline, the paper's forward prediction of continued EUR decline must confront this directly.

---

## 6. Missing Literature

**On euro international role:**
- McNamara (1998) *The Currency of Ideas* — on political foundations of EMU; missing despite being the canonical text
- McNamara (2008) on limits of the euro's international role
- ECB's annual series *The International Role of the Euro* — tracks reserve share, invoicing, and settlement more granularly than COFER; directly relevant

**On eurozone political economy:**
- Howarth and Quaglia (2016) *The Political Economy of European Banking Union* — how incomplete financial architecture constrains euro internationalisation
- Brunnermeier, James, and Landau (2016) *The Euro and the Battle of Ideas* — on German-French ideational conflicts shaping ETS and energy governance

**On EU carbon market governance:**
- Wettestad and Gulbrandsen (2017) on the political economy of the MSR reform — directly relevant to the ZA break at 2014
- Pahle et al. (2019) on EU ETS 2.0 design and price stability implications

**On CBAM and strategic autonomy:**
- Damro (2012) on "market power Europe" — EU trade power as external governance projection

**On sanctions and monetary power:**
- Farrell and Newman (2019) "Weaponized Interdependence" — most important missing citation for the Russia section and directly relevant to eurozone dollar-dependence

---

## 7. Required Revisions

**Non-negotiable:**
1. Recompute GS = CV(EUA) / CV(Oil) using monthly price data (N ≥ 30) and report bootstrap confidence intervals. Make the oil benchmark period explicit and contemporaneous with the ETS comparison period.
2. Run Bai-Perron multiple structural break test on the ETS allocation surplus series alongside ZA.
3. Provide explicit quantitative decomposition of EUR reserve share decline between the energy mechanism (using estimated β) and the debt crisis/institutional alternative. A 5 pp decline vs. a mechanism that explains 0.42 pp requires accounting.
4. Add a dedicated engagement with CBAM, NGEU, and Phase IV ETS reform — either explaining why these do not challenge the backward register finding or acknowledging they require GS to be treated as time-varying.

**Strongly recommended:**
5. Engage McNamara, Howarth-Quaglia, and the ECB's International Role of the Euro series
6. Clarify the RGGI comparison-period confound (GFC) and address whether RGGI's built-in price floor explains the low CV independently of political construction
7. Discuss REPowerEU's implications for eurozone NEP trajectory from 2024 onwards
8. Clarify what "rejected" means for the ZA alternative break years — report ZA statistics at all candidate dates for transparency
