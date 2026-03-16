# Framework Extensions: Battery Transition and AI Compute
## Analytical Addendum to "The Carbon-Thorium Standard"

**Document type:** Author working notes — analytical extensions for revision
**Audience:** IPE scholars, monetary economists, central bank researchers
**Date:** March 2026
**Purpose:** Two developments — the battery-led energy transition and AI compute demand — have direct implications for the paper's core variables (p_t, NEP, Katzenstein filter). This document specifies those implications in the paper's own framework language.

---

## 1. The Battery Transition as a p_t Scenario, Not an Industry Story

### The Precise Question for This Paper

The paper's forward register rests on p_t rising — the probability weight shifting from the carbon-era NEP term to the thorium-era TMPI term. The battery transition raises one specific question for the framework:

**Under what conditions does solar-wind-battery dominance make p_t irrelevant — not just slow, but permanently near-zero?**

This is not an EV story. It is a scenario analysis question about the paper's transition function. The paper currently treats p_t as rising toward 1 as thorium fuel cycle technology matures. The battery scenario is the null hypothesis: p_t stays near zero because variable renewables with grid-scale storage displace the need for dispatchable nuclear before thorium reaches commercial scale.

### Why This Matters for the MPI Framework

If p_t → 0, the MPI collapses to:

MPI_{i,t} = NEP_{i,t−λ} · GS_{i,t}

This is the carbon-era formula only. TMPI becomes irrelevant. India's 15.8 score becomes zero contribution. China's 4.2 becomes zero contribution. The forward register predictions — India's monetary rise, China's marginalisation, yen recovery — are all contingent on p_t rising above some threshold.

The paper needs to state this explicitly as a conditional claim and defend the threshold.

### Two Scenarios the Paper Must Model

**Scenario A — Nuclear Baseload Survives (p_t rises to ~0.4–0.6 by 2040)**

Conditions: AI data centre electricity demand requires dispatchable zero-carbon baseload that variable renewables cannot reliably provide at acceptable cost. Grid-scale battery storage remains insufficient for multi-day or seasonal storage. Nuclear — including thorium-cycle reactors — captures 15-25% of electricity generation in major economies.

Under this scenario, TMPI scores are meaningful. The paper's forward predictions hold with the stated timelines. p_t is calibrated against nuclear capacity growth trajectories in India, China, and France.

*Empirical evidence supporting Scenario A already in the data:* Microsoft-Three Mile Island PPA (2024), Google-Kairos Power SMR agreement (2024), Amazon nuclear deals (2024-2025), US DOE projection of 47-100 GW additional baseload demand from AI compute by 2030. These are not projections — they are signed commercial contracts. They are the single strongest piece of real-world evidence that p_t is rising, and the paper should cite them.

**Scenario B — Battery Transition Wins (p_t stays near 0)**

Conditions: Lithium-ion battery costs continue declining along the current learning curve (~18% cost reduction per doubling of cumulative capacity). Grid-scale iron-air or sodium-ion batteries achieve multi-day storage by 2035. Nuclear cannot compete on LCOE with solar-plus-storage in most markets. Thorium commercial deployment is delayed past 2050 by technical challenges.

Under this scenario, what happens to the MPI framework?

- NEP remains the dominant term, but its composition shifts: states with renewable energy self-sufficiency (solar irradiance + wind resources + domestic manufacturing) gain NEP advantage over states dependent on uranium/thorium imports
- **China's NEP actually improves under Scenario B**: China dominates solar panel manufacturing (80%+ of global supply), battery manufacturing (CATL ~37% of global market), and rare earth processing (80%+ of global supply). This is the one scenario where China's TMPI irrelevance doesn't matter — China wins the battery transition instead
- **India's NEP is mixed under Scenario B**: strong solar irradiance, large domestic market, but dependent on Chinese battery supply chains for the transition. This is the critical minerals constraint the domain panel identified
- **Gulf petrostate NEP collapses** in Scenario B regardless of thorium — neither scenario is good for hydrocarbon exporters once oil demand destruction accelerates past the tipping point

The paper should include a two-paragraph discussion of Scenario B, show what the MPI distribution looks like under that scenario, and argue — with evidence — why Scenario A is the more likely outcome. This is not a concession; it is rigour. And it preempts the "thorium is fantasy" attack from battery-transition advocates, which will be the most credible challenge the paper faces in policy circles.

### What to Add to the Paper

**In §3 (Framework):** Add a paragraph specifying p_t as conditional on energy mix outcomes. State explicitly: "The forward register predictions are conditional on nuclear energy maintaining a meaningful share (~15-25%) of global electricity generation. Under a scenario in which grid-scale battery storage achieves sufficient cost and duration to displace dispatchable baseload, p_t would remain near zero and TMPI scores would not contribute meaningfully to MPI. The paper treats Scenario A as the baseline for three reasons: [evidence from hyperscaler nuclear procurement, IEA nuclear capacity forecasts, technical constraints on long-duration storage]."

**In §9 (Forward Register):** Add a sensitivity table showing TMPI contribution under p_t = 0.1, 0.3, 0.5, 0.7. This demonstrates that even at p_t = 0.3 — a conservative nuclear share — India's monetary trajectory diverges meaningfully from China's and the Gulf states'. The paper's predictions do not require p_t → 1; they require only p_t > 0.2.

**In the falsification conditions:** Add: "If grid-scale battery storage achieves >72-hour duration at <$50/kWh by 2035 (current IEA projections suggest this is possible but not certain), p_t will remain below 0.2 and the TMPI-driven forward predictions should be treated as falsified."

---

## 2. AI Compute and the Katzenstein Filter

### The Precise Question for This Paper

The paper's Katzenstein filter explains why energy-rich states embedded in dense alliance networks channel monetary strategies through the dominant power's financial architecture. Security embedding → monetary subordination.

AI raises a parallel question: **Does compute dependency constitute a new embedding mechanism that reinforces dollar subordination independently of energy position?**

This is not an AI industry story. It is a question about whether the Katzenstein filter has a second term.

### The Argument

The paper identifies three transmission channels through which energy sovereignty translates into monetary power: trade invoicing (Ch.1), asset recycling (Ch.2), and credibility (Ch.3).

AI compute creates a **fourth channel**: infrastructure dependency. States whose critical AI infrastructure runs on US cloud platforms (AWS, Azure, Google Cloud) and US semiconductors (NVIDIA, AMD, Intel) are embedded in US technological architecture in a way that creates dollar demand independently of energy position. This is not speculative — it operates through:

- Cloud computing contracts denominated in USD
- NVIDIA GPU procurement in USD (NVIDIA's export controls create dollar-denominated scarcity)
- US CHIPS Act industrial policy channelling semiconductor investment through dollar-denominated supply chains
- Software licensing, IP royalties, and AI model access priced in USD

**The implication for the paper's India prediction:** India's TMPI = 15.8 predicts monetary rise through thorium energy sovereignty. But India's AI infrastructure is heavily dependent on US cloud (AWS India, Microsoft Azure India are the dominant platforms) and US semiconductors. Even as India achieves energy sovereignty, its compute dependency reinforces the Katzenstein filter through a new channel. The non-alignment energy argument partially escapes this — India's digital sovereignty push (data localisation laws, domestic cloud mandates) and its NVIDIA GPU procurement strategy are attempts to build compute sovereignty analogous to its energy sovereignty doctrine. But the paper does not model this tension.

**The implication for China's position:** China has invested heavily in compute sovereignty precisely because it recognised this dependency. The Huawei Ascend AI chips, domestic LLM development outside US model architectures, and CIPS as a parallel to SWIFT — these are all compute sovereignty moves that mirror the energy sovereignty logic the paper describes. China's TMPI = 4.2 understates its total strategic independence position because it misses China's compute sovereignty dimension.

**The implication for the Katzenstein filter more broadly:** The filter currently operates through energy dependence and security alliance. In a world where AI compute is as strategically central as energy, the filter has two inputs:

Modified Katzenstein Filter = f(security alliance depth, energy sovereignty, compute sovereignty)

States that achieve independence on all three dimensions have the strongest case for escaping dollar embedding. India is strongest on energy sovereignty (thorium pathway), moderate on security (Quad tension), and weakest on compute (US cloud dependency). China is moderate on security (no formal alliance but US adversary), weakest on energy (Malacca dilemma), and strongest on compute (domestic semiconductor push). Neither escapes the filter completely, but through different vulnerabilities.

### AI Electricity Demand as a p_t Accelerant

This is the most actionable AI connection for the paper.

US AI data centre electricity demand is projected by the Department of Energy at 47-100 GW of additional baseload requirement by 2030. The International Energy Agency projects global data centre electricity demand rising from approximately 460 TWh (2022) to 1,000+ TWh by 2026. Crucially: this demand is **baseload** — it runs 24/7 and cannot be met by variable renewables alone. AI hyperscalers have already demonstrated this preference through their nuclear procurement decisions.

This is an empirical accelerant for p_t that the paper should incorporate:

- The Microsoft-Three Mile Island PPA (September 2024) is the first major hyperscaler nuclear contract in decades. It is a market signal that dispatchable zero-carbon baseload has commercial demand at scale
- Google's Kairos Power agreement (October 2024) is specifically for Small Modular Reactors — the commercial technology class closest to thorium-capable designs
- Amazon's nuclear agreements (2024-2025) add further commercial validation

These are not policy interventions. They are private market actors with energy cost visibility signing long-duration baseload contracts. For the paper's monetary framework, this matters because it establishes that **the institutional demand for dispatchable nuclear exists independently of government policy** — which is precisely what the paper needs to defend against the "thorium is a government fantasy" critique.

**What to add to the paper:**

In §9 (Forward Register / p_t discussion): "The emergence of AI data centre electricity demand as a commercial driver of dispatchable baseload procurement constitutes an exogenous accelerant for p_t. Hyperscaler nuclear procurement agreements in 2024-2025 (Microsoft-Constellation, Google-Kairos, Amazon-X-energy) demonstrate private market validation of the paper's premise that nuclear's dispatchability premium commands a monetary credibility premium. These contracts are treated here as leading indicators of p_t's upward trajectory, independent of government policy."

This is one paragraph. It does not require a new section. But it grounds the p_t argument in observable 2024-2025 market data that post-dates most of the paper's citations — and it is not something incumbent fossil fuel interests can easily attack, because it is their own customers (the hyperscalers) making the nuclear investment decision.

---

## 3. What This Paper Does Not Need to Engage

The following AI and EV dimensions are **not** relevant to this paper's argument or audience and should not be added:

- EV adoption curves as consumer products
- Tesla's competitive position
- Battery chemistry (NMC vs. LFP vs. sodium-ion) beyond the storage duration question
- AI model capabilities or LLM development
- Semiconductor industry competitive dynamics
- Autonomous vehicles
- Any industry-level financial analysis of EV or AI companies

The test is simple: **does it change NEP, GS, TMPI, p_t, or the Katzenstein filter?** If no, it does not belong in this paper.

---

## 4. Summary: What to Add, Where, How Much

| Addition | Location in Paper | Length | Priority |
|---|---|---|---|
| p_t conditional on nuclear share — Scenario A vs. B | §3 Framework | 1 paragraph | Must-add |
| TMPI sensitivity table under p_t = 0.1 to 0.7 | §9 Forward Register | 1 table | Must-add |
| Battery scenario falsification condition | Falsification section | 1 sentence | Must-add |
| Hyperscaler nuclear PPAs as p_t accelerant evidence | §9 Forward Register | 1 paragraph | Must-add |
| Compute sovereignty as Katzenstein filter extension | §4 Katzenstein Filter | 1 paragraph + footnote | Recommended |
| India compute dependency as qualification to TMPI=15.8 | §7 India | 1 footnote | Recommended |
| China compute sovereignty as qualification to TMPI=4.2 | §8 China | 1 footnote | Recommended |

**Total addition:** approximately 600-800 words across the paper. No new sections required. These are precision additions that close specific analytical gaps, not new argumentative threads.

---

*These are framework extensions written for the paper's existing audience — IPE scholars, monetary economists, central bank researchers, and sovereign wealth strategists. The test applied throughout: does this change a variable in the MPI formula or the Katzenstein filter? If not, it is outside scope.*
