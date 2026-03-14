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

For this paper, p_t is estimated independently from the 5-year rolling mean CAGR of world nuclear energy consumption (OWID/BP data). World nuclear *share* has been declining since 2000 (post-Fukushima, German phase-out), making it an uninformative base for a transition signal; absolute nuclear *consumption* has been growing, driven by China and India additions. The 5-year rolling mean CAGR smooths regulatory shocks — German reactor closures (2022) and French maintenance outages (2022–23) — that are transient, not structural. Reference rate is 15% annual CAGR, calibrated so that 2024's observed rate (~1.7%) maps to p_t ≈ 0.11 — consistent with the Low scenario (p_t ≈ 0.10). This construction is independent of scenario endpoint assumptions: it derives from the observed trajectory, not from a target level imposed from outside the data. The Low/Base/High scenario bounds then provide sensitivity analysis around the central trajectory.

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
post-Fukushima: NEP dropped 67% in two years). TMPI is a structural endowment: geological
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

GS appears in both states of the MPI expression. This is not redundant — it is the
paper's central theoretical claim made explicit: **governance contestability is the
mechanism that makes energy sovereignty a policy variable in any era.**

GS operates at two distinct levels in this paper, and it is essential to keep them
separate.

**GS_regime — regime-level calibration (backward leg).** Measures how politically
constructed a specific allocation mechanism is, relative to the underlying commodity:

```
GS_regime = CV(allocation_governance_indicator_{era}) / CV(commodity_benchmark_{era})
```

The EU ETS Phase I provides the cleanest measurement: GS_regime = CV(EUA Phase I) /
CV(oil) = 0.815 / 0.292 ≈ 2.79. The Phase I allocation surplus was nearly three times
more volatile than the oil price in the same period — the signature of a politically
negotiated regime, not a commodity with fixed physical supply. The backward leg
establishes GS_regime > 1 as a structural property of the EU carbon regime; it does not
require, and does not claim, that all energy governance exhibits this property — the RGGI
comparison (GS_regime ≈ 0.16) demonstrates that the same asset class can be governed
with far lower political sensitivity. GS_regime is normalised to GS_norm ≈ 0.85 for use
as a scaling anchor in the MPI assembly (§5.4).

**GS_{i,t} — entity-level governance sensitivity (MPI assembly input).** Measures how
volatile each entity's energy import position has been relative to the commodity
benchmark — a proxy for how exposed the entity's energy balance is to politically
constructed allocation regimes, rather than stable administered governance:

```
GS_{i,t} = CV(energy_imports_pct_i, 2000–2023) / CV(oil_price, 2000–2023)
```

High GS_{i,t} indicates an energy position that moves substantially more than the
underlying commodity price — the hallmark of politically contested allocation. Low
GS_{i,t} indicates administered stability. Russia post-2022 is computed from post-sanction
years only (2022–23), reflecting exclusion from Western governance infrastructure.
Table 3 reports computed values:

| Entity | GS_{i,t} (raw) | GS_{i,t} (norm) | Interpretation |
|--------|----------------|-----------------|----------------|
| RUS | 0.011 | 0.004 | Post-2022 sanctions: near-zero Western governance participation |
| EMU | 0.076 | 0.024 | Slowly declining imports, administered elements |
| CHE | 0.127 | 0.040 | Financial entrepôt, stable administration |
| JPN | 0.139 | 0.043 | METI-administered prices, stable import dependence ✓ |
| IND | 0.465 | 0.144 | Volatile import dependence (oil price sensitivity) |
| CAN | 0.502 | 0.156 | Commodity-exposed, moderate governance |
| AUS | 0.626 | 0.195 | LNG/coal exporter, market-priced |
| CHN | 1.348 | 0.419 | Rapid energy structure change |
| GBR | 1.827 | 0.568 | North Sea depletion, liberalised market |
| USA | 1.984 | 0.616 | Shale revolution, deregulated ✓ |
| BRA | 3.219 | 1.000 | Hydroelectric + oil import volatility |

The ordering confirms the theoretical priors: Japan and Switzerland (administered) are
among the lowest non-sanctioned entities; USA and GBR (deregulated, structurally
volatile) are among the highest. This entity-level variation differentiates entities at
the same NEP level within the MPI assembly.

**The relationship between GS_regime and GS_{i,t}.** Both measure governance volatility
normalised to a commodity benchmark; they differ in scope. GS_regime characterises a
specific allocation mechanism (the EU carbon market, the oil-dollar settlement system).
GS_{i,t} characterises a country's exposure to however governance operates in its era.
GS_regime > 1 established by the backward leg is the theoretical warrant for using
GS_{i,t} in the MPI: it proves that governance construction is real and measurable, not
a classification artefact.

**Complement: the Zivot-Andrews statistic.** CV captures the degree of political
construction over a phase; the ZA statistic captures whether that construction breaks
endogenously at a political event rather than a supply shock. Both are reported in §5.
They are complementary measures of the same underlying property.

In State 1, GS captures whether the thorium allocation regime will be politically
constructed or treated as geologically fixed. The countries investing now in domestic fuel
cycle control — India's closed-cycle programme, Canada's CANDU heavy-water expertise —
are pre-positioning for high GS in the thorium era. Countries that allow their thorium
endowment to be allocated by international markets cede the GS term and with it the
amplification it provides on TMPI.

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
