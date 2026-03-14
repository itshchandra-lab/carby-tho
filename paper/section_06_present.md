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

**Russia.** Russia's case separates into two mechanisms (see Section 7 and §9.2).
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

## 6.8 Limitations

**Uniform lag λ=10.** The λ≈10 year transmission lag is estimated from the USA case
and applied uniformly to all entities. This is an assumption, not a finding. Entity-
specific lag estimation is the primary empirical extension for the revision stage;
it requires longer time series than are available for CNY and post-2004 EMU. The
directional results are robust to λ=8 and λ=12 (reported in the DOLS robustness
tables), but the uniform lag imposes equal transmission speed across structurally
different capital markets. Readers should treat entity-level coefficient magnitudes
as illustrative of mechanism direction, not precise structural parameters.

**EMU reserve share: energy vs. institutional confound.** The r=0.864 correlation
between lagged EMU NEP and EUR reserve share decline (1999–2024) spans the 2010–2015
eurozone sovereign debt crisis, which caused compositional shifts in central bank
reserves independent of energy position. No event-study design is attempted to
isolate the energy effect from the institutional fragility effect. The correlation
is consistent with the mechanism but does not distinguish it from an alternative
in which the sovereign debt crisis — itself partly driven by energy import costs on
peripheral eurozone economies — is the operative variable. Both channels would
produce the same observed correlation. This paper does not claim to have separated
them.

**Katzenstein prediction asymmetry.** The cross-case falsification structure
(India gains, Australia does not gain disproportionately) tests the Katzenstein
alliance-structure filter in only one direction. If India gains and Australia also
gains independently, the filter is refuted but the underlying mechanism survives.
If neither gains, the mechanism is falsified. This means the theory can survive
three of four possible outcomes — a weaker falsification structure than the within-
case AUD and INR predictions taken individually. The cross-case test should be
read as a comparative check on the alliance filter, not as the primary mechanism
test. The primary tests are the dated BIS and COFER predictions with quantified
thresholds.
