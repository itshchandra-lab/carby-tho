# §9 — Conclusion: The Mechanism, Its Predictions, and Its Limits

## 9.1 What the Paper Has Done

This paper has proposed and tested the Monetary Power Index (MPI) — a theoretical
framework that formalises the relationship between energy sovereignty and monetary power
across energy eras. Three empirical legs test three components of the framework, and
the synthesis assembles them into a coherent account of monetary power's past,
present, and future distribution.

The **backward leg** established that energy governance is politically constructed.
The EU ETS allocation surplus broke structurally in 2014 at a political event, not a
supply shock (ZA stat=−6.248, p=0.0006). Phase I EUA volatility was 17 times higher
than the RGGI in its equivalent first compliance period — both synthetic permits,
the difference attributable entirely to the EU's allocation politics. Energy position
is a policy variable. The transition between eras is not technologically determined
but politically contested. This is the premise without which the forward leg has no
significance: if energy positions were exogenous, TMPI rankings would be descriptions
of geological fate, not strategic opportunities.

The **present leg** documented the mechanism in the two cases where it can be cleanly
identified. The United States — net energy producer, NEP rising through the shale
era — shows cointegration between lagged NEP and reserve share; USD share has
stabilised since 2021 as the shale-era NEP gain flows through the λ≈10 year lag.
The eurozone — net energy importer, NEP declining from 0.010 (1999) to 0.005 (2024)
— shows r=0.864 between lagged NEP and EUR reserve share decline. Japan provides a
natural experiment: Fukushima collapsed NEP by 61% and yen reserve share has been
stagnant since. Switzerland falsifies nothing: institutional quality can substitute
for energy position in financial entrepôts, a boundary condition the framework
anticipates.

The **forward leg** mapped where the mechanism points next. The TMPI top-three
ranking — USA (100), Canada (20.8), India (15.8) — is scenario-invariant across
three transition assumptions. The full MPI framework reveals the trajectory: India's
MPI is currently suppressed by negative NEP but rises discontinuously as p_t
increases, driven by the world's largest thorium reserves and an active three-stage
nuclear programme. This trajectory is the central forward claim of the paper and
is unproducible by any present-era framework.

## 9.2 Russia as the Hinge: Two Mechanisms, Not One

Russia threads through all three temporal legs, but the IR theory reviewer's challenge
must be addressed directly: two distinct causal mechanisms are operating simultaneously,
and conflating them would make the thesis unfalsifiable.

**Mechanism A: The structural energy corridor (thesis mechanism).** Russia's
pre-existing energy dominance in Eurasian supply chains made bilateral corridor
formation *structurally viable* before 2022. The ruble-yuan energy relationship traced
hydrocarbon supply routes that had existed for decades; the ruble-rupee corridor traced
Indian refinery dependence on Russian crude that predated the sanctions. These corridors
did not emerge from nothing in February 2022. They emerged from a pre-existing energy
geography. This is the present-leg mechanism operating under duress: energy
relationships determined which monetary corridors were viable when forced, not merely
which ones were convenient. Mechanism A supports the thesis.

**Mechanism B: The coercion shock (GS mechanism).** SWIFT exclusion and EU ETS
expulsion did not test Mechanism A. They tested the GS argument in the backward leg:
Western monetary and carbon infrastructure is political weaponry, not neutral mechanism.
Russia's expulsion confirms that allocation regimes — whether carbon markets or
interbank settlement systems — are constructed to be excludable by political decision.
GS > 1 in the monetary domain is the backward-leg claim; Russia 2022 is its most
vivid demonstration. Mechanism B does not support the thesis independently — corridor
formation under coercion is consistent with many theories — but it confirms the GS
premise that makes the thesis non-trivial.

The paper does not treat forced corridors as proof of organic monetary strategy. It
treats them as proof that pre-existing energy geography determined which coerced
outcomes were structurally possible. A sanctions shock to a country with no energy
relationships (e.g., a financial entrepôt with no bilateral energy supply) would not
produce energy corridors. Russia's corridors emerged because the energy geography was
already there. That distinction is what keeps the thesis falsifiable: if energy
geography had not preceded the coercion, the corridors could not have formed at this
speed or scale.

## 9.3 The Falsification Registry

The paper's forward claims are dated and specific. We record them here and in
`outputs/tables/falsification_registry.csv`.

**Claims checkable at submission:**
- ZA break year is within ±2 years of a documented political event. *[Check: 2014,
  Phase III structural reform — confirmed.]*
- EUA Phase I CV > RGGI Phase 1 CV. *[Check: 0.815 vs 0.047 — confirmed.]*
- USA ARDL bounds F-statistic exceeds I(1) critical value. *[Check at submission.]*
- USA DOLS bootstrap CI for NEP coefficient excludes zero. *[Check at submission.]*
- TMPI top-3 order scenario-invariant. *[Check: USA > CAN > IND across Low/Base/High
  — confirmed.]*

**Claims checkable at BIS Triennial 2028:**
- INR FX turnover share rises with India's nuclear capacity additions by 2030.
  *Falsify if: INR share flat or declining despite nuclear additions.*

**Claims checkable at BIS Triennial 2031:**
- INR FX turnover share approaches 3–5%.
  *Falsify if: INR share <2% despite programme completion.*

**Claims checkable at IMF COFER 2035–2040:**
- AUD reserve share remains within ±0.5 percentage points of its 2022 level (~6.7% of allocated reserves) through 2040, conditional on AUKUS nuclear capacity coming online.
  *Falsify if: AUD share falls more than 1 percentage point below 2022 level after AUKUS nuclear capacity is confirmed operational. Note: the failure condition is asymmetric — a sharp decline (>1pp) falsifies niche reinforcement; a sharp rise (>2pp) would falsify the Katzenstein filter (niche reinforcement, not independent activation).*

**Claims checkable at BIS Triennial 2037:**
- BRL does NOT gain reserve share without capital account opening.
  *Falsify if: BRL FX turnover rises without Chinn-Ito KAOPEN improvement.*

The last item is rare in IPE: a negative prediction about a specific country by a
specific date. If it is wrong — if Brazil gains reserve currency status without
institutional reform — the mechanism as specified fails for the institutional quality
term. We would welcome being wrong.

## 9.4 Extensions

Three extensions follow directly from the framework.

**Entity-specific Governance Sensitivity.** This paper estimates GS for the EU carbon
governance regime. Constructing GS for each entity — using domestic energy price
regulation data, ZA statistics on national energy policy series, or regulatory
stringency indices — would enable cross-entity variation in GS and a more precise
separation of the governance term from the energy position term in the MPI regression.

**Estimating p_t independently.** We calibrate transition probability from scenario
bounds (Low/Base/High nuclear share assumptions). An independent p_t series —
constructed from nuclear technology cost curves, IAEA capacity projections, and
geopolitical signal indices — would make the synthesis chart more than illustrative
and the forward predictions more precisely conditional.

**The geopolitical activation conditions paper.** The distinction between TMPI
*potential* and actual monetary leverage activation is the paper's most politically
consequential implication, and it requires a Katzenstein (1985) filter applied to the
forward leg. Small states and alliance-embedded states do not independently leverage
resource endowments into monetary structural power. The MPI framework makes specific,
falsifiable cross-case predictions for the activation question:

- **India** (TMPI rank 3): sovereign fuel cycle under active construction, non-aligned
  foreign policy tradition, capital account under domestic policy control. Prediction:
  INR FX share rises with nuclear capacity. Activation expected.

- **Australia** (TMPI rank 0 currently, rising post-AUKUS): Five Eyes member,
  US-alliance constrained. Prediction: AUD maintains its current reserve niche (already
  a reserve currency via Arslanalp et al. 2022) but does *not* gain share
  disproportionate to current position through independent energy leverage. AUKUS
  nuclear capacity reinforces the existing niche within the dollar order; it does not
  create an independent monetary leverage position. *Falsify if*: AUD share rises
  sharply after AUKUS nuclear capacity comes online.

- **Canada** (TMPI rank 2): Five Eyes member but resource trade increasingly
  denominated in CAD through bilateral arrangements. Prediction: modest, quiet share
  gains through commodity channels, not through dollar system displacement.

- **Brazil** (TMPI rank 4): capital account closed (Chinn-Ito KAOPEN = −1.25).
  Prediction: no monetary activation regardless of thorium endowment. *Falsify if*:
  BRL gains reserve share without KAOPEN improvement by 2037.

These are cross-case predictions, not just country-level. If India activates and
Australia does not, the Katzenstein filter is supported: alliance structure is the
operative variable distinguishing activation from niche reinforcement. Formalising
these conditions — specifying the interaction between TMPI potential, alliance
structure, and capital account regime — is Paper 3 of this research programme.

## 9.5 The Larger Claim

The reserve currency system is not determined by GDP alone. It tracks energy
sovereignty, with a generational lag, filtered through the political construction of
governance regimes. Sterling followed coal. The dollar followed oil. What follows
thorium — if thorium follows — will not be determined by which country discovers the
most reserves. It will be determined by which country constructs the governance regime
that makes those reserves into leverage, builds the institutional quality that makes
its currency credible, and does so while the transition probability p_t is still
rising.

That window is open. It will not remain open indefinitely. The backward test proves
that incumbents have every incentive to slow it.
