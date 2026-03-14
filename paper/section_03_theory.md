# §3 — A Formal Theory of Monetary Power Across Energy Eras

## 3.1 The Gap in Existing Frameworks

Three bodies of literature approach the relationship between energy and monetary power but none
formalises it across time.

Strange (1988) identified finance and energy as two of the four structures of structural power
and argued that states capable of controlling both acquire disproportionate capacity to shape
international outcomes. She did not formalise the interaction or specify how it changes as the
dominant energy input shifts. Her framework is synchronic: it describes structural power at a
point in time.

Eichengreen (2011) estimates the determinants of reserve currency share with panel regressions
that include trade share, financial depth, and institutional quality. Energy position does not
appear. The specifications are linear and present-only: they capture the existing distribution
of monetary power but cannot map its evolution across energy transitions.

Stigler's (1971) regulatory capture theory — the most natural framework for describing
politically constructed allocation regimes like the EU ETS — is static, single-sector, and
carries no monetary dimension. Applying the capture label to carbon markets (as several
political economy scholars have done) explains allocation outcomes but says nothing about
what follows for monetary power.

The gap all three share: none formalises the *temporal* interaction between energy governance
contestability, current energy position, and forward energy positioning across transitions.
This paper proposes a framework that does.

---

## 3.2 The Monetary Power Index

We define the **Monetary Power Index** (MPI) for entity *i* at time *t* as:

```
MPI_{i,t} = [α(era) · NEP_{i,t−λ}] × [β(era) · GS_{i,t}] × [γ(era) · TI_{i,t+τ}]
```

where:

| Symbol | Name | Definition | Empirical counterpart |
|--------|------|------------|----------------------|
| NEP_{i,t−λ} | Net Energy Position (lagged) | Production share minus net import share in world primary energy; lagged λ years | World Bank energy balance data; λ=10 estimated from USA case |
| GS_{i,t} | Governance Sensitivity | Ratio of energy governance volatility to comparable commodity benchmark: CV(EG_{i,t}) / CV(commodity_t) | Phase CV comparison (EU ETS §5); Zivot-Andrews statistic as ordinal complement |
| TI_{i,t+τ} | Transition Index | Forward energy positioning under the next dominant energy input; projected τ years ahead | TMPI (§7): thorium_reserve_share × nuclear_capacity_share × institutional_quality |
| α(era), β(era), γ(era) | Era weights | Shift across energy transitions; sum to 1 within each era | Theoretically calibrated — see Table 1 |

**Multiplicative structure.** The three terms are multiplied, not summed. This reflects a
*necessary conditions* logic: a country that excels on energy position but whose governance
regime is fully insulated from political contestation (GS→0) — i.e., one whose energy
allocation is determined by geological endowment rather than political negotiation — has no
leverage surface. Conversely, a country with high governance sensitivity but negligible
energy position (NEP→0) has nothing to contest. All three components must be non-zero for
monetary leverage to compound.

This structure already operates in the TMPI: Australia currently has thorium reserves (12.6%
world share) and strong institutions but zero nuclear capacity, which collapses its current
TMPI to zero. The same logic applies to MPI at the general level.

**The three time registers in one expression.** MPI at time *t* is a function of energy
position established *λ* years in the past (NEP_{t−λ}), governance contestability *now*
(GS_t), and forward transition positioning *τ* years ahead (TI_{t+τ}). This is the temporal
sandwich the paper's three empirical legs each estimate separately:

```
BACKWARD leg (§5) → estimates GS_{i,t}  via ZA break + CV comparison
PRESENT leg  (§6) → estimates NEP_{i,t−λ} → reserve share (λ, β coefficients)
FORWARD leg  (§7) → constructs TI_{i,t+τ} = TMPI
```

We do not estimate MPI as a single reduced-form regression. We estimate each component
separately with appropriate methods for its temporal register, then synthesise in §8.

---

## 3.3 Era Weights

The era weights α(era), β(era), γ(era) formalise the paper's central claim: that the
mechanism is not oil-specific. In each energy era, one component dominates:

**Table 1: Era weight calibration**

| Era | Dominant energy input | α (NEP weight) | β (GS weight) | γ (TI weight) | Historical anchor |
|-----|----------------------|---------------|--------------|--------------|-------------------|
| Coal/steam (1850–1920) | Coal | High | Low | — | British coal = British naval + monetary power |
| Oil (1945–2000) | Oil | High | Medium | Low | Petrodollar recycling; oil shocks |
| Carbon/transition (2000–2040) | Mixed + carbon governance | Medium | **High** | Rising | EU ETS political construction; this paper's backward test |
| Thorium/next (2040–) | Nuclear fission | Low → medium | Low | **High** | TMPI forward projections |

The era weights are *not* estimated — they are calibrated from historical cases and treated
as theoretical prior. A future paper could estimate them structurally if sufficient cross-era
panel data were available (it currently is not). Within this paper, the weights justify the
architecture: the backward leg (β high in the carbon era) and the forward leg (γ rising) are
the novel contributions; the present leg (α) extends an existing literature.

---

## 3.4 The Governance Sensitivity Term

The central innovation is the GS term. Existing frameworks treat energy position as
exogenous endowment — a geological given. GS_{i,t} operationalises the claim that this is
wrong: energy governance regimes are politically constructed, and their volatility relative
to the underlying commodity reveals the degree of political contestation.

**Formal definition:**
```
GS_{i,t} = CV(EG_{i,era}) / CV(commodity_benchmark_{era})
```

where EG is the energy governance indicator (allocation surplus for carbon markets; domestic
price regime for oil markets) and the commodity benchmark is the underlying physical commodity
traded at world prices.

**Interpretation.** If GS = 1, the governance regime is no more volatile than the physical
commodity — endowment-like. If GS > 1, the regime exhibits excess volatility attributable
to political intervention. Phase I EU ETS: GS = 0.82/0.29 ≈ 2.8. The allocation surplus
was nearly three times more volatile than the oil price in the same period. This is not a
commodity with fixed physical supply. It is a politically constructed allocation regime.

**Complement: the Zivot-Andrews statistic.** CV captures the degree of political construction
over a phase; the ZA statistic captures whether that construction breaks endogenously at a
political event. Both are reported in §5. They are complementary measures of the same
underlying property: governance sensitivity.

**Cross-country extension.** For the present leg, GS does not vary across the six reserve
currency entities because they are all subject to the same international oil market (the
commodity benchmark is common). GS enters the MPI expression as a framework variable; in
the present-leg regressions it is held constant and the variation comes from NEP. Future work
could construct entity-specific GS measures using domestic energy price regulation data.

---

## 3.5 What the Framework Explains That Prior Work Cannot

**The USA-EMU contrast.** The USA is a net energy producer (NEP rising through the shale
revolution); the eurozone is a net energy importer (NEP declining post-2014). Under the same
β and GS terms, the MPI predicts opposite trajectories — USD strengthening relative to EUR
in reserve share. This is exactly what the data show (§6). A framework that omits NEP cannot
produce this prediction from first principles.

**The Japan test.** Japan has the world's third-largest economy (GDP share ~6%) but persistent
underperformance in reserve share (~5–6%). Under a GDP-only framework (Eichengreen), Japan
is anomalous. Under MPI, it is predicted: Japan's NEP collapsed 61% after Fukushima (2011),
and its reserve share has been stagnant since. Exogenous shock to NEP → mechanism suppressed.

**The Russia hinge.** Russia's 2022 expulsion from Western financial infrastructure illustrates
all three components simultaneously: its governance regime (GS) was exposed as political
infrastructure; its energy corridors (NEP operating under duress) shifted to bilateral
ruble-yuan and ruble-rupee; and its forward transition positioning (TI) is intact (nuclear
capacity, thorium potential) but geopolitically isolated. MPI captures why Russia has
potential but cannot activate it — the GS term under sanction regime approaches zero.

**The Australia case.** Australia has thorium reserves (TI component high in the next era)
and open capital account (institutions component of TI high), but zero nuclear capacity
(which collapses TI multiplicatively to zero). AUKUS changes the nuclear capacity constraint
~2035. MPI predicts: AUD reserve currency status maintained by other components now;
potential step-change after AUKUS nuclear capacity activates. This is the paper's most
falsifiable forward prediction.

---

## 3.6 Relationship to Strange's Structural Power

Strange argued that structural power — the power to shape the framework within which
others must operate — derives from four sources: security, production, finance, and
knowledge. She identified finance and energy (a subset of production) as jointly constitutive:
states that control both acquire disproportionate structural leverage.

MPI formalises the finance-energy interaction she described. NEP is the energy component.
Reserve share (the outcome MPI predicts) is the financial component. GS is the political
contestability of the interface between them — the degree to which energy allocation is a
strategic variable rather than a geological constant. TI extends the framework to future
transitions Strange could not have anticipated.

The key departure from Strange: she assumed structural power is reproduced in the present.
MPI shows it is reproduced across eras, and that the reproduction mechanism — energy
governance contestability feeding into monetary position — is estimable. Countries that
understand the GS term can strategically construct governance sensitivity in the next era.
That is what the EU ETS Phase III reforms did for European carbon governance, and what
India's three-stage nuclear programme is doing for the thorium era.

---

*Empirical implementation: §5 (backward, GS), §6 (present, NEP), §7 (forward, TI), §8 (synthesis).*
