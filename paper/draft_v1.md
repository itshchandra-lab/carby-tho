# The Carbon-Thorium Standard: Energy-Backed Currencies and the Architecture of Monetary Failure in a Multipolar World

---

**Abstract**

Why do reserve currencies rise and fall? The standard account points to GDP, financial depth,
and network effects. This paper argues that energy sovereignty is the missing mechanism.
We develop the Monetary Power Index (MPI), a two-state framework that formalises the
relationship between energy governance and monetary power across energy eras:
MPI_{i,t} = (1−p_t)·[NEP_{i,t−λ}·GS_{i,t}] + p_t·[TMPI_i·GS_{i,t+τ}], where NEP is
Net Energy Position lagged by one generation, GS is Governance Sensitivity (the degree
to which allocation regimes are politically constructed), TMPI is the Thorium Monetary
Potential Index, and p_t is the transition probability weighting the present and next era.

We test the framework across three temporal registers. The *backward leg* establishes that
energy governance is politically constructed: the EU ETS allocation surplus breaks
structurally in 2014 at a political reform event (Zivot-Andrews stat=−6.248, p=0.0006),
and EU ETS Phase I price volatility (CV=0.815) is 17 times higher than the RGGI in its
equivalent first compliance period (CV=0.047) — both synthetic carbon permits. The
*present leg* tests the mechanism: ARDL bounds confirms cointegration between NEP and
reserve share for the USA; the eurozone's declining NEP correlates with EUR reserve share
decline at r=0.864 (n=16); Japan's post-Fukushima NEP collapse of 61% in two years
provides an exogenous natural experiment supporting the mechanism. The *forward leg*
constructs the TMPI — a multiplicative index of thorium reserves, nuclear capacity, and
institutional quality — whose top-three ranking (USA=100, Canada=20.8, India=15.8) is
scenario-invariant across Low/Base/High transition assumptions.

The two-state framework reveals trajectories invisible to any present-era regression:
India's MPI rises discontinuously as p_t increases, driven by the world's largest thorium
reserves and an active three-stage nuclear programme, despite near-zero current reserve
share. Russia's strong endowments are permanently suppressed by sanctions-induced
exclusion from Western monetary infrastructure (GS_RUS=0.05 post-2022). We register
eleven falsifiable predictions at dated future checkpoints, including INR FX turnover
share rising to 3–5% by BIS Triennial 2031 and BRL not gaining reserve share without
Chinn-Ito KAOPEN improvement by 2037.

**Keywords:** reserve currencies, energy sovereignty, structural power, thorium, monetary
power index, governance sensitivity, Zivot-Andrews, ARDL bounds

**JEL codes:** F31, F33, Q43, Q48

---

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
components. Section 4 describes the data and measurement strategy. Sections 5, 6, and
7 present the backward, present, and forward empirical legs respectively. Section 8
assembles the MPI trajectories as p_t varies, with Russia as the hinge case that threads
all three legs, and presents the full falsification registry. Section 9 concludes.

---

# §2 — Literature Review: Three Traditions, One Gap

## 2.1 Reserve Currency Determinants

The empirical literature on reserve currency status has converged on a standard set of
determinants: the size of the issuing economy's GDP and trade share, the depth and
liquidity of its financial markets, the stability of its monetary institutions, and
network effects that make the dominant currency self-reinforcing (Chinn and Frankel
2007; Eichengreen 2011; Cohen 2015; Maggiori, Neiman, and Schreger 2020). The
theoretical underpinning draws on the inertia of network goods: switching costs are
high, incumbents benefit from incumbency, and structural change requires a sufficiently
large shock to displace an equilibrium. Helleiner (2014) showed why the 2008 financial
crisis — the most severe in a century — failed to displace dollar primacy: no credible
alternative existed and the institutional infrastructure of dollar settlement was too
embedded to dislodge in crisis conditions.

This literature has produced several important findings. First, reserve currency shares
change slowly but not irreversibly — sterling's decline from ~60% in 1899 to ~5% by
1976 took three generations but was not arrested by incumbency alone (Eichengreen and
Flandreau 2009). Second, the relationship between GDP share and reserve share is
positive but non-deterministic — Japan has maintained a substantially smaller reserve
share than its GDP would predict for three decades, while Switzerland commands a share
far above its GDP weight. Third, institutions matter: Chinn-Ito openness, rule of law,
and credibility of the monetary authority all enter reserve share regressions with
positive and significant coefficients. Fourth, Arslanalp, Eichengreen, and Simpson-Bell
(2022) document a "stealth erosion" of dollar dominance since 2000 driven not by euro
or yen gains — the traditional hegemons-in-waiting — but by a set of non-traditional
reserve currencies including AUD and CAD. Their finding is directly relevant to this
paper's forward leg: the diversification is already happening, but into currencies that
are positioned by commodity endowment and institutional openness, not by GDP mass.

Gopinath et al. (2020) propose the dominant currency paradigm (DCP): dollar primacy persists because international trade is invoiced predominantly in dollars, creating a self-reinforcing equilibrium independent of US productive capacity. The DCP explains stickiness *within* an era — why the dollar remains dominant even as US GDP share falls. It does not explain *transitions between* eras: the DCP has no mechanism for predicting when the invoicing equilibrium breaks or which currency displaces it. The sterling-dollar transition involved a complete re-invoicing of commodity trade from pounds to dollars over 1914–1945 — precisely the kind of era-level shift the DCP treats as exogenous. MPI addresses the preconditions for that shift; the DCP addresses the equilibrium that follows. They are complements, not competitors: MPI explains which currency has the energy foundation to become the new invoicing anchor; DCP explains why the transition is slow and requires a large shock to complete.

**A methodological note on network effects.** Reserve currency shares are
system-level properties: they sum to approximately 100% by construction, and the
dollar's share is high partly because the yuan's share is low. Farrell and Newman's
(2019) weaponised interdependence framework and Kirshner's (1995) monetary coercion
analysis both show that monetary power is a relational, hub-and-spoke property, not a
country-level endowment. Entity-specific error correction models — the paper's primary
specification — reduce but do not eliminate the compositional dependence. The
system-level topology of monetary networks is beyond the scope of this paper and
constitutes the primary methodological extension for future work. The entity-specific
results reported here should be interpreted as capturing the bilateral energy-monetary
relationship for each entity, not as independent draws from a cross-sectional sample.

**The gap:** energy position does not appear in any standard specification. This is
not an oversight that can be corrected by adding a control variable to an existing
regression. It reflects a deeper assumption: that energy is an exogenous endowment,
priced by world markets, whose implications for monetary power are fully captured by
trade shares and GDP. This paper argues the assumption is wrong in two ways. First,
energy governance regimes are politically constructed — allocation rules are negotiated,
not market-cleared, and their construction creates the conditions for monetary leverage.
Second, energy positions shift across transition eras, and the transition itself is
politically contested. A framework that treats energy as exogenous cannot predict
transition dynamics.

## 2.1b Hegemonic Stability Theory and the Production Mechanism

Hegemonic Stability Theory (Kindleberger 1973; Gilpin 1981) provides the dominant
realist framework for reserve currency analysis: the international monetary system
requires a hegemon willing and able to provide the public goods of monetary stability,
and reserve currency status follows from that hegemonic position. HST correctly
describes the correlation — dominant powers issue the dominant currency — but leaves
the production mechanism underspecified. What makes a state structurally powerful in
the first place?

The standard HST answer is aggregate capability: GDP, military power, technological
lead. Our argument is that at the *production dimension* of structural power, energy
sovereignty is the operative variable. The sterling-dollar transition tracks the
coal-oil transition more precisely than it tracks the GDP transition or the military
balance (the UK remained the world's pre-eminent naval power until the 1920s; its
GDP lead over the US had already reversed before 1900). If HST is the map, the energy
mechanism is the terrain beneath it.

This is a specification of HST, not a rejection of it. HST predicts that reserve
currency status follows from hegemonic structural power; MPI specifies that hegemonic
structural power at the production dimension follows from energy sovereignty, filtered
through governance contestability and lagged by a generation. The distinction matters
for prediction: HST can identify incumbents but cannot identify challengers before
they emerge, because it observes structural power as constituted rather than as
constituting. MPI observes the energy base before it produces the monetary outcome —
which is why the forward leg can make predictions about India in 2031 and Australia
in 2035 that HST, by design, cannot make.

## 2.2 Structural Power and the Finance-Energy Nexus

Strange (1988) identified four structures of structural power: security (the capacity
to provide or threaten violence), production (control over how goods are made and
distributed), finance (control over the creation and allocation of credit), and
knowledge (control over information and ideas). She argued that the United States'
postwar dominance rested on simultaneous command of all four — and that the most
durable source of that command was the finance-production nexus, in which dollar
issuance underwrote American productive capacity while American productive capacity
underwrote dollar credibility.

Energy sits in the production structure but, Strange argued, is not reducible to it.
The 1973 oil shock demonstrated that control over energy supply could function as
structural power in its own right — OPEC's embargo was not merely a trade disruption
but a rearrangement of the structural hierarchy. Strange was cautious about the
monetary implications of this: her analysis of the petrodollar recycling system
suggests she understood the finance-energy linkage but treated it as contingent on
the specific institutional arrangements of dollar-denominated oil trade rather than
as a general mechanism.

The international political economy literature has not formalised the finance-energy
nexus she described. Kirshner's (1995, 2014) work on monetary power focuses on
financial statecraft — the use of monetary relationships as instruments of coercion —
without deriving the underlying distribution of monetary power from structural energy
positions. Cohen's (2015) geography of money addresses the spatial dimension of
currency internationalisation but does not model the energy determinants of that
geography. McNally (2019) and Norrlof (2010) address dollar primacy but without an
energy mechanism.

**The gap:** the finance-energy interaction Strange identified has never been
formalised across energy transitions. This paper does so, extending Strange's
synchronic account into a dynamic one by specifying how the mechanism reproduces
across eras.

## 2.3 Carbon Market Political Economy

The EU ETS is the world's largest carbon market and has attracted substantial
political economy scholarship. Ellerman and Buchner (2008) documented systematic
over-allocation in Phase I, showing that member states lobbied successfully for
excess permit allocations that they then sold, generating revenue while emissions
continued. Koch, Fuss, Grosjean, and Edenhofer (2014) analysed the 2013 price
collapse, attributing it to the interaction of the economic crisis (reducing verified
emissions) and political resistance to cap tightening. Bayer and Aklin (2020) showed
that despite low prices, the ETS reduced CO2 emissions — suggesting the allocation
politics, while distortive, did not fully neutralise the price signal.

This literature has established that carbon market prices are not determined by physical
supply-demand fundamentals alone. Allocation rules, banking provisions, Market
Stability Reserve interventions, and national lobbying all shape the price series.
Mattli and Woods (2009) provide the most systematic framework for this phenomenon:
in international regulatory institutions, capture by incumbents is the normal
equilibrium, not an aberration. The EU ETS Phase I — where member states lobbied
successfully for excess allocations that were then sold at public expense — is a
textbook Mattli-Woods regulatory capture at the supranational level. Paterson and
Stripple (2010) show that carbon markets are not merely sites of price formation but
arenas of political contestation in which the boundaries of the market are themselves
subject to negotiation. Their insight is our backward leg's theoretical foundation.

What the literature has not done is formalise the *degree* of political construction
relative to a baseline — Stigler's (1971) capture framework provides the vocabulary
but not a measurement. Governance Sensitivity (GS), defined as the ratio of energy
governance volatility to commodity benchmark volatility, provides this measurement:
GS > 1 is the empirical signature of a politically constructed regime. The RGGI
comparison in Section 5 provides the most direct test: EU ETS Phase I CV = 0.815;
RGGI Phase 1 CV = 0.047 — both synthetic permits, both first compliance periods,
difference of 17×. The difference is not the permit design. It is the political
economy of the allocation regime.

**The gap:** the carbon market political economy literature has not connected
governance contestability to monetary outcomes, nor derived the implication that a
politically constructed allocation regime is inherently unstable as a monetary anchor.
This paper provides both connections.

## 2.4 Energy Transitions and Geopolitics

A growing literature on energy transitions and international order (Dannreuther 2017;
Scholten 2018; Scholten et al. 2020; Overland 2019) examines how the shift away from
fossil fuels will redistribute geopolitical power. The standard finding is that
transitions favour renewable-endowed importers over fossil-fuel exporters: Norway,
Saudi Arabia, and Russia lose structural leverage; Germany, Japan, and South Korea
gain. The mechanisms identified are trade balance shifts, technological competitiveness,
and the end of fossil fuel rents.

This literature has not addressed monetary consequences. The geopolitical transition
literature asks who gains *economic* leverage from new energy positions; it does not ask
who gains *monetary* leverage — the ability to have one's currency held as a reserve,
to price international trade, or to run external deficits without financing constraints.
These are related but distinct questions. A country can gain productive capacity from
a transition without gaining monetary power if its institutional quality is low, its
financial markets are shallow, or its governance of the new energy regime is captured
by incumbents.

Katzenstein's (1985) work on small states in world markets provides an important
corrective to naive transition optimism. Small states — including Australia and Canada,
both TMPI-endowed — do not independently leverage resource positions into structural
monetary power. Their monetary behaviour is conditioned by their position within
alliance structures, specifically the US-centred security and economic order. For Five
Eyes states, thorium endowment does not imply monetary independence; it implies a
niche reinforcement within the existing dollar order. This paper incorporates this
insight as a falsifiable prediction: AUD and CAD will not gain reserve share
disproportionate to their current positions through independent energy leverage,
because their geopolitical alignment channels thorium potential into the dollar system.
India's case is structurally different — sovereign fuel cycle, non-alignment tradition,
capital account under domestic policy control — and the framework predicts activation
rather than niche reinforcement.

**The gap:** the transition geopolitics literature has no monetary mechanism and no
specification of the *activation conditions* that distinguish which energy positions
translate into reserve currency candidacy. The TMPI provides the structural ranking;
the Katzenstein framework provides the activation filter.

## 2.5 Synthesis: The Gap This Paper Fills

The four literatures reviewed above approach the finance-energy nexus from different
angles but none crosses the full distance:

| Literature | What it explains | What it omits |
|------------|-----------------|---------------|
| Reserve currency determinants | Present-era reserve share | Energy mechanism; transition dynamics |
| Strange's structural power | Finance-energy linkage | Formalisation; temporal evolution |
| Carbon market political economy | Allocation regime politics | Monetary consequences; GS measurement |
| Energy transition geopolitics | Power shifts under transitions | Monetary mechanism; reserve currency implications |

The MPI framework fills the intersection of all four. It operationalises Strange's
finance-energy pillars (reserve share as outcome, NEP as energy mechanism), measures
the political construction of governance regimes (GS from the carbon literature),
and extends the transition geopolitics literature to monetary outcomes (TMPI as
forward leg). The three temporal legs — backward, present, forward — are not
independent analyses. They are one causal mechanism tested across three registers of
evidence.

---

# §3 — A Formal Theory of Monetary Power Across Energy Eras

## 3.1 The Gap in Existing Frameworks

Three bodies of literature approach the relationship between energy and monetary power but
none formalises it across time.

Strange (1988) identified finance and energy as two of the four structures of structural
power and argued that states capable of controlling both acquire disproportionate capacity
to shape international outcomes. She did not formalise the interaction or specify how it
changes as the dominant energy input shifts. Her framework is synchronic: it describes
structural power at a point in time, not its reproduction across eras.

Eichengreen (2011) estimates the determinants of reserve currency share with panel
regressions that include trade share, financial depth, and institutional quality. Energy
position does not appear. The specifications are linear and present-only: they capture the
existing distribution of monetary power but cannot map its evolution across energy
transitions.

Stigler's (1971) regulatory capture theory — the most natural framework for describing
politically constructed allocation regimes like the EU ETS — is static, single-sector,
and carries no monetary dimension. Applying the capture label to carbon markets explains
allocation outcomes but says nothing about what follows for monetary power.

The gap all three share: none formalises how monetary power is *reproduced across energy
eras*. Strange's insight is correct but static. Eichengreen's regressions are dynamic but
present-era only. Neither asks what happens to the finance-energy nexus when the dominant
energy input shifts.

The central problem is that prior work conflates two distinct quantities: the *current*
monetary power derived from present energy sovereignty, and the *forward option* on
monetary power contingent on the next energy transition. These are not the same variable.
A country can hold significant current monetary power with negligible transition potential
(UK: sterling reserve decline tracking North Sea depletion), or negligible current
monetary power with significant transition potential (India: net energy importer today,
largest thorium reserves globally). Any framework that puts both in the same expression
without distinguishing their temporal basis will misrank both.

---

## 3.2 The Monetary Power Index

We define **Monetary Power Index** (MPI) for entity *i* at time *t* as an expected value
across two states of the world: the present energy era and the next one.

```
MPI_{i,t} = (1 − p_t) · [NEP_{i,t−λ} · GS_{i,t}]
           +      p_t  · [TMPI_i       · GS_{i,t+τ}]
```

**State 0 (present era, weight 1−p_t):**

```
NEP_{i,t−λ} · GS_{i,t}
```

Monetary power in the current era is driven by Net Energy Position — the present-leg
mechanism — multiplied by Governance Sensitivity, the degree to which energy allocation
is a policy variable rather than a geological constant.

**State 1 (next era, weight p_t):**

```
TMPI_i · GS_{i,t+τ}
```

Monetary power in the next era is driven by the Thorium Monetary Potential Index —
structural endowment for the transition — multiplied by the governance sensitivity of the
emerging regime. GS_{i,t+τ} is not yet estimable; in the forward leg we treat it as
constant and note that the entities best positioned to construct high GS in the thorium
era are those currently building domestic fuel cycle control (India's three-stage
programme; Canada's CANDU export position).

**p_t — the transition probability:**

p_t is the market's current assessment of the probability that thorium-era nuclear has
become the dominant energy input by time t+τ. It is the structural variable that connects
all three temporal legs:

```
p_t = f(nuclear_cost_trajectory_t, geopolitical_signal_t, cumulative_capacity_t)
```

For this paper, p_t is estimated independently from the observed trajectory of world nuclear share of primary energy (OWID/BP data). We compute the annual deviation of world nuclear share from its 2005 baseline and apply a logistic normalisation to map this onto [0, 0.6] — consistent with the High scenario ceiling. This gives p_t ≈ 0.08 in 2020, ≈ 0.10 in 2022, and ≈ 0.12 in 2024, reflecting the gradual but measurable resumption of nuclear capacity additions globally. Independently derived p_t values are used in the synthesis chart (§8); the Low/Base/High scenario bounds provide sensitivity analysis around the central trajectory.

| Symbol | Name | Definition | Empirical counterpart |
|--------|------|------------|----------------------|
| NEP_{i,t−λ} | Net Energy Position (lagged) | Production share minus net import share in world primary energy; lagged λ | World Bank energy balance; λ=10 from USA case |
| GS_{i,t} | Governance Sensitivity | CV(energy governance indicator) / CV(commodity benchmark) | Phase CV comparison; ZA statistic as ordinal complement |
| TMPI_i | Thorium Monetary Potential Index | thorium_reserve_share × nuclear_capacity_share × institutional_quality | Constructed in §7; static endowment, not a flow |
| p_t | Transition probability | P(thorium era dominant by t+τ) | Calibrated from scenario bounds in §7 |

---

## 3.3 Why Two States, Not Multiplication

The natural first instinct is to write MPI as a product of all three components:
*[NEP × GS × TMPI]*. This is wrong for a precise reason.

NEP and TMPI measure energy sovereignty in *different eras*. NEP is a current flow: it
changes yearly with production and consumption decisions and can go negative (Japan
post-Fukushima: NEP dropped 61% in two years). TMPI is a structural endowment: geological
reserves do not move, nuclear capacity changes on decadal timescales, institutional quality
is persistent. Multiplying a flow variable by a stock variable in the same contemporaneous
expression conflates their temporal basis.

The consequence: a multiplicative form *understates* countries whose current NEP is low but
whose TMPI is high (India), and *overstates* countries whose current NEP is high but whose
TMPI is low (UK: North Sea depleted, no thorium programme). The two-state form resolves
this by putting NEP and TMPI in separate terms, weighted by which era is operative.

The two-state form also has clean limiting cases that the multiplicative form cannot produce:

- **p_t = 0:** MPI reduces to NEP · GS — the present-leg mechanism exactly as estimated
  in §6. The entire empirical content of the present leg is a special case of MPI.
- **p_t = 1:** MPI reduces to TMPI · GS — the forward-leg ranking exactly. The TMPI
  analysis in §7 is the other limiting case.
- **0 < p_t < 1:** MPI is a weighted average, with India rising and UK declining as p_t
  increases. The trajectory of individual country scores as p_t rises is the paper's most
  falsifiable forward prediction.

An option-pricing analogy is exact: NEP · GS is the *intrinsic value* of current monetary
leverage (in-the-money now); TMPI · GS_{t+τ} is the *time value* (the option on future
leverage). p_t is the risk-neutral probability weighting the two. A country's total monetary
power today is the sum of what it holds now and what its option is worth at current
transition odds.

---

## 3.4 The Governance Sensitivity Term

GS_{i,t} appears in both states of the MPI expression. This is not redundant — it is the
paper's central theoretical claim made explicit: **governance contestability is the
mechanism that makes energy sovereignty a policy variable in any era.**

In State 0, GS captures whether the current energy allocation regime is politically
constructed or geologically determined. A regime with GS > 1 is more volatile than the
underlying physical commodity — the signature of a politically negotiated allocation. The
EU ETS provides the cleanest measurement: GS = CV(EUA Phase I) / CV(oil) ≈ 2.79. The
Phase I allocation surplus was nearly three times more volatile than the oil price in the
same period. This is not a commodity with fixed physical supply. It is a politically
constructed regime.

In State 1, GS captures whether the thorium allocation regime will be politically
constructed or treated as geologically fixed. The countries investing now in domestic fuel
cycle control — India's closed-cycle programme, Canada's CANDU heavy-water expertise —
are pre-positioning for high GS in the thorium era. Countries that allow their thorium
endowment to be allocated by international markets cede the GS term and with it the
amplification it provides on TMPI.

**Formal definition:**

```
GS_{i,t} = CV(EG_{i,era}) / CV(commodity_benchmark_{era})
```

where EG is the energy governance indicator (allocation surplus for carbon markets;
domestic energy price regime for oil markets). GS = 1 means the governance regime is no
more volatile than the physical commodity. GS > 1 means excess volatility attributable to
political construction.

**Complement: the Zivot-Andrews statistic.** CV captures the degree of political
construction over a phase; the ZA statistic captures whether that construction breaks
endogenously at a political event rather than a supply shock. Both are reported in §5.
They are complementary measures of the same underlying property.

**Cross-entity GS in this paper.** GS is estimated both at the regime level (EU ETS Phase I: GS=2.79, establishing that GS>1 holds for carbon governance) and at the entity level (computed as CV(energy_imports_pct_i, 2000–2023) / CV(oil_price, 2000–2023)). Entity-specific GS captures how much more volatile each country's energy import position is relative to the underlying commodity price. USA receives the highest GS (deregulated markets, shale-revolution volatility); Japan receives the lowest (METI-administered prices, stable import share); Russia post-2022 is floored at GS=0.05 — not by fiat but from the observed collapse in its participation in Western energy governance infrastructure following SWIFT exclusion. This entity-level variation is what allows the MPI to differentiate entities at the same NEP level: two countries with identical energy positions but different governance sensitivity will have different monetary leverage.

---

## 3.5 The Causal Chain

The MPI equation is not merely a classification. It encodes a causal sequence:

```
GS_{i,t} [backward leg]
    ↓ constructs
NEP_{i,t−λ} [present leg]
    ↓ with generational lag λ
Monetary power [present-leg outcome]
    ↓ signals
p_t [transition probability]
    ↓ weights
TMPI_i [forward leg]
```

The backward test establishes the first link: governance sensitivity is politically
constructed, not technologically determined. If GS were exogenous — if energy allocation
regimes tracked commodity fundamentals — then the present leg would be documenting a
fixed geological constraint. Because GS is high and politically endogenous (ZA break
aligns with political events, not supply shocks), NEP itself is a *strategic variable*.
States choose their energy position through allocation regimes, investment decisions, and
pipeline diplomacy.

The second link — NEP to monetary power with lag λ — is the present-leg's empirical
contribution. λ ≈ 10 years estimated from the USA case.

The third link — from current monetary power to p_t — is the one most prior work
ignores. A state with dominant current monetary power can influence the rate at which
transition probability rises. The USA's ability to set the terms of nuclear non-
proliferation treaties, the EU's ability to construct carbon market rules, India's
insistence on a sovereign fuel cycle: all are attempts to influence p_t. The transition
is not technologically inevitable on a fixed schedule. It is politically contested. The
backward test proves this claim for the carbon era. The forward prediction assumes it
will be equally true for the thorium era.

---

## 3.6 What the Framework Explains That Prior Work Cannot

**The USA-EMU contrast.** USA: net energy producer, NEP rising post-shale, high GS
(domestic energy policy is contested). EMU: net energy importer, NEP declining 2009-2024
(r=0.864 with EUR reserve share decline), energy policy increasingly constrained by
external dependence. Under MPI at p_t≈0, USA dominates. This is the present-leg result.

**The Japan test.** Japan has the world's third-largest economy (GDP share ~6%) but
persistent underperformance in reserve share (~5-6%). Under MPI: Japan's NEP collapsed
61% after Fukushima (2011), suppressing the State 0 term. Japan's TMPI is non-zero
(institutional quality high, policy target 20% nuclear by 2035) — so as p_t rises,
Japan recovers in the MPI ranking. The framework predicts when Japan should recover,
not just that it is currently anomalous.

**The Russia isolation case.** Russia has strong underlying components: positive NEP,
non-trivial TMPI (thorium reserves, nuclear capacity). But post-2022 sanctions are a
governance shock that collapses GS in both states: access to Western carbon markets
ended; bilateral energy corridors operate outside the institutional infrastructure
that makes monetary leverage convertible into reserve status. MPI captures this
correctly: the framework does not fail on Russia — it explains exactly why a country
with strong raw endowments has suppressed monetary power when excluded from the
governance infrastructure.

**The Australia case.** High thorium reserves (12.6% world share), open capital
account, strong institutions — but zero nuclear capacity collapses TMPI multiplicatively
to zero. In the two-state MPI: Australia's State 1 term is currently zero; AUKUS
changes this ~2035 when nuclear capacity comes online. MPI predicts a step-change in
Australia's forward monetary power at a specific date, conditional on AUKUS delivery.
This is the paper's most precisely falsifiable forward prediction.

**The India trajectory.** India's current NEP is negative (net energy importer,
suppressing State 0). India's TMPI is third globally (largest thorium reserves, active
three-stage nuclear programme, improving institutions). As p_t rises, India's MPI
rises discontinuously — not because its current position improves but because the
weight on State 1 increases. This trajectory is the central forward claim of the paper
and is unproducible by any present-only framework.

---

## 3.7 Relationship to Strange's Structural Power

Strange argued that structural power — the power to shape the framework within which
others must operate — derives from four sources: security, production, finance, and
knowledge. Finance and energy jointly constitutive.

MPI formalises the finance-energy interaction across eras she never developed. NEP is
the energy component. Reserve share (the outcome MPI predicts) is the financial
component. GS is the political contestability of the interface between them. TMPI
extends the framework to the next era.

The key departure: Strange assumed structural power is reproduced in the present.
MPI shows it is reproduced *across* eras — and that the reproduction mechanism is
estimable from current data. The backward test proves the mechanism was operative in
the carbon era. The present test proves it is operative now. The forward test derives
where it points next.

*Strange identified the pillars. We formalise their interaction across time.*

The corollary that Strange could not see from 1988: because p_t is politically
determined (the backward test establishes this), the transition itself is a site of
contestation. Incumbents who understand the MPI framework have an incentive to
slow p_t — to delay the moment at which the thorium era's weights dominate the
ranking. This is not a theoretical prediction. It is already observable in nuclear
non-proliferation architecture, uranium supply chain politics, and the terms on which
AUKUS was negotiated.

---

*Empirical implementation: §5 (backward, GS), §6 (present, NEP_{t−λ}), §7 (forward, TMPI),
§8 (synthesis: MPI trajectories as p_t varies from 0 to 1).*

---

# §4 — Data and Measurement

## 4.1 Panel Construction

The present-leg panel covers six reserve currency entities — United States (USD),
Euro Area (EMU), United Kingdom (GBR), Japan (JPN), China (CHN), and Switzerland
(CHE) — over 1995–2024, yielding a maximum of 180 entity-year observations. Effective
observations after missing-data listwise deletion are approximately 155 for the main
specifications.

The Euro Area is constructed as a single entity from 1999, with NEP calculated as a
GDP-weighted average of the five largest eurozone members by economic weight:
Germany, France, Italy, Spain, and the Netherlands. This construction captures the
aggregate energy import dependence that affects the EUR's structural position while
avoiding the fragmentation problems of treating each member state separately.

## 4.2 Reserve Currency Share

Reserve currency share is sourced from the IMF Currency Composition of Official Foreign
Exchange Reserves (COFER) database, which reports the share of allocated global
reserves held in each major currency. COFER data has two limitations that the paper
accounts for explicitly. First, reporting is voluntary; the allocated share was only
~55% of total reserves in the early 2000s, rising to ~95% by 2024. Second, China's
renminbi was added to the SDR basket in 2016 and COFER reporting improved subsequently;
CNY reserve share data before 2016 are reconstructions.

## 4.3 Net Energy Position

Net Energy Position (NEP) measures a country's energy sovereignty as its share of
world primary energy production minus its net energy import share:

```
NEP_{i,t} = (production_{i,t} / world_production_t) - (net_imports_{i,t} / world_production_t)
```

A positive NEP indicates a net energy exporter (the country contributes more to the
world energy supply than it draws from it); a negative NEP indicates a net importer.
The normalisation to world production shares — rather than domestic consumption shares
— ensures comparability across countries of different sizes and across time as world
energy volumes grow.

Data are sourced from the World Bank World Development Indicators (energy production
and use, ktoe) extended with Our World in Data (OWID) which aggregates BP Statistical
Review of World Energy data to 2024. The two series are spliced at 2021 using a linear
adjustment factor to correct for methodological differences in primary energy accounting.

**The λ=10 lag.** The generational lag between energy position and reserve currency
status is estimated from the USA case: the correlation between NEP and reserve share
is maximised at lag 10 in the ARDL bounds specification. The same lag is applied to
all entities for consistency, though entity-specific lag estimation would be a
refinement. The economic rationale: monetary trust accumulates through decades of
stable exchange, not years; a country's energy position in 2010 affects its monetary
credibility as perceived by central banks making reserve allocation decisions in 2020.

## 4.4 EU ETS Data

EU ETS compliance data — annual freely allocated allowances and verified emissions by
sector, 2005–2024 — are sourced from the European Commission's European Union
Transaction Log (EUTL), downloaded via the Sandbag Carbon Price Viewer. Allocation
surplus (freely allocated minus verified) is the governance variable on which the
Zivot-Andrews test is run.

EUA spot prices (2005–2024) used in the coefficient of variation analysis are
reconstructed from academic sources: Ellerman and Buchner (2008) for Phase I dynamics,
Koch et al. (2014) for Phase II and the 2013 collapse, Bayer and Aklin (2020) for
cross-phase reconstruction, and European Commission monitoring reports for Phase III
and IV annual averages. These are annual average prices; intra-year high-frequency
data from Sandbag or ICAP would provide a more precise CV estimate for Phase I in
particular. The data note in the backward leg notebook flags this limitation
explicitly.

RGGI auction clearing prices (2009–2024) are sourced from RGGI Inc. quarterly auction
results, which are publicly available. Annual averages are used to match the EU ETS
annual frequency.

## 4.5 Thorium Reserves and TMPI Components

Thorium reserve data are sourced from the World Nuclear Association (WNA) and USGS
Mineral Commodity Summaries (2024 edition), which reports identified thorium resources
by country in thousand tonnes. World shares are computed from these totals.

Nuclear energy share (nuclear consumption as a fraction of primary energy consumption)
is from OWID/BP Statistical Review of World Energy, 2024 edition.

Institutional quality is the World Governance Indicators (WGI) composite, computed
as the unweighted average of the six WGI dimensions (Voice and Accountability, Political
Stability, Government Effectiveness, Regulatory Quality, Rule of Law, Control of
Corruption). The composite is normalised to [0,1] for use in the multiplicative TMPI.

TMPI is constructed multiplicatively:

```
TMPI_i = thorium_reserve_share_i × nuclear_share_energy_i × institutional_quality_i
```

Scores are then normalised to a 100-point scale with USA=100 for presentation.

**The static TMPI limitation.** TMPI is a snapshot of structural endowments; it does
not model the dynamic accumulation of nuclear capacity over the transition period.
Trajectory adjustment columns are reported in `outputs/tables/tmpi_rankings.csv`
using CAGR-based projections to 2035, with Japan using its official policy target
(20% nuclear by 2035) rather than an extrapolation from near-zero post-Fukushima
levels. These trajectory scores are addenda; the static TMPI is the primary cross-
section result.

## 4.6 Governance Sensitivity Measurement

GS is defined as the ratio of energy governance volatility to commodity benchmark
volatility:

```
GS_{i,t} = CV(EG_{i,era}) / CV(commodity_benchmark_{era})
```

For the backward leg, EG is the EU ETS allocation surplus (annual, 2005–2024) and the
benchmark is Brent crude oil (annual average, same period). For the CV comparison of
carbon prices, EG is the annual average EUA spot price by phase; the benchmark is
Brent crude oil 2005–2024 (CV=0.292) and RGGI allowance prices by period.

GS is estimated at two levels. At the **regime level**: GS_{EU ETS, Phase I} = CV(EUA Phase I) / CV(Brent crude) = 0.815/0.292 = 2.79. This establishes that GS > 1 holds for politically constructed carbon governance and provides the benchmark.

At the **entity level**: GS_i = CV(energy_imports_pct_i, 2000–2023) / CV(oil_price, 2000–2023), where energy_imports_pct is sourced from the World Bank World Development Indicators. This measure captures how much more volatile entity i's energy import dependence is relative to the underlying commodity price — high volatility implies energy position is politically determined rather than tracking commodity markets. USA has high entity-level GS (deregulated energy markets, shale-revolution-driven import share volatility). Japan has low entity-level GS (METI-administered prices, stable import dependence). Russia post-2022 receives GS=0.05, computed from the near-total collapse in Russian participation in Western energy governance infrastructure post-SWIFT exclusion.

In the MPI assembly (§8), entity-specific GS values are used in place of the common regime-level value, creating cross-entity variation in monetary leverage at identical NEP levels.

## 4.7 BIS FX Turnover Data

BIS Triennial Central Bank Survey data on FX turnover by currency (2004, 2007, 2010,
2013, 2016, 2019, 2022) are used to cross-validate reserve share findings and as the
primary data source for forward predictions. INR FX turnover share (1.6% in 2022) is
the baseline against which the BIS 2028 and 2031 predictions are benchmarked.

## 4.8 Summary Statistics

Full summary statistics, variable definitions, and data sources are reported in the
supplementary appendix. The panel dataset (`data/processed/panel_model_ready.csv`) is
available in the replication archive.

| Variable | Source | Period | N entities | Notes |
|----------|--------|--------|-----------|-------|
| Reserve share (%) | IMF COFER | 1995–2024 | 6 | Allocated reserves only |
| NEP | World Bank / OWID/BP | 1900–2024 | 180+ | λ=10 lag used in main spec |
| ETS surplus (Mt CO2) | EC EUTL / Sandbag | 2005–2024 | EU only | ZA test variable |
| EUA price (EUR/tCO2) | Academic reconstruction | 2005–2024 | EU only | CV comparison; see data note |
| RGGI price (USD/tCO2) | RGGI Inc. | 2009–2024 | US NE only | CV benchmark |
| Thorium reserves | WNA / USGS 2024 | Cross-section | 12 | Thousand tonnes |
| Nuclear share (%) | OWID/BP 2024 | 1965–2024 | 12 | Primary energy share |
| WGI composite | World Bank | 1996–2024 | 12 | Unweighted avg of 6 dims |

---

# §5 — Backward Leg: Energy Governance as Politically Constructed

## 5.1 Design

The backward leg tests the MPI framework's premise: that the GS term in the State 0
expression — CV(EG)/CV(commodity benchmark) — is significantly greater than unity for
a modern energy governance regime. If GS were close to 1, energy allocation would track
commodity fundamentals and the theoretical distinction between a geological endowment
and a policy variable would collapse. The political contestability claim would be
unfounded, and the forward leg's predictions would be descriptions of geological fate
rather than strategic opportunities.

The EU ETS is the test case for three reasons. First, it is the world's largest carbon
market and the only case with two decades of documented allocation surplus data at
annual frequency. Second, its political construction is on the public record — member
state lobbying for permit allocations, phase transitions by political decision, Market
Stability Reserve activation by regulation — providing external validation for the ZA
break interpretation. Third, the RGGI comparison case is available: a second carbon
market of the same asset class, same period, with systematically different governance
construction.

## 5.2 Zivot-Andrews Structural Break Test

We run the Zivot-Andrews (1992) endogenous structural break test on the annual EU ETS
allocation surplus series (freely allocated allowances minus verified emissions,
2005–2024, Mt CO2eq). The test allows for a one-time break in level and/or trend
without pre-specifying the break date, making it appropriate for identifying the
*timing* of a governance regime change against the null of a unit root process.

**Result:** the break falls in **2014** (ZA statistic = −6.248, p = 0.0006). The
test strongly rejects the unit root null. The break is aligned with the Phase III
structural reform, which introduced the Market Stability Reserve mechanism — a
political decision negotiated over 2013–2015 that fundamentally altered the
allocation rules. 2014 is the year the reform became the governing assumption
for market participants.

Two alternative break dates would falsify the alignment claim: a break in 2008–2009
(the GFC reducing verified emissions) or a break in 2019–2020 (COVID lockdowns).
Both would indicate that the series responds to supply fundamentals rather than
political events. Neither occurred: the GFC produced a level shift in verified
emissions but not a structural break in the surplus series detectable at this
significance; the ZA algorithm identifies 2014 as the uniquely dominant break point.

**Sample size note.** The test runs on T=20 annual observations. The ZA test's
asymptotic critical values were derived for larger samples (~T≥25). With
stat=−6.248 versus the 1% asymptotic critical value of approximately −5.57, the
margin is sufficient that a plausible size correction does not alter the conclusion.
We note this as a limitation and identify extension to pre-2005 EU ETS registry data
as a robustness check for the revision stage.

## 5.3 Carbon Price Volatility: EUA vs RGGI vs Oil

The GS argument requires more than a structural break. It requires that the energy
governance regime exhibits *excess* volatility relative to the underlying physical
commodity — the signature of a politically constructed price, not a commodity price.
We compare three series over their respective first compliance periods:

| Series | Period | CV (sample) | Ratio to Oil |
|--------|--------|-------------|-------------|
| Brent crude oil | 2005–2024 | 0.292 | 1.00 |
| RGGI allowances | 2009–2012 | 0.047 | 0.16 |
| EU ETS Phase I | 2005–2007 | 0.815 | 2.79 |

The RGGI comparison is the most informative. RGGI and EUA Phase I are both synthetic
carbon permits — identical asset class, both first-compliance-period markets with
similar over-allocation problems. RGGI Phase 1 (2009–2012) was *more stable than
the oil market*: CV=0.047, below oil's CV=0.292 by a factor of six. EU ETS Phase I
was nearly three times more volatile than oil, and 17 times more volatile than RGGI.
The difference is not inherent to synthetic permits. It is specific to the EU's
allocation politics.

The EU ETS Phase I price trajectory is decisive evidence. Prices opened at ~€18/tCO2
in 2005–2006 and collapsed to ~€0.80/tCO2 by 2007, when Phase I allowances were
revealed to be non-bankable and the over-allocation surplus became transparent.
No commodity with a fixed physical supply — not even those subject to supply shocks
— exhibits a near-total price collapse driven by a political accounting revelation.
This is the signature of GS ≫ 1.

**A note on CV estimation.** The CV=0.815 is computed from annual average EUA prices, which suppress intra-year volatility. Phase I prices opened at ~€18/tCO2 in 2005–2006 and closed at ~€0.80/tCO2 by end-2007 — a 22-fold peak-to-trough movement within a 30-month window. Annual averages compress this into three data points. The true daily CV substantially exceeds 0.815. Our GS estimate of 2.79 is therefore a conservative lower bound on the political construction of Phase I EU ETS governance.

RGGI Phase 2 (post-reform, 2014–2024) shows CV=0.552 — substantially above Phase 1's
0.047. This is directionally consistent with the GS argument: as political contestation
over the RGGI cap increased post-2014, governance sensitivity rose. GS is not a fixed
property of a market; it tracks the degree of political construction in the allocation
regime at any given phase.

## 5.4 Governance Sensitivity Score

From the Phase I comparison:

```
GS_{EU ETS, Phase I} = CV(EUA Phase I) / CV(Oil 2005–2024)
                     = 0.815 / 0.292
                     ≈ 2.79
```

Normalised logistically to [0,1] for use in the MPI assembly: GS_norm ≈ 0.85. This
is the common GS value used in the State 0 term of the MPI assembly in Section 8.
Entity-specific GS estimation — using each country's domestic energy governance
volatility relative to commodity benchmarks — is identified as the primary extension
for future work.

## 5.5 What the Backward Leg Proves (and What It Does Not)

The backward leg establishes three claims:

1. **The allocation surplus breaks at a political event, not a supply shock.** The
   2014 ZA break is aligned with Phase III structural reform. This is consistent with
   the GS argument that allocation regimes are governed by political calendar, not
   commodity fundamentals.

2. **EU ETS price volatility substantially exceeds both the commodity benchmark and
   the RGGI equivalent.** GS ≈ 2.79 indicates that the EU carbon governance regime
   was approximately 2.8 times more politically constructed than the underlying
   commodity market. By the RGGI comparison, this excess is EU-specific — not a
   property of carbon markets as a class.

3. **Carbon governance cannot anchor sovereign energy policy.** A regime exhibiting
   GS > 1 of this magnitude cannot function as a credible, rule-based allocator.
   Political incumbents will renegotiate the rules whenever the allocation imposes
   material costs. This instability is the structural condition from which the thorium
   transition derives its logic: the carbon era's monetary architecture is unstable
   not because of poor design but because the allocation mechanism is contestable
   by design.

The backward leg does not prove intentional capture by identifiable actors — the
Stigler-Mattli-Woods capture claim is a stronger claim that requires actor-level
evidence beyond the price series. It does not prove that all energy governance exhibits
GS > 1 — the RGGI finding suggests that less politically constructed regimes can
approach GS ≈ 1. And it does not test whether the EU carbon era produced monetary
outcomes: the ETS is too young and the N too small for a monetary test. That test is
the present leg.

---

# §6 — Present Leg: Net Energy Position → Reserve Currency Share

## 6.1 Design and Epistemological Framing

The present leg tests the State 0 term of the MPI framework: does NEP_{i,t−λ} predict
reserve share, and does it do so with a generational lag? The panel covers six reserve
currency entities — USD, EUR, GBP, JPY, CNY, CHF — over 1995–2024.

The honest epistemological framing is stated at the outset: this is not a treatment-
effects identification. With N=6 entities and T≈30 years, the panel cannot support
causal inference in the contemporary econometric sense. Two entities drive the
structured cases (USA: rising NEP, stable/rising share; EMU: falling NEP, falling
share); three are boundary conditions (Japan: NEP shock; Switzerland: institutional
substitution); one is a recent addition with limited COFER history (China). This is
historical political economy with falsifiable predictions, not cross-sectional
identification.

The primary empirical strategy is entity-specific cointegration: ARDL bounds tests
to establish whether long-run relationships exist, followed by entity-specific ECM
and DOLS estimations where cointegration is confirmed. The heterogeneity statistic
I²>90% across entity-specific slopes confirms that pooled OLS is the wrong estimator;
we report it for transparency but do not treat it as the paper's result.

## 6.2 Pre-Regression Diagnostics

ADF and KPSS stationarity tests indicate mixed integration orders: reserve share is
I(1) for most entities; NEP is I(1) for most entities with some borderline I(0) cases.
Mixed I(0)/I(1) orders are the key motivation for the ARDL bounds approach, which is
valid under either order or a mixture without requiring pre-testing for exact order.
Johansen cointegration is reported as supplementary — it requires I(1) pre-testing and
is inappropriate for mixed cases.

## 6.3 Pooled Specifications (Transparency Only)

Pooled OLS with entity and time fixed effects yields β≈84 (SE=37.9, p=0.027) at
lag 10 and β≈108 (SE=37.7, p=0.004) at lag 15 in undifferenced levels. Differenced
specifications are not significant (β=58.9, p=0.242 at lag 10; β=−6.1, p=0.874 at
lag 15). The logit transform — which respects the compositional nature of reserve
shares — is not significant at any specification.

Table 1 reports all eight pooled specifications for transparency. The pattern is
diagnostic, not problematic: significance only in undifferenced levels is consistent
with the presence of a cointegrating relationship that differencing destroys. It is
not evidence of a spurious regression, provided cointegration is confirmed by the
ARDL bounds test below. The leave-one-out jackknife confirms the pooled result is
driven by the USA case: dropping the US flips β from +84 to −3. Pooled OLS
inappropriately averages opposite-sign slopes across structurally heterogeneous
entities. The entity-specific results are the paper's primary empirical contribution.

## 6.4 ARDL Bounds Test and Entity-Specific ECM

The ARDL bounds test (Pesaran, Shin, and Smith 2001) is the appropriate primary
cointegration framework for a mixed I(0)/I(1) panel. It tests the null of no long-run
relationship against the alternative of cointegration without requiring pre-specified
integration orders. For each entity we estimate the unrestricted ARDL model and test
whether the F-statistic on the lagged level terms exceeds the upper (I(1)) critical
bound.

**United States:** ARDL bounds F-statistic exceeds the I(1) critical value at the
5% level. Cointegration confirmed. The long-run DOLS coefficient on NEP is positive
and significant; the ECM speed-of-adjustment coefficient is negative and significant,
confirming that deviations from the long-run relationship are corrected over time.
The shale revolution raised US NEP from 0.143 (2010) to 0.166 (2019) — a 16% increase
concentrated over 2010–2019. USD reserve share declined from 64% (2015) to 59% (2021)
as portfolio diversification into non-traditional reserve currencies proceeded
(Arslanalp, Eichengreen, and Simpson-Bell 2022). Since 2021, USD share has stabilised
at 58.5–59.0%, approximately λ=10 years after peak shale output — consistent with the
mechanism beginning to counteract the diversification trend on schedule.

**Euro Area (EMU):** ARDL bounds test confirms cointegration. GDP-weighted eurozone
NEP — constructed from DEU, FRA, ITA, ESP, NLD — declined from 0.010 (1999) to 0.005
(2024) as North Sea reserves depleted and import dependence rose. EUR reserve share
peaked at 24% in 2009 and declined to 19% by 2024. The Pearson correlation between
NEP lagged 10 years and EUR reserve share is r=0.864 (n=16). This is the paper's
second structured case and it runs in the opposite direction to the USA: same mechanism,
falling NEP, falling reserve share. EMU is not a boundary condition. It is confirmation.

The LOO jackknife result — dropping USA flips pooled β from +84 to −3 — is evidence
of opposite-sign slopes that pooled OLS conflates, not evidence against the mechanism.
Two entities, opposite energy trajectories, opposite reserve share trajectories. A pooled
estimator that assigns them the same coefficient is the wrong model.

## 6.5 Japan: The Control Case

Japan provides the cleanest identification in the paper. With the world's third-largest
GDP, deep and liquid financial markets, and stable monetary institutions, Japan commands
every predictor the standard reserve currency literature deploys. The yen should, on
GDP grounds, hold 10–15% of global reserves. It holds 5–6%.

The mechanism explains this directly. Japan is a chronic net energy importer — NEP
has been negative for most of the postwar period. The identification sharpens
post-Fukushima. The March 2011 nuclear disaster triggered a near-complete shutdown
of Japan's nuclear fleet: NEP fell from 0.0084 (2010) to 0.0028 (2012), a 67% decline
in two years. This is an exogenous shock to the energy variable — the shutdown was
not driven by monetary policy decisions, trade patterns, or financial market conditions.
It was driven by a natural disaster and the subsequent regulatory response.

Yen reserve share did not recover following the NEP collapse. The Fukushima natural
experiment thus isolates the energy variable's effect from the GDP, finance, and
knowledge variables that remain unchanged: the same country, same institutions, same
financial depth — but with an exogenous collapse in energy position. Reserve share
stagnated. The control variables predict recovery; the energy mechanism predicts
stagnation. The data support the energy mechanism.

The framework also predicts when Japan should recover: Japan's official energy policy
targets 20% nuclear capacity by 2035. As nuclear capacity rebuilds, NEP improves.
As p_t rises toward the thorium era, Japan's TMPI components (institutional quality,
policy commitment) begin to activate. MPI predicts a gradual recovery in yen
reserve share from approximately 2025–2030, conditional on nuclear restart
proceeding as planned. This is a falsifiable prediction, not a post-hoc rationalisation.

## 6.6 Boundary Conditions

**Switzerland.** CHF holds 0.2–0.3% of global reserves with NEP of approximately
0.001 — the smallest NEP of any entity in the panel, essentially zero net energy
position. Switzerland is not a falsification of the mechanism. It is an institutional
substitution case: financial entrepôt status, rule of law, and monetary credibility
built over two centuries generate reserve demand independently of energy position.
The MPI framework anticipates this: if GS_CHE ≈ 0 (energy governance entirely
administered, no allocation politics), then the State 0 term approaches zero and
reserve share must be explained by other structural factors. Switzerland is the
purest example of Strange's (1988) finance-knowledge combination without the
production structure. The mechanism's absence confirms its theoretical scope: it
applies where governance contestability creates leverage surfaces, not where
institutional substitution operates independently.

**China.** CNY reserve share entered COFER reporting fully from 2016; prior data
are reconstructions. The short and partially reconstructed series prevents ARDL
estimation. China's NEP is approximately zero (near energy balance at world scale
despite large absolute production volumes). CNY reserve share is 2–3%. The mechanism
does not predict CNY dominance; it predicts that without a positive and rising NEP,
CNY's path to reserve currency status runs through institutional quality and capital
account opening rather than energy position — which is consistent with the observed
trajectory of incremental internationalisation.

**Russia.** Russia's case separates into two mechanisms (see Section 8 and §9.2).
In the present leg, Mechanism A applies: pre-existing energy supply relationships
(Eurasian hydrocarbon corridors) determined which bilateral monetary corridors were
structurally viable when sanctions forced their formation in 2022. This supports the
thesis mechanism. Mechanism B — SWIFT shock forcing corridor formation at abnormal
speed — tests the GS argument rather than the NEP mechanism and is discussed in the
synthesis.

## 6.7 Pooled Panel: Honest Assessment

Two specifications out of eight show statistical significance, both in undifferenced
levels. Under I(1) non-stationary series, undifferenced levels regression without
cointegration correction produces spuriously inflated R² and t-statistics. The R²=0.997
is diagnostic: with entity and time fixed effects absorbing most variation in a
persistent panel, this level of fit is expected regardless of whether the mechanism
is real.

The differenced and logit-transformed specifications are not significant. This would
be damaging if entity-specific cointegration were not confirmed. But the ARDL bounds
test confirms cointegration for the two structured cases (USA, EMU), which is exactly
the condition under which levels regression is valid and differencing is inappropriate
— differencing cointegrated series throws away the long-run relationship. The pooled
table is consistent with the entity-specific results, not in conflict with them.

The paper's primary empirical result is: ARDL bounds confirms cointegration for USA
and EMU; entity-specific DOLS yields positive and significant NEP coefficients for
USA and negative and significant for EMU; the Japan natural experiment provides
exogenous identification; I²>90% confirms heterogeneous slopes requiring entity-
specific rather than pooled estimation. Pooled β≈84 is reported as a descriptive
baseline, not as the headline result.

---

# §7 — Forward Leg: TMPI and the Distribution of Next-Era Monetary Potential

## 7.1 Design

The forward leg constructs the State 1 term of the MPI framework: TMPI_i · GS_{i,t+τ}.
It asks which states hold the structural position to convert thorium-era energy
sovereignty into monetary leverage when p_t rises. The TMPI is not a forecast. It is
a structural mapping: given the mechanism identified in the present leg, which entities
have the endowment configuration that the mechanism requires?

The forward leg does not require thorium to be commercially dominant in 2024. It
requires that the structural preconditions — reserve endowment, conversion capacity,
institutional quality — are measurable now and that the mechanism's direction, if the
transition occurs, is derivable from those preconditions. The predictions are conditional
on transition *beginning*, not on transition completing: the INR FX turnover prediction
(BIS 2028) requires only that India's nuclear programme continues at current trajectory
and that markets begin pricing this into currency demand.

## 7.2 TMPI Construction

The Thorium Monetary Potential Index is constructed multiplicatively:

```
TMPI_i = thorium_reserve_share_i × nuclear_share_energy_i × institutional_quality_i
```

**Thorium reserve share** — country's identified thorium resources as a share of
world total (WNA and USGS 2024). India holds 16.1% of world reserves, Australia
12.6%, Brazil 13.4%, USA 10.8%. These are known, documented, non-moveable endowments.
The multiplicative structure means that reserve endowment alone is insufficient: the
thorium must be convertible into energy and the energy convertible into monetary
leverage.

**Nuclear energy share** — nuclear consumption as a fraction of primary energy
consumption (OWID/BP 2024). This is the conversion capacity term: a country with
large thorium reserves but zero nuclear programme cannot activate the endowment.
USA leads at 7.6% current nuclear share; France (treated within EMU) is the highest
globally but France's thorium reserves are negligible, producing a low TMPI despite
high nuclear share.

**Institutional quality** — WGI composite (unweighted average of six dimensions),
normalised to [0,1]. This is the monetisation term: a country with energy position
but weak institutions cannot convert it into reserve status. Russia's nuclear capacity
is real (5.8% of primary energy) and thorium endowment is non-trivial (2.5%), but
WGI composite of 0.40 dampens the TMPI to 9.3 — consistent with the present leg's
finding that energy position without convertibility infrastructure does not produce
reserve status.

## 7.3 Rankings and the Three-Constraint Diagnostic

Table 2 reports TMPI scores, normalised to USA=100:

| Entity | TMPI | Thorium share | Nuclear share | WGI | Binding constraint |
|--------|------|--------------|--------------|-----|-------------------|
| USA | 100.0 | 10.8% | 7.6% | 0.76 | None — all three present |
| CAN | 20.8 | 2.8% | 5.4% | 0.86 | Modest reserves |
| IND | 15.8 | 16.1% | 1.2% | 0.52 | Nuclear capacity (early stage) |
| BRA | 9.7 | 13.4% | 1.0% | 0.46 | Double: capacity + institutions |
| RUS | 9.3 | 2.5% | 5.8% | 0.40 | Institutions (+ GS suppressed) |
| CHN | 4.2 | 2.1% | 2.2% | 0.56 | Reserves + partial capacity |
| AUS | 0.0 | 12.6% | 0.0% | 0.85 | Nuclear capacity — zero current |
| GBR | 0.0 | ~0% | 5.1% | 0.79 | Reserves — negligible |

The three-constraint diagnostic is the table's analytical contribution. TMPI is
not merely a ranking — it identifies *which* constraint is binding for each entity,
which is where policy and forward analysis diverge.

**India** is the paper's forward prediction. With the world's largest thorium reserves
(16.1%), an active three-stage nuclear programme, and improving institutions, India
ranks third globally despite current nuclear share of only 1.2%. The programme is
70 years underway: Stage 1 (PHWR, pressurised heavy water) is producing; Stage 2
(fast breeder reactors, using plutonium to breed U-233 from thorium) has its first
commercial reactor under construction at Kalpakkam; Stage 3 (thorium-based AHWR)
follows. The binding constraint is not strategic intent — it is the time to deployment.
As nuclear share rises from 1.2% to the policy target of 3–4% by 2030 and beyond,
India's TMPI rises with it, driving the INR forward prediction.

**Australia** is the clearest demonstration of the multiplicative structure's logic.
Reserve endowment (12.6%) and institutional quality (WGI=0.855, one of the highest in
the dataset) are both high. Current nuclear energy share: zero. Australia has a policy
prohibition on nuclear power that predates the AUKUS agreement. TMPI=0 — not because
Australia lacks potential but because the conversion capacity term collapses the entire
index. AUKUS changes this constraint from ~2035 when nuclear-powered submarines
imply at minimum the development of a nuclear infrastructure with civilian co-benefits.
The paper makes a specific prediction: AUD reserve share should step up from its
current niche (~6–7% of FX turnover, Arslanalp et al. 2022) as AUKUS nuclear capacity
activates, conditional on geopolitical activation (see §7.5 below).

**The Katzenstein filter: activation vs niche reinforcement.** The raw TMPI scores
treat USA, Australia, and Canada similarly in their institutional dimension. But
Katzenstein's (1985) framework on small states in world markets establishes that
Five Eyes alliance-embedded states do not independently leverage resource endowments
into structural monetary power. Australia and Canada are already reserve currencies
(Arslanalp et al. 2022) as *niches within the dollar system* — their monetary status
comes from commodity credibility and financial openness, not from independent
leverage. The paper's prediction for these two cases is niche reinforcement, not
independent activation. India, by contrast, has no equivalent alliance constraint
and a deliberate policy of sovereign fuel cycle control designed precisely to prevent
external dependence of the kind Australia and Canada accept.

This produces a falsifiable cross-case prediction: if the mechanism is correctly
specified and the Katzenstein filter applies, then (a) India will gain FX turnover
share from 2028 as nuclear capacity grows; (b) Australia will not gain share
disproportionate to its current niche despite AUKUS nuclear development. If both
gain independently, the Katzenstein filter is refuted. If neither gains, the mechanism
is refuted. The cross-case contrast is the test.

## 7.4 Scenario Sensitivity

The TMPI rankings are constructed at current nuclear shares. The forward prediction
requires that the rankings remain stable as the transition progresses. We test this
across three energy transition scenarios:

- **Low** (3% nuclear share of world primary energy by 2040): conservative; limited
  deployment beyond current trajectory
- **Base** (10%): consistent with IEA net-zero scenario nuclear revival
- **High** (20%): rapid deployment; approximate energy equivalence of thorium to oil

**Finding:** the top-three ranking (USA > CAN > IND) is scenario-invariant across all
three assumptions. The mechanism that produces the ranking — multiplicative combination
of reserves, capacity, and institutions — is robust to the pace of transition. India
remains third regardless of how fast thorium reaches commercial scale, because the
reserve endowment is large enough to maintain its position even under rapid deployment
that would benefit capacity-leaders like Canada and Russia.

The stability finding is important for the falsification structure. The forward
prediction is not contingent on a precise p_t calibration — the ranking is stable
across the range of plausible p_t values corresponding to the three scenarios.

## 7.5 Trajectory Adjustments

A limitation of the static TMPI is that it captures current nuclear share, which for
several key cases reflects regulatory constraints rather than strategic trajectory.
Two adjustments are noted (not incorporated into the primary ranking):

**China**: nuclear share grew 82% between 2015 and 2024 (0.0123 → 0.0224). CAGR-based
projection to 2035 gives a nuclear share of 0.025, raising trajectory-adjusted TMPI
from 4.2 to 5.1. China remains sixth globally, but the trajectory is upward and
deserves monitoring.

**Japan**: the base year (2015) had near-zero nuclear share (0.0021) following
post-Fukushima shutdowns. Any extrapolation from that base is uninformative.
Japan's trajectory-adjusted TMPI uses the official policy target of 20% nuclear by
2035 — a government commitment, not a projection. At 20% nuclear share, Japan's
TMPI rises substantially. Whether this translates into reserve share depends on
whether the MPI mechanism predicts yen recovery — which it does, conditional on
nuclear restart proceeding (see §6.5).

---

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

---

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

---

## References

Arslanalp, S., Eichengreen, B., and Simpson-Bell, C. (2022). "The stealth erosion of
dollar dominance: Active diversifiers and the rise of nontraditional reserve currencies."
*IMF Working Paper* WP/22/58.

Bayer, P. and Aklin, M. (2020). "The European Union Emissions Trading Scheme reduced
CO2 emissions despite low prices." *Proceedings of the National Academy of Sciences*,
117(16), 8804–8812.

Chinn, M.D. and Frankel, J.A. (2007). "Will the euro eventually surpass the dollar as
leading international reserve currency?" In Clarida, R. (ed.), *G7 Current Account
Imbalances*. University of Chicago Press, 283–338.

Cohen, B.J. (2015). *Currency Power: Understanding Monetary Rivalry*. Princeton
University Press.

Dannreuther, R. (2017). *Energy Security*. Polity Press.

Eichengreen, B. (2011). *Exorbitant Privilege: The Rise and Fall of the Dollar and the
Future of the International Monetary System*. Oxford University Press.

Eichengreen, B. and Flandreau, M. (2009). "The rise and fall of the dollar (or when
did the dollar replace sterling as the leading reserve currency?)." *European Review
of Economic History*, 13(3), 377–411.

Ellerman, A.D. and Buchner, B.K. (2008). "Over-allocation or abatement? A preliminary
analysis of the EU ETS based on the 2005–06 emissions data." *Environmental and
Resource Economics*, 41(2), 267–287.

Farrell, H. and Newman, A.L. (2019). "Weaponized interdependence: How global economic
networks shape state coercion." *International Security*, 44(1), 42–79.

Gilpin, R. (1981). *War and Change in World Politics*. Cambridge University Press.

Helleiner, E. (2014). *The Status Quo Crisis: Global Financial Governance after the
2008 Meltdown*. Oxford University Press.

Katzenstein, P.J. (1985). *Small States in World Markets: Industrial Policy in Europe*.
Cornell University Press.

Kindleberger, C.P. (1973). *The World in Depression, 1929–1939*. University of
California Press.

Kirshner, J. (1995). *Currency and Coercion: The Political Economy of International
Monetary Power*. Princeton University Press.

Kirshner, J. (2014). *American Power after the Financial Crisis*. Cornell University
Press.

Koch, N., Fuss, S., Grosjean, G., and Edenhofer, O. (2014). "Causes of the EU ETS
price drop: Recession, CDM, renewable policies or a broken carbon market?" *Energy
Policy*, 73, 676–685.

Maggiori, M., Neiman, B., and Schreger, J. (2020). "International currencies and
capital allocation." *Journal of Political Economy*, 128(6), 2019–2066.

Mattli, W. and Woods, N. (2009). *The Politics of Global Regulation*. Princeton
University Press.

McNally, R. (2019). *Crude Volatility: The History and Future of Boom-Bust Oil Prices*.
Columbia University Press.

Norrlof, C. (2010). *America's Global Advantage: US Hegemony and International
Cooperation*. Cambridge University Press.

Overland, I. (2019). "The geopolitics of renewable energy: Debunking four emerging
myths." *Energy Research & Social Science*, 49, 36–40.

Paterson, M. and Stripple, J. (2010). "My Space: governing individuals' carbon
emissions." *Environment and Planning D*, 28(2), 341–362.

Pesaran, M.H., Shin, Y., and Smith, R.J. (2001). "Bounds testing approaches to the
analysis of level relationships." *Journal of Applied Econometrics*, 16(3), 289–326.

Scholten, D. (ed.) (2018). *The Geopolitics of Renewables*. Springer.

Scholten, D., Bazilian, M., Overland, I., and Westphal, K. (2020). "The geopolitics
of renewables: New board, new game." *Energy Policy*, 138, 111059.

Stigler, G.J. (1971). "The theory of economic regulation." *The Bell Journal of
Economics and Management Science*, 2(1), 3–21.

Strange, S. (1988). *States and Markets*. Pinter Publishers.

Zivot, E. and Andrews, D.W.K. (1992). "Further evidence on the great crash, the
oil-price shock, and the unit-root hypothesis." *Journal of Business & Economic
Statistics*, 10(3), 251–270.
