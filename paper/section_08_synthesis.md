# §8 — Synthesis: MPI Trajectories, Russia as the Hinge, and the Falsification Architecture

## 8.1 Assembling the MPI

The three empirical legs each estimate one component of the MPI framework. This section
assembles them into the full two-state expression and derives the forward trajectories
as p_t varies from 0 to 1.

**Component estimates:**
- GS_regime = 0.815 / 0.292 = 2.79, normalised to GS_norm ≈ 0.85 (regime-level
  scaling anchor; entity-specific GS_{i,t} values in Table 3 of §3.4 enter the MPI
  to differentiate entities within each state)
- GS_RUS = 0.011 post-2022 (data-derived from 2022–23; reflects sanctions exclusion
  from Western monetary and carbon governance infrastructure)
- NEP_i: current values from World Bank/OWID panel, normalised to [0,1]
- TMPI_i: from Section 7, USA=100 normalised to 1.0

The MPI at transition probability p_t:

```
MPI_{i,t} = (1−p_t) · [NEP_norm_i · GS_norm]  +  p_t · [TMPI_norm_i · GS_norm]
```

## 8.2 MPI Trajectories as p_t Rises

Figure 1 plots MPI scores for eight entities at p_t = 0.0, 0.2, 0.5, and 1.0, and
Figure 2 shows continuous trajectories. Three trajectory patterns emerge:

**Declining:** UK and Japan have strong current NEP-derived positions and low TMPI
(zero or very low reserves). Their MPI falls as p_t rises — the transition erodes
their current monetary leverage before they can build replacement positions. Japan
recovers post-2035 if nuclear restart proceeds (trajectory-adjusted TMPI). UK has no
identified recovery path under current policy.

**Rising:** India has the most striking trajectory — low current NEP (net energy
importer), third-highest TMPI globally. At p_t=0, India's MPI is near zero. As p_t
rises, India's MPI rises faster than any other entity, overtaking Russia, China, and
eventually approaching Canada. The mechanism that produced this prediction —
differentiating a current flow (NEP) from a structural endowment (TMPI) using a
two-state framework — is the paper's primary theoretical move. No present-era
regression or static ranking produces this result.

**Stable:** USA and Canada hold strong positions in both states. USA leads at p_t=0
(highest NEP of any entity) and at p_t=1 (highest TMPI). Canada leads on institutional
quality and has sufficient nuclear capacity to rank second in TMPI. Their MPI trajectories
are relatively flat — the transition does not threaten their positions; it may modestly
improve Canada's relative standing as γ rises.

**Constrained:** Russia has non-trivial NEP and TMPI components, but
GS_RUS = 0.05 post-2022 suppresses both State 0 and State 1 terms. Russia's MPI
remains low regardless of p_t, because the governance infrastructure that makes
energy leverage convertible into reserve status is inaccessible under sanctions. This
is the framework's prediction for Russia: strong endowments, permanently suppressed
activation unless the GS constraint is lifted by a change in the sanctions regime.

## 8.3 Russia: The Hinge

Russia is the paper's most powerful illustration because it provides simultaneous
evidence for the backward, present, and forward legs — through two distinct causal
mechanisms that must be kept analytically separate.

**Mechanism A — Structural energy geography (present-leg mechanism).** Russia's
pre-existing Eurasian energy supply relationships made bilateral corridor formation
structurally viable before 2022. The ruble-yuan energy relationship traced hydrocarbon
supply routes that existed for decades; ruble-rupee corridors traced Indian refinery
dependence on Russian crude oil. These corridors did not emerge ex nihilo in February
2022. They emerged because the energy geography was already there. This is the
present-leg mechanism: energy position determines which monetary corridors are viable
when pressure is applied. A sanctions shock to a state with no energy relationships
would not produce energy corridors. Russia's corridors formed because they were
structurally possible, not merely because they were forced.

**Mechanism B — Political weaponisation of governance (backward-leg GS mechanism).**
SWIFT exclusion and EU ETS expulsion confirm the backward leg's GS claim: Western
monetary and carbon infrastructure is political weaponry, not neutral mechanism.
The speed and scale of the exclusion — activated within days of the 2022 invasion
— demonstrates that the governance infrastructure can be made excludable by political
decision. GS > 1 applies not only to carbon permit allocation but to the allocation
of access to international settlement systems. Russia 2022 is the backward test
applied to monetary infrastructure.

These mechanisms make different predictions and would generate different evidence if
wrong. If Mechanism A is wrong — if energy geography did not determine viable corridor
formation — then countries without pre-existing energy relationships would have formed
comparable bilateral corridors under comparable pressure. No evidence of this exists.
If Mechanism B is wrong — if Western monetary infrastructure were not political
weaponry — then exclusion would require lengthy legal process rather than executive
decision. The speed of SWIFT exclusion refutes this alternative.

## 8.4 The Falsification Architecture

The paper commits to 11 specific falsifiable claims, 5 checkable at submission and
6 at dated future checkpoints. The full registry is in `outputs/tables/
falsification_registry.csv`. The claims and their check dates:

**At submission (checkable now):**

| Claim | Test | Status |
|-------|------|--------|
| ZA break within ±2yr of political event | 2014 vs Phase III reform | ✓ Confirmed |
| EUA Phase I CV > RGGI Phase 1 CV | 0.815 vs 0.047 | ✓ Confirmed |
| USA ARDL F-stat > I(1) critical value | Entity ARDL | Check at submission |
| USA DOLS β bootstrap CI excludes zero | Wild bootstrap | Check at submission |
| TMPI top-3 scenario-invariant | Low/Base/High | ✓ Confirmed |

**At BIS Triennial 2028:**

INR FX turnover share rises with India's nuclear capacity additions by 2030.
*Falsify if: INR share flat or declining despite nuclear additions proceeding on
schedule.*

The INR prediction does not require thorium deployment. It requires that markets
price India's growing nuclear capacity — and with it, growing energy sovereignty —
into currency demand. BIS 2022 shows INR at 1.6% of global FX turnover. The
prediction is that INR exceeds 2.5% by BIS 2028.
*Falsify if: INR share below 2.0% in BIS 2028 despite nuclear capacity additions
proceeding on schedule.*

**At BIS Triennial 2031:**

INR FX turnover share approaches 3–5%.
*Falsify if: INR share below 2.5% in BIS 2031 despite programme completion.*

**At IMF COFER 2035–2040:**

AUD reserve share remains within ±0.5 percentage points of its 2022 level (~6.7% of allocated reserves) through 2040, conditional on AUKUS nuclear capacity coming online.
*Falsify if: AUD share falls more than 1 percentage point below 2022 level after AUKUS nuclear capacity is confirmed operational. Note: the failure condition is asymmetric — a sharp decline (>1pp) falsifies niche reinforcement; a sharp rise (>2pp) would falsify the Katzenstein filter (niche reinforcement, not independent activation).*

**At BIS Triennial 2037:**

BRL does NOT gain reserve share without capital account opening.
*Falsify if: BRL FX turnover rises without Chinn-Ito KAOPEN improvement.*

This is the paper's only negative forward prediction. Brazil has the second-largest
thorium reserves, active nuclear capacity, and middle-tier institutions. The
prediction that BRL does not activate without capital account reform tests the
institutional quality term directly: if energy position alone were sufficient, Brazil
should gain share regardless of KAOPEN. If institutional quality is necessary,
Brazil cannot activate until KAOPEN improves. The BIS 2037 data will distinguish
these.

**The cross-case Katzenstein prediction (ongoing):**

India will gain FX turnover share as nuclear capacity grows; Australia will not gain
disproportionately despite AUKUS. If both gain independently, the alliance-structure
filter is refuted. If neither gains, the mechanism fails. The cross-case contrast
across all BIS Triennial surveys from 2028 through 2037 is the paper's most sustained
empirical test.

## 8.5 The Synthesis Argument

The three legs do not merely add up. Each one changes what the others mean.

The backward leg, standing alone, establishes that the EU carbon governance regime
exhibits political construction — ZA break at a political event, GS=2.79 far above
the RGGI equivalent. A useful finding, but limited: it could be read as a contingent
feature of one poorly designed market.

The present leg, standing alone, establishes a correlation between NEP and reserve
share across two structured cases and a natural experiment. Suggestive, but
explicable: energy-rich states may be wealthy states, and wealthy states issue reserve
currencies for other reasons.

Together, they establish something neither can establish alone: **the mechanism that
produced historical reserve currency outcomes is the same mechanism the backward leg
shows to be politically constructed and contestable.** The present leg is not a
correlation between geology and monetary power. It is a correlation between governance
outcomes — politically negotiated energy positions — and monetary power. GS > 1 in
the backward leg transforms the interpretation of the present leg. NEP is not an
exogenous endowment. It is the accumulated product of allocation decisions, pipeline
diplomacy, and domestic energy policy. States *choose* their NEP trajectories through
governance, and the monetary outcomes follow with a generational lag.

The forward leg, standing alone, is a TMPI ranking — a static snapshot of structural
endowment. With the backward and present legs established, it becomes something more:
**a map of which states will face the governance design problem of the thorium era.**
The TMPI ranking is not a ranking of geological fate. It is a ranking of structural
position from which states must construct politically durable allocation regimes — or
fail to, as the carbon era's architects failed, and watch the monetary potential of
their endowment be captured or contested away.

Russia brings this synthesis into focus. Its MPI trajectory — strong endowments,
permanently suppressed by GS=0.011 — is not an anomaly. It is the mechanism at
maximum visibility. The backward leg shows exclusion from governance infrastructure
is politically constructed (SWIFT, EU ETS expulsion). The present leg shows the
corridors that formed track pre-existing energy geography (ruble-yuan, ruble-rupee
traced bilateral supply routes of decades). The forward leg shows that TMPI potential
is real but monetarily inert without access to the governance infrastructure that
converts it into reserve status. Russia holds all three components of the mechanism
simultaneously, in extremis. It is the clearest illustration of the paper's central
claim: governance is the variable, not geology.

This is the synthesis the three temporal legs produce together. The transition from
the carbon era to the thorium era is not a technological event that happens to states.
It is a political contest that states enter from unequal structural positions —
positions the backward leg shows are politically constructed, the present leg shows
have monetary consequences, and the forward leg maps for the next round. The backward
test does not prove the thorium era will be politically contested. But it would be
extraordinary if it were not. Every major energy transition in the historical record
involved a renegotiation of the governance regimes that made the prior era's energy
positions into monetary leverage. There is no mechanism in the framework — and none
in the historical record — by which the thorium era would be different.
