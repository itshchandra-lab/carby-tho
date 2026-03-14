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
