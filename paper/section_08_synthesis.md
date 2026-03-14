# §8 — Synthesis: MPI Trajectories, Russia as the Hinge, and the Falsification Architecture

## 8.1 Assembling the MPI

The three empirical legs each estimate one component of the MPI framework. This section
assembles them into the full two-state expression and derives the forward trajectories
as p_t varies from 0 to 1.

**Component estimates:**
- GS_{EU ETS, Phase I} = 0.815 / 0.292 = 2.79, normalised to GS_norm ≈ 0.85
  (common to all entities in State 0; cross-entity estimation is future work)
- GS_RUS = 0.05 post-2022 (sanctions exclusion from Western monetary infrastructure)
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
prediction is that 2028 shows measurable gain.

**At BIS Triennial 2031:**

INR FX turnover share approaches 3–5%.
*Falsify if: INR share <2% in BIS 2031 despite programme completion.*

**At IMF COFER 2035–2040:**

AUD reserve share maintained or increased post-AUKUS nuclear capacity.
*Falsify if: AUD share declines after AUKUS nuclear capacity comes online.*

Note: the Katzenstein filter predicts AUD niche *reinforcement*, not independent
growth. The falsification here is weaker than India's: if AUD share falls after
AUKUS nuclear capacity, the niche reinforcement prediction fails. If AUD share
rises disproportionately, the Katzenstein filter — not the TMPI — is refuted.

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

## 8.5 What the Three Legs Together Establish

The backward leg establishes that energy governance is a policy variable, not a
geological constant. Without this, the forward leg's predictions would be descriptions
of fate, not strategic stakes.

The present leg establishes that the mechanism has operated historically: two
structured cases (USA, EMU) with opposite energy trajectories and opposite reserve
share trajectories, a natural experiment (Japan/Fukushima), and a boundary condition
(Switzerland) that identifies the scope conditions. The mechanism is real.

The forward leg establishes where the mechanism points next: India rising, Australia
niche-reinforcing, Russia endowed but constrained, UK declining, Brazil blocked. These
are predictions derived from the mechanism estimated in the present leg, applied to
the structural endowments measured in the forward leg, weighted by the transition
probability that the backward leg shows to be politically — not technologically —
determined.

Together they constitute a theoretical framework with empirical illustration and
falsifiable forward predictions. Strange (1988) identified the pillars. This paper
formalises their interaction across time and derives where they point next. The falsification
dates are in the registry. The window for the next great transition is open. The backward
test proves it will not stay open by default.
