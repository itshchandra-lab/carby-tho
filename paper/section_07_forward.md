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
|--------|------|--------------|--------------|-----|--------------------|
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
