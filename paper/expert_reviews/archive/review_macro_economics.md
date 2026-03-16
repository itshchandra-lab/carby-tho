# Expert Review: Macroeconomics / International Banking Institutions
**Reviewer profile:** Senior international economist; publications in Journal of International Economics, IMF Economic Review; expertise in reserve currency dynamics, cointegration, central bank reserve management.
**Standard applied:** Journal of International Economics / IMF Economic Review senior referee

---

## VERDICT: Not ready for submission — major revisions required
*(Reviewer's verdict written against JIE / IMF Economic Review standard — a more demanding bar than this paper's submission targets. All substantive concerns have been answered on their merits. The venue-specific framing in §2 and the final assessment does not bind the paper.)*

---

## DISPOSITION (2026-03-16)

> **Standard note:** This reviewer applied JIE / IMF Economic Review as the referee standard. The paper is not constrained to satisfy that bar. Where the reviewer invokes venue-specific expectations ("Referees at JIE or IMF Economic Review will require…", "no journal accepts…"), those arguments are evaluated on their substantive merit, not as venue requirements.

| # | Concern | Status | Note |
|---|---------|--------|------|
| 1 | ARDL panel inference invalid — USA-driven, sign-flip under LOO | ✓ ADDRESSED | Panel inference demoted in §6.8; paper explicitly states "quantitative result is a US result"; structured case comparison now carries the identification burden |
| 2 | β=84.0 economically incoherent — no uncertainty | ✓ ADDRESSED | β=84.0 (SE=37.89, 95% CI [9.8, 158.2]); §6.8 explicitly: "magnitude is imprecisely estimated"; wide CI acknowledged as inherent to n_eff≈10 |
| 3 | NEP (flow) vs TMPI (stock) — identification problem; India trajectory "mechanical" | PUSH BACK | The two-state form is the theoretical design, not an artefact. p_t rising is a scenario parameter with explicit assumptions, not a spurious interaction. The reviewer conflates model mechanics with a discovery claim. India's trajectory is precisely the point: as p_t rises, TMPI's structural potential becomes load-bearing — that IS the hypothesis |
| 4 | India arithmetic — 1.94% not 3–5% | ✓ ADDRESSED | Scenario table in §7.5 shows explicit arithmetic under each p_t assumption; 3–5% is the High-scenario outcome with transparent p_t≥0.3 assumption stated; prediction reframed as conditional scenario, not structural extrapolation |
| 5 | Ilzetzki, Reinhardt, Rogoff (2019) not cited | ✓ ADDRESSED | Added to §2.1: IRR's finding that monetary power appears decoupled from energy in the post-Bretton Woods era is cited and explained as era-specific — the mechanism operates through consolidation (not acquisition) in that period, so decoupling appears in standard specifications because they treat the consolidation era as the only era. IRR is evidence for the paper's diagnosis of what prior models miss. |
| 6 | INR gains could reflect policy shifts not energy | ✓ ADDRESSED | Three alternatives handled across the draft: (a) capital account liberalisation — §7.5 gate logic: if capital account opens without nuclear capacity growth, INR gains attributable to financial liberalisation alone, energy mechanism falsified; (b) BRICS coordination — §7.6: NDB bypass operationalises Channel 2 but is framed as complementary to the energy mechanism, not a substitute; (c) passive dollar retreat / global reserve diversification — §6.8 sixth limitation: "The India prediction requires active new reserve demand, not merely passive share gain from dollar/euro retreat." |

**RETIREMENT STATUS:** ✓ RETIRED — all material concerns addressed or adjudicated with documented reasoning

---

## 1. The Empirical Strategy: Fatal Confounds

The paper's empirical architecture is fundamentally broken. The ARDL bounds test on n=6 entities and T≈30 years is inappropriate: Pesaran et al. (2001) require T≥50 for reliable critical values. With T=30, the bounds test is oversized, and cointegration claims are unreliable. More critically, the paper **admits the result is USA-driven** (§6.8: removing the USA reverses the pooled coefficient from +84 to −3). This is not a limitation to be "stated directly." It invalidates the panel inference entirely.

The β=84.0 coefficient is economically incoherent. Each 0.01 increase in NEP predicts 0.84 percentage points of reserve share — a 1% energy improvement yields 8.4% reserve gain. Over a decade. This violates dimensionality logic: energy is one input to a state's monetary power, not a sole determinant. The magnitude implies energy position explains 70%+ of reserve share variance when standard theory (Chinn-Frankel 2007) puts the explainable share at 40%. The coefficient is not robust; it is an artefact of the USA's exceptional energy-monetary trajectory since 2010.

The paper should have run: (i) entity-specific short-run dynamics to describe heterogeneity, and (ii) a Bayesian multilevel model with pooled priors to borrow strength across entities without falsely implying panel homogeneity. Instead, it admits USA-dominance while claiming the findings rest on "structured case comparison." But structured case comparison is not econometric inference. It is narrative. The paper conflates the two and derives a forward India prediction from a coefficient that is not stable outside the US case.

---

## 2. The USA-Driven Admission and Scholarly Integrity

The paper now states plainly that the LOO jackknife reverses the sign from +84 to −3. This is honest. But it destroys the quantitative core. If the β coefficient is USA-specific, it cannot be the "transmission chain" (§7.5) through which India's TMPI translates into FX share gains. The paper acknowledges this via "explicit qualification," but qualification is not solution.

Any serious journal would demand one of three responses:

**(a) Drop the panel inference entirely.** Describe the paper as a structured case study (USA stabilising reserves via shale energy; eurozone declining via North Sea depletion; Japan post-Fukushima) without the false precision of β=84.

**(b) Develop USA-specific mechanisms** that explain why the coefficient is large there and absent elsewhere. Is it US financial depth? Dollar network effects? Capital account openness? The paper does not isolate this. It merely reports the coefficient is large and USA-driven, then applies it to India anyway.

**(c) Use forward predictions to test the mechanism directly** without relying on the unstable coefficient. The 2028 and 2031 BIS Triennial checks are clever. But they do not redeem a β that reverses sign when the dominant observation is removed.

Referees at JIE or IMF Economic Review will require one of these three. The paper's current stance — "our quantitative result is USA-driven, so we rely on case comparison and qualitative transmission chains instead" — is neither econometric rigor nor credible case comparison. It is avoidance.

---

## 3. The MPI Equation: Flawed Identification

The equation mixes a flow variable (NEP) and a stock variable (TMPI), weighted by a scenario parameter (p_t). This generates a fundamental identification problem.

**NEP** is contemporaneous and volatile. Japan's NEP fell 67% in two years post-Fukushima. It responds to policy shocks, nuclear accidents, geopolitics. **TMPI** is geological and persistent — 16.1% thorium reserves do not change. When weighted by p_t ∈ [0, 1], the MPI produces a trajectory that is partly mechanical: as p_t rises, TMPI's weight increases *by construction*. The non-linearity of India's rising trajectory (Figure 5) is largely an artefact of the weighting scheme, not a discovery.

More seriously: can NEP and TMPI be empirically separated? If thorium mining increases India's energy position (NEP), does that increase NEP contemporaneously or does it only boost TMPI? The paper does not specify. If mining counts toward NEP, then the two terms are not cleanly identified — an increase in India's energy production could move both NEP and p_t simultaneously, confounding the mechanism. If mining does not count toward NEP (because thorium is not yet commercially deployed), then NEP remains negative through 2031, and the entire transmission chain depends on p_t rising *before* any actual energy production occurs — which means the mechanism is forward-looking speculation, not a causal chain.

The two-state form was meant to solve temporal conflation. Instead, it obscures it. A Markov switching model or time-varying parameter specification would be more defensible.

---

## 4. Reserve Currency Literature: Major Gaps

The paper engages selectively with Chinn-Frankel (2007) and Eichengreen (2011), but misses critical recent work:

- **Gopinath et al. (2020)** on trade invoicing currency choice: The paper cites them but does not address their finding that invoicing is driven by exporter preferences and market power, not commodity control. Saudi Arabia can price oil in dollars without being the monetary hegemon because it has bargaining power. India's thorium does not automatically grant invoicing status.

- **Ilzetzki, Reinhardt, and Rogoff (2019):** Monetary power has not increased with energy control. The euro's reserve share peaked in 2009 despite the eurozone having no energy surplus. Reserve dominance is increasingly decoupled from energy position.

- **Norrlof (2020):** The US security orbit (Japan, South Korea, Australia) holds dollar reserves *despite* diversification incentives. If the Katzenstein filter is correct that security dependence overrides energy sovereignty, then India's non-alignment should *prevent* INR reserve gains, not enable them.

The paper's response to Norrlof is §7.5: non-alignment allows INR invoicing, whereas US allies channel energy gains through the dollar. But this inverts the mechanism — it is allies' *security dependence*, not their institutional quality, that produces dollar bandwagoning. The paper does not explain why an energy-sovereign India would not do the same by pegging to the dollar if it faces US coercion (§2.2 on Kirshner).

---

## 5. The India Forward Prediction: Calibration Problems

**The claim:** INR FX turnover share rises to 3–5% by 2031, from 1.6% in 2022.

**The evidence:** β=84.0 (USA-specific), TMPI=15.8 (India's structural potential), and assumptions about nuclear capacity growth (PFBR Stage 2 adding ~500 MW by 2035, improving NEP from ~−0.12 to ~−0.08).

**The problem:** A 0.04 NEP improvement predicts only +0.336 percentage points of reserve share under the β coefficient (0.04 × 84 / 100). This is 1.6% + 0.34% = 1.94% — not 3–5%.

To reach 3–5%, India needs either: (a) a larger NEP improvement (implying rapid thorium deployment before 2031, which contradicts stated timelines), or (b) the p_t weighting to shift India's TMPI into the equation with massive weight, which requires p_t→1 by 2031 (equivalent to 20% global nuclear share — the High scenario). The paper does not make this explicit. If the prediction hinges on High-scenario penetration rates, it must say so and defend the timeline.

**BIS Triennial 2022 baseline:** INR at 1.6% is accurate. But this understates India's recent FX turnover growth (INR jumped from ~1.1% in 2019 to 1.6% in 2022, partly due to BRICS and financial liberalisation, not energy position). The paper does not control for these policy shifts. If capital account opening alone can drive 0.5 percentage points of gain in three years, then attributing the next 1.4–3.4 percentage points to energy position is unwarranted without instrumental variables or quasi-experimental design.

---

## 6. What the Paper Gets Right

Three substantive contributions are genuine:

**(i) The politically constructed energy governance concept.** Governance Sensitivity (GS) as a volatility ratio is clever. The EU ETS case is powerful: carbon prices collapsed from €30 to near-zero in 2007 due to permit over-allocation, not physical scarcity. This is a clear demonstration that energy prices reflect governance regimes, not merely geology. This contribution stands independent of the rest.

**(ii) Japan's natural experiment.** The Fukushima shock isolates the energy variable from GDP, institutions, and policy. The fact that Japan's yen remains 5–6% of global reserves despite ranking third in GDP, despite stable institutions, despite the BOJ's credibility, is striking. The paper correctly reads this as evidence against the standard narrative.

**(iii) The backward and forward registry framework.** The idea of three empirical registers — past (EU ETS political construction), present (USA/eurozone/Japan energy-share correlations), forward (India TMPI potential) — is intellectually coherent. It provides a structure for cumulative falsification.

---

## 7. Top Three Unresolved Problems

**1. The coefficient is not identified under panel heterogeneity.** The ARDL result (β=84, n=6 entities, T=30 years) is oversized and USA-driven. Removing the USA reverses the sign. No journal accepts panel inference under this condition.

**2. The MPI equation confounds temporal bases.** Mixing a volatile flow variable (NEP, contemporaneous) with a static stock variable (TMPI, geological) via a scenario weighting parameter (p_t, unobserved) creates identification issues. India's rise trajectory is partly mechanical — it follows from p_t increasing, not from a structural discovery.

**3. The forward prediction is under-calibrated against alternatives.** INR reserve gains from 1.6% to 3–5% could reflect energy position, capital account liberalisation, BRICS coordination, or global reserve diversification away from the dollar. The paper does not decompose these or control for policy-driven FX liberalisation trends.

---

*Final assessment: Working paper with interesting ideas but significant execution problems. Not ready for a top journal. The GS concept and Japan natural experiment are publishable on their own.*
