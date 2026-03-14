# §1 — Introduction

In 1944, the United States dollar became the anchor of the postwar monetary order at
Bretton Woods. The standard explanation for this outcome emphasises American economic
size, the depth of its financial markets, and the institutional architecture its
negotiators imposed. These explanations are not wrong. But they are incomplete. The
dollar did not simply follow American GDP. It followed American energy. The United
States was the world's dominant oil producer from the 1860s through the 1970s — a
position that underwrote the industrial capacity, trade surpluses, and geopolitical
leverage from which monetary hegemony was constructed. The sterling-dollar transition
of the twentieth century was simultaneously a coal-oil transition. No existing framework
in international political economy makes that connection formally.

This paper proposes one.

We develop the **Monetary Power Index** (MPI), a theoretical framework that formalises
the relationship between energy sovereignty and monetary power across energy eras:

```
MPI_{i,t} = (1 − p_t) · [NEP_{i,t−λ} · GS_{i,t}]  +  p_t · [TMPI_i · GS_{i,t+τ}]
```

The first term captures monetary power in the *present* energy era: Net Energy Position
(NEP) — production share minus net import share in world primary energy, lagged λ years
— multiplied by Governance Sensitivity (GS), the degree to which the energy allocation
regime is politically constructed rather than geologically fixed. The second term captures
monetary power in the *next* era: the Thorium Monetary Potential Index (TMPI), a
composite of thorium reserve endowment, nuclear capacity, and institutional quality,
multiplied by the governance sensitivity of the emerging regime. The transition
probability p_t weights the two — at p_t=0 the equation reduces to a present-era
regression; at p_t=1 it reduces to a forward ranking. Between 0 and 1 it maps every
country's monetary power trajectory as the energy transition progresses.

We test the framework across three temporal registers.

The **backward leg** establishes the premise: energy governance regimes are politically
contested, not geologically determined. We test this on the EU Emissions Trading System
(2005–2024) using the Zivot-Andrews structural break test on the allocation surplus
series. The break falls in 2014 (stat=−6.248, p=0.0006), aligned with the Phase III
structural reform — a political decision, not a commodity supply shock. We then compare
price volatility across carbon markets: EU ETS Phase I exhibits a coefficient of
variation of 0.815, nearly 17 times higher than the US Regional Greenhouse Gas
Initiative (RGGI) in its first compliance period (CV=0.047). Both are synthetic carbon
permits. RGGI was actually *more stable than the oil market* (oil CV=0.292). The
difference is entirely attributable to the EU's politically constructed allocation
rules. Energy governance is a policy variable, not an exogenous endowment.

The **present leg** tests whether the mechanism operates: does NEP predict reserve
currency share with a generational lag? We estimate entity-specific ARDL bounds tests,
error correction models, and DOLS regressions for six reserve currency entities
(1995–2024). Two structured cases emerge. In the United States, where NEP rose through
the shale revolution, the ARDL bounds test confirms cointegration; USD reserve share
has stabilised since 2021, approximately λ=10 years after peak shale output —
consistent with the mechanism operating on schedule. In the eurozone, where NEP
declined from 0.010 (1999) to 0.005 (2024) as North Sea reserves depleted and import
dependence rose, EUR reserve share tracked the decline with a 10-year lag
(r=0.864, n=16). The LOO jackknife — dropping USA flips β from +84 to −3 — is
not a weakness: it is evidence of two structured cases with opposite-sign slopes that
pooled OLS cannot distinguish. Japan's post-Fukushima experience provides an
exogenous test: NEP dropped 61% in two years following the 2011 nuclear shutdown;
yen reserve share has been stagnant since. Switzerland holds 13–22% of global
central bank reserves with near-zero NEP — not a falsification but an instance of
institutional substitution in a financial entrepôt.

The **forward leg** asks where the mechanism points next. If energy transitions
determine monetary trajectories, and if thorium-based nuclear power becomes the
dominant energy input of the mid-21st century, which states hold the structural
position to convert that endowment into monetary leverage? We construct the TMPI as
a multiplicative index of thorium reserve share, nuclear energy share, and
institutional quality. The top-three ranking — USA (100), Canada (20.8), India (15.8)
— is scenario-invariant across Low/Base/High transition assumptions (3%/10%/20%
nuclear share by 2040). More importantly, the full MPI framework reveals the trajectory
that static rankings obscure: India's current NEP is negative (net energy importer),
suppressing its present-era monetary power. But as p_t rises with the transition,
India's MPI rises discontinuously — driven by the world's largest thorium reserves
and an active three-stage nuclear programme. No present-era regression produces this
prediction. The two-state MPI does.

---

**What this paper contributes and what it does not claim.**

Strange (1988) identified finance and energy as two of the four structures of structural
power but never formalised their interaction or its evolution across eras. Eichengreen
(2011) and the reserve currency literature estimate the determinants of reserve share
in the present era — trade volumes, financial depth, institutional quality — without
an energy term. Stigler's (1971) regulatory capture framework describes how politically
connected interests shape allocation regimes but carries no monetary dimension and no
temporal architecture. This paper connects these three traditions in a single framework:
Strange's pillars, operationalised across energy eras, with Stigler's insight that
allocation regimes are politically constructed rather than technically optimal.

We make three targeted claims, not a general theory of monetary hegemony. First: energy
governance regimes are politically constructed — GS > 1 is estimable and significantly
above unity for the EU carbon era. Second: NEP predicts reserve share with a generational
lag for the two structured cases in which the mechanism can be identified. Third: TMPI
maps the forward distribution of monetary potential under the next energy transition,
with falsifiable predictions at dateable checkpoints.

We do not claim causal identification in the treatment-effects sense. The correct
epistemological framing is historical political economy: we document a structural
relationship across three temporal registers and derive falsifiable predictions. This
is the standard for theoretical framework papers in this literature, not a weakness.

We do not claim that energy is the sole determinant of monetary power. Switzerland
holds substantial reserve share with near-zero energy production — institutional quality
and financial entrepôt status can substitute. The mechanism is probabilistic and
operates over decades, not quarters.

What we do claim is that any framework for understanding the evolution of the
international monetary system that omits the energy-governance nexus will systematically
mispredict transitions — as it has for every major reserve currency shift in the past
two centuries, and as it is currently doing for the next one.

---

**Structure of the paper.**

Section 2 reviews the literature on reserve currency determinants, structural power,
and carbon market political economy, identifying the gap this paper fills. Section 3
presents the MPI framework formally and derives the causal chain connecting its three
components. Sections 4, 5, and 6 present the backward, present, and forward empirical
legs respectively. Section 7 assembles the MPI trajectories as p_t varies, with Russia
as the hinge case that threads all three legs. Section 8 presents the unified
falsification registry — time-bound, checkable predictions that would refute the
framework's central claims. Section 9 concludes.
