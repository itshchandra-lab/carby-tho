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
rules. Energy governance is a policy variable, not an exogenous endowment. This has
a further implication that links the backward leg to the forward: if carbon prices
are politically constructed rather than market-cleared, the carbon governance regime
cannot function as a credible anchor for sovereign energy policy. A monetary
arrangement partly calibrated to the carbon era is therefore structurally unstable —
not because of bad policy, but because the allocation regime is contested by design.
The thorium transition does not arrive from outside the system. It is already latent
in the carbon era's failure to produce an authoritative, de-politicised allocation
mechanism.

The **present leg** tests whether the mechanism operates: does NEP predict reserve
currency share with a generational lag? The cleanest identification comes from Japan.
Japan has the world's third-largest economy, deep financial markets, and every GDP-
level predictor that the standard literature (Eichengreen 2011; Cohen 2015) would use
to forecast reserve currency status — yet the yen has held 5–6% of global reserves
for three decades, far below its GDP weight. The mechanism explains this directly:
Japan is a chronic net energy importer with near-zero NEP, and post-Fukushima the
position worsened sharply — NEP dropped 61% in two years following the 2011 nuclear
shutdown; yen reserve share has been stagnant since. Japan is not anomalous. It is
the control case that isolates the energy variable's independent effect against the
GDP null hypothesis.

We estimate entity-specific ARDL bounds tests, error correction models, and DOLS
regressions for six reserve currency entities (1995–2024). Two structured cases
corroborate the mechanism in opposite directions. In the United States, where NEP rose
through the shale revolution, the ARDL bounds test confirms cointegration; USD reserve
share has stabilised since 2021, approximately λ=10 years after peak shale output —
consistent with the mechanism operating on schedule. In the eurozone, where NEP
declined from 0.010 (1999) to 0.005 (2024) as North Sea reserves depleted and import
dependence rose, EUR reserve share tracked the decline with a 10-year lag (r=0.864,
n=16). The LOO jackknife — dropping USA flips β from +84 to −3 — is not a weakness:
it is evidence of opposite-sign slopes that pooled OLS cannot distinguish. Switzerland
holds 13–22% of global central bank reserves with near-zero NEP — institutional
quality and financial entrepôt status can substitute for energy position, a boundary
condition the framework anticipates.

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

**What this paper contributes and what it does not claim.**

Hegemonic Stability Theory (HST) — Kindleberger (1973), Gilpin (1981) — provides the
closest prior framework: reserve currency status follows from the structural power of
the hegemonic state. Our argument is a specification of HST's production dimension,
not a rejection of it. HST describes the correlation (structural power → monetary
dominance) but does not specify what structural power is made of at the production
level. MPI provides that specification: energy governance, contested and lagged, is
the causal mechanism beneath the correlation HST tracks. This is why HST cannot predict
transitions — it treats structural power as given rather than derived from the energy
base that produces it. When the energy base shifts, HST observes the outcome after the
fact. MPI observes the preconditions before it.

Strange (1988) identified finance and energy as two of the four structures of structural
power but never formalised their interaction across eras. The Japan case illustrates
why this matters: Japan commands Strange's finance and knowledge structures but lacks
production autonomy — and its reserve share reflects exactly that deficit. Strange's
framework predicts this outcome; MPI specifies the mechanism that produces it. We
extend Strange's synchronic account into a dynamic one by formalising how the
finance-energy interaction *reproduces across* energy transitions.

The "architecture of monetary failure" in our title is technical, not normative. Monetary
architectures are built atop energy bases; when those bases transition, the architecture
faces structural obsolescence. This is a Polanyian claim about the disembedding of monetary
arrangements from their material foundations — not a claim that incumbents have failed by
any moral standard. Helleiner (2014) showed why the 2008 crisis did not dislodge dollar
primacy: the absence of a credible alternative and the inertia of network effects
preserved the existing architecture. Our claim is different: the next dislodging force
is not a financial crisis but an energy transition, and that transition is already
detectable in the data.

We make three targeted claims, not a general theory of monetary hegemony: energy
governance regimes are politically constructed (GS > 1 estimable); NEP predicts reserve
share with a generational lag in the two structured cases where the mechanism is
identified; TMPI maps the forward distribution of monetary potential with falsifiable
predictions at dateable checkpoints. We do not claim causal identification in the
treatment-effects sense — the correct framing is historical political economy with
falsifiable forward predictions. Any framework that omits the energy-governance nexus
will systematically mispredict reserve currency transitions, as every standard account
has for every major transition of the past two centuries.

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
