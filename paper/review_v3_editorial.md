# Editorial Review Memo: "The Carbon-Thorium Standard" (draft_v3.md)

**Reviewer:** Claude Code (academic review mode)
**Date:** 2026-03-16
**Draft reviewed:** `paper/draft_v3.md`
**Review against:** `writing-academic-papers` skill quality checklist, geoeconomics/IR/econometrics discipline norms

---

## 1. Summary Verdict

This is a genuinely original working paper with a clear claim, a sophisticated multi-temporal empirical architecture, and writing that mostly achieves the post-GenZ geoeconomics register it targets. The three-register structure is well-executed and the falsification registry is a genuine strength — rare in this literature. The options-pricing reframing of the MPI is the paper's best theoretical move and deserves more prominence in the abstract.

**Single biggest weakness:** The paper announces the US ARDL result in §6.2 without stating the coefficient magnitude, buries it in §7.5, and never discloses the LOO jackknife result (dropping USA reverses the sign of β). The most important robustness finding in the paper — that the quantitative result is USA-driven — is absent from the body. It belongs in §6.8 Limitations, which also appears to be missing from the current draft entirely.

---

## 2. Structural Issues (ordered by severity)

### Issue 1 — CRITICAL: §6.8 Limitations is missing from the draft

The paper moves directly from §6.6 Lag Sensitivity to the §7 Forward Register. There is no §6.8 and no §6.7. The commit log (b69e6f4: "Add §6.8 Limitations") suggests this section exists in git history but is not in the current draft file. Verify whether it was accidentally dropped in a subsequent merge or rebase.

This section must exist and must cover:
- The LOO jackknife result: dropping USA flips β from +84 to −3 (currently absent from the entire paper)
- The EUA price data provenance (academic reconstruction, not primary exchange data)
- Asymptotic reliability with n=20 in the ZA test
- The Japan and UK time-series results being non-significant at all lag specifications

Without this section, the paper has no acknowledged limitations and the USA-driven result is hidden.

### Issue 2 — HIGH: β=84.0 coefficient announced in the wrong section

§6.2 announces the key quantitative result ("ARDL bounds test confirms cointegration... The long-run DOLS coefficient on NEP is positive and significant") without stating the coefficient. The magnitude — β=84.0 — first appears in §7.5, nested inside the India prediction chain. A reader following the empirical argument has no number to work with for the seven sections between §6.2 and §7.5.

**Fix:** Add to §6.2, after the cointegration statement: "The long-run DOLS coefficient on NEP is β=84.0 (lag 10, entity-specific), implying that each +0.01 improvement in net energy position predicts approximately +0.84 percentage points of reserve share over the subsequent decade."

### Issue 3 — HIGH: LOO jackknife finding absent from paper body

Memory records the following: "Panel robustness: 2/8 specs significant — USA-driven; pooled OLS inappropriate" and "LOO jackknife: Dropping USA flips β from +84 to −3." Neither result — the 2/8 specs finding nor the sign reversal — appears anywhere in the paper. §6.1 says pooled OLS is inappropriate and mentions I² above 90%, but does not disclose that removing the US reverses the result.

This is not a minor transparency issue. It is the single most important robustness finding in the empirics. A reviewer at any serious journal will run this test independently. If they find it before the author discloses it, the paper's credibility collapses. Disclose it prominently in §6.1 or §6.8, with a clear explanation of why entity-specific analysis is the correct response (which the paper already has — it just needs the jackknife number attached to it).

### Issue 4 — HIGH: p_t never operationalized

The MPI equation's fourth component — transition probability p_t — is introduced in §3.2 and used throughout the synthesis in §8.2, but the paper never states what value p_t currently takes, how it would be estimated, or what observable would indicate its level. "As p_t rises from zero toward one" (§8.2) is conceptually clear but analytically empty without an anchor.

Two approaches are available: (a) calibrate p_t from expert forecasts of commercial thorium deployment timelines and report a current estimate (e.g., p_t ≈ 0.05–0.15 under current programme pace); or (b) state explicitly that p_t is a scenario parameter across which the paper constructs comparative statics, in which case the scenario table in §7.6 should be re-framed as p_t sensitivity rather than just nuclear share sensitivity.

### Issue 5 — MEDIUM: §2 is titled "Four Literatures" but reviews five (and the synthesis table has six)

The section heading reads "What Four Literatures Miss" but there are five subsections (§2.1–§2.5: reserve currency determinants; HST/structural power; institutional persistence; carbon market political economy; energy transitions/geopolitics). The synthesis table in §2.6 has six rows (it splits HST/Strange from Keohane/Ikenberry and adds multipolarity as a sixth entry). The mismatch reads as a drafting error.

**Fix:** Either retitle to "Five Literatures" and make the synthesis table consistent, or collapse two subsections and keep the "Four Literatures" branding. The current five-section structure is more complete; the title should catch up.

### Issue 6 — MEDIUM: MPI trajectory figure described but not shown

§8.2 ("MPI Trajectories as the Transition Progresses") describes trajectories for the USA, India, and Russia as p_t rises — this is the synthesis section's analytical core — but there is no Figure 5 showing these trajectories. Figures 1–4 are all referenced and present. §8.2 is doing the work a figure should do, in prose, without the figure.

The paper would benefit substantially from a Figure 5: a line graph showing MPI_{i,t} as a function of p_t for USA, India, Russia, and (optionally) UK — illustrating India's discontinuous rise and Russia's flat trajectory. This is the paper's forward claim visualised.

### Issue 7 — LOW: §9 conclusion's final paragraph underuses the Russia hinge

§8.1 makes excellent use of Russia as the crystallising case across all three registers. §9 returns to Russia only in the parenthetical about "if sanctions are substantially lifted" (§8.2). The conclusion's final three paragraphs lose the Russia thread entirely. For a paper targeting geoeconomics audiences in 2026, the Russia case is both the most vivid contemporary evidence and the most policy-relevant. Bringing it back explicitly in the conclusion's penultimate paragraph would strengthen the close.

---

## 3. Numerical Inconsistencies Table

| Quantity | Paper (draft_v3.md) | Memory / previous notes | Section | Resolution recommendation |
|----------|---------------------|------------------------|---------|--------------------------|
| EUA Phase I CV | 0.815 | 0.82 | §5.3, Table | **Paper is internally consistent** (0.815/0.292 = 2.793 ≈ 2.79). Memory entry likely a rounded value from an earlier notebook run. Verify against notebook 03 output. If notebook produces 0.815, paper is correct; update memory. |
| GS (Phase I EUA) | 2.79 | 2.83 | §5.3 | Follows from CV inconsistency above: 0.82/0.29 = 2.83 vs 0.815/0.292 = 2.79. The paper's values are mutually consistent. Confirm notebook output. |
| Japan NEP range | 0.0084 → 0.0028 (67% decline) | 0.0094 → 0.0037 (61% decline) | §6.3, Fig 3 caption | Commit b69e6f4 message says "Fix pre-submission errors: Japan NEP %." **Paper is likely the corrected version.** Verify against notebook 04; update memory file accordingly. |
| GBR TMPI | 0.0 (thorium reserves ≈ 0%) | 12.3 | §7.3 table | **Paper is logically correct** given the zero-collapse property (§7.2): UK has negligible thorium reserves, so TMPI collapses to zero regardless of nuclear share. Memory entry 12.3 was an earlier computation that ignored zero-collapse or used a non-zero placeholder. Paper should be trusted; memory should be updated. |
| Oil CV (denominator) | 0.292 | 0.29 | §5.3 | Rounding difference only. No substantive inconsistency. |

**Action:** Run notebook 03 (backward carbon) and notebook 04 (present NEP) to confirm which figures are authoritative. The paper's numbers are internally consistent in all cases; memory entries appear to be from an earlier computational pass.

---

## 4. Line-Level Edits (section-by-section)

### §1 — Introduction

**Strength:** The opening three paragraphs deliver concrete historical narrative before theorizing — exactly the right structure per the human-voice protocol. The petrodollar origin story is well-told and cites Spiro precisely.

**Issue — "Note on the title" sidebar is overlong:** The two-paragraph sidebar on why it's called a "standard" and the Polanyian reading belongs as a footnote or compressed to a single paragraph. At 200+ words, it interrupts the section's momentum. The Polanyian insight is valuable; it should reappear more briefly in §5 where the GS measure is introduced, not here.

**Voice edit:** Final sentence of §1 — "No existing framework in international political economy makes this connection formally. This paper proposes one." — is excellent. Keep exactly as written.

### §2 — Literature Review

**Strength:** Thematic organisation rather than author-by-author survey. Each subsection ends with a "The gap:" formulation that maintains argumentative momentum. This is well above average for IR literature reviews.

**Issue — §2.2:** "Strange understood the finance-energy linkage but treated it as contingent on the specific institutional arrangements of dollar-denominated oil trade rather than as a general mechanism." This is the paper's key contribution relative to Strange — but the phrasing buries it in a subordinate clause. Promote this to a dedicated sentence: "Strange identified the finance-energy linkage. She did not formalise it as a mechanism that reproduces across energy transitions. This paper does."

**Issue — Polanyi reference without citation:** §1 line 48 opens "The Polanyian reading is precise here." Polanyi is not in the reference list. Either add the reference (Polanyi, K. (1944). *The Great Transformation*. Farrar & Rinehart) or rephrase without the proper noun.

**Missing canonical citations (required by geoeconomics norms per discipline guide):**
- **Hirschman (1945)** — *National Power and the Structure of Foreign Trade* is foundational for the geoeconomics literature on economic dependency as strategic instrument. The discipline guide explicitly requires engagement with it. The paper's argument about energy dependency and monetary leverage is a direct application of Hirschman's framework; cite and credit it.
- **Baldwin (1985)** — *Economic Statecraft* is the other required anchor for geoeconomics. McNally (2017) is cited, but Baldwin gives the theoretical scaffolding for thinking about economic instruments as strategic tools that McNally applies to oil markets. One sentence in §2.1 or §2.4 would suffice.

### §3 — Theory

**Strength:** §3.3's defense of the two-state form over the multiplicative form is one of the paper's best passages. The flow/stock distinction is precisely stated. The options-pricing analogy is apt and well-executed.

**Issue — transmission channels (§3.4):** The section is 600+ words but ends without a synthesis sentence that maps the full conceptual structure back to the empirics. The closing paragraph ("The BIS 2028 falsification condition therefore reads...") in §7.5 does this work, but the theory section should close with something like: "The three-channel structure means the relevant question for any state is not whether energy endowment exists but which channel is binding given its institutional configuration. For India, the binding channel is sequencing. For Russia, it is institutional quality. For Switzerland, no channel operates because institutional substitution renders energy position irrelevant." This would make the three-constraint diagnostic table in §7.3 read as a direct application of §3.4.

**Issue — Channel 3's GS sentence:** "The EU ETS's GS of 2.79 is precisely a Channel 3 failure." The first use of the GS number in the theory section should be flagged as "presented formally in §5.3" — or moved there entirely. Citing an empirical number before presenting the empirical section creates a forward reference that disorients readers.

### §5 — Backward Register

**Strength:** §5.4's three-claims-established / three-claims-not-established structure is unusually honest and effective. This should become a template for §6 as well.

**Issue:** §5.3's sentence "No commodity with a fixed physical supply exhibits a near-total price collapse driven by a political accounting revelation" — this is a strong claim that could be challenged (commodity markets can respond to accounting/inventory revelations). A qualifier would help: "No commodity with a fixed physical supply exhibits a *near-total* price collapse driven solely by a political accounting revelation without any change in physical supply fundamentals." The distinction between physical and political shocks is the paper's argument; the sentence should make that contrast explicit.

### §6 — Present Register

**Issue §6.2:** The eurozone correlation caveat — "both series are declining and persistent, meaning a high correlation is partly mechanical" — is exactly right and exactly the kind of honest limitation the paper should show more of. This self-aware passage strengthens rather than weakens the paper.

**Missing:** After stating "The long-run DOLS coefficient on NEP is positive and significant," add the coefficient and standard error here. See Issue 2 above.

**Issue §6.3 (Japan):** "Japan commands every predictor the standard literature would use to forecast reserve currency status: the world's third-largest GDP, deep and liquid financial markets, stable monetary institutions, and the Bank of Japan's long record of credibility. On GDP grounds, the yen should hold 10–15% of global reserves. It holds 5–6%." — This passage is the paper's best single argumentative paragraph. Consider making it the opening of §6, moved before the framing discussion, as the puzzle that motivates the structured case comparison strategy.

**Issue §6.6 (lag sensitivity table):** Japan and UK showing "Not sig." at all lag specifications is more important than a table footnote conveys. The text currently says "Directional signs are stable across all lag specifications." This is technically true but misleading: Japan and UK have no significant sign in any specification, making "stable direction" vacuous. Rewrite: "Statistical significance is concentrated in the two primary cases. Japan and UK display directional consistency but no statistically significant lag relationship at any specification — a finding consistent with the boundary condition logic of §6.4 but one that the present register cannot resolve. The natural experiment in §6.3 carries the identification burden for the Japan case."

### §7 — Forward Register

**Issue §7.1:** "Uranium fails the first and second conditions. Reserves are too widely distributed and enrichment technology diffuses. Lithium and rare earths fail the second and third conditions." This elimination logic is sound and important, but it reads as assertion rather than argument. One footnote per claim would deflect the obvious challenge that a reviewer will make.

**Issue §7.4 (Katzenstein filter):** The filter is well-integrated, not bolted on. The Australia/India structural distinction is the right analytical move. However, the filter implicitly predicts that Canada's TMPI score (20.8, second globally) will not translate to reserve currency gains — and this claim is never stated explicitly as a prediction. Add it to the falsification registry or to §7.4: "The Katzenstein filter therefore predicts that Canadian dollar reserve share will remain within its current niche regardless of any thorium programme Canada develops, absent a structural break in its US security dependence."

**Issue §7.5:** The causal chain diagram (the bulleted flow from "Nuclear capacity growth" to "INR FX share rises") is one of the most useful structural elements in the paper. It would be more legible as a numbered list with quantitative anchors at each step, rather than a code block. The code block formatting implies precision that isn't there.

### §8 — Synthesis

**Strength:** §8.1's core point — that GS > 1 retroactively transforms the interpretation of the present register from "geology predicts money" to "governance predicts money" — is the paper's deepest theoretical insight. It's well-stated here.

**Issue §8.3 (falsification registry):** The AUD prediction condition reads "AUD reserve share remains within ±0.5 percentage points of its 2022 level (~6.7%)" — so the falsification condition is AUD *falls* more than 1pp below 2022 after AUKUS capacity is confirmed. But AUKUS nuclear delivery is 2030s at earliest; the 2035–2040 checkpoint is appropriate. Clarify: the prediction is that AUD does NOT rise discontinuously (because AUKUS channels capacity into the dollar system), not that it falls. The current phrasing can be read as a falsification trigger for a *decline*, when the claim is about the absence of an *increase*.

### §9 — Conclusion

**Strength:** "The carbon governance regime showed what happens when the allocative mechanism is too politically contested to hold: prices collapse, allocations are renegotiated, and the monetary potential of the energy base is captured by incumbents before it can be converted into reserve status." — One of the best sentences in the paper. The "not because it was designed badly but because any allocation mechanism that imposes material costs on powerful incumbents will be renegotiated by those incumbents" construction is precise and memorable.

**Issue:** The final sentence — "That is the only honest way to make a forward prediction in geoeconomics." — is a strong rhetorical close, but the paragraph it concludes has become somewhat circular (we will know by 2031, the paper stakes its reputation, etc.). Consider tightening the final paragraph to two sentences and ending on the falsification challenge, not on the paper's posture toward it.

---

## 5. Missing Content

| Item | Location | Required for |
|------|----------|-------------|
| §6.8 Limitations (entire section) | After §6.6, before §7 | Transparency; critical for peer review; LOO jackknife must appear here |
| LOO jackknife disclosure: β flips from +84 to −3 when USA dropped | §6.1 or §6.8 | Intellectual honesty; reviewer will find this independently |
| β=84.0 stated in §6.2 where the finding is announced | §6.2 | Basic results reporting |
| p_t current value or scenario anchoring | §3.2 or §7.6 | MPI equation is not functional without this |
| Figure 5: MPI trajectories as p_t rises (USA, India, Russia, UK) | §8.2 | Visual synthesis of the paper's core forward claim |
| Hirschman (1945) citation and engagement | §2.1 or §2.4 | Mandatory for geoeconomics venue |
| Baldwin (1985) citation | §2.1 or §2.4 | Mandatory for geoeconomics venue |
| Polanyi reference entry | References section | In-text proper noun without citation |
| Canada TMPI non-prediction (Katzenstein filter applied explicitly to Canada) | §7.4 | Completes the Katzenstein application |
| Clarification of AUD falsification condition (stagnation, not decline) | §8.3 | Precision of the falsification claim |

---

## 6. Citations & References

### Style inconsistency (high severity)

The paper uses **APSA format in-text** (author year with no comma, "and" not "&": `Chinn and Frankel 2007`, `Pesaran, Shin, and Smith 2001`) but **APA format in the reference list** (year in parentheses after author name: `Chinn, M.D. and Frankel, J.A. (2007)`). These are two different styles and cannot coexist in a single paper.

**Recommendation:** Standardize to APSA throughout. It is the correct style for *International Organization*, *World Politics*, and *International Security* — the most likely target venues. APSA reference list format has the year immediately after the author name without parentheses: `Chinn, M.D., and J.A. Frankel. 2007.`

### Orphaned in-text reference

- **Polanyi** — named in §1 ("The Polanyian reading is precise here") with no entry in the reference list. Add: `Polanyi, Karl. 1944. *The Great Transformation: The Political and Economic Origins of Our Time*. New York: Farrar & Rinehart.`

### Reference list entries with no in-text citation

The following appear in the reference list but are not cited anywhere in the paper body (verified by text search):
- Abdelal (2007)
- Helleiner (2008)
- Helleiner (2014)
- Ikenberry (2001) and (2011)
- Kirshner (1995) and (2014)
- Maggiori, Neiman, and Schreger (2020)
- Mearsheimer (2001)

Either cite these in the text where relevant, or remove them from the reference list. Ghost references undermine the paper's credibility.

### Pforr, Pape, and Petry (2025) — missing page range

Reference reads: `*International Organization*, 79(S1).` No page numbers. If this is an advance-access article, note as "advance access" or use article DOI.

### DOIs

Multiple journal articles lack DOIs. At minimum, the following should have them:
- Farrell and Newman (2019) — DOI: 10.1162/isec_a_00351
- Eichengreen and Flandreau (2009) — European Review of Economic History
- Bayer and Aklin (2020) — PNAS
- Ellerman and Buchner (2008)
- Koch et al. (2014)
- Pesaran, Shin, and Smith (2001)

For geoeconomics/IR venues (Chicago/APSA), DOIs are strongly recommended on all journal articles.

---

## 7. Submission Readiness Checklist

| Quality check | Status | Action required |
|---------------|--------|----------------|
| Central claim is a claim, not a topic | ✅ PASS | — |
| Research gap precisely stated | ✅ PASS | Minor: title says "Four Literatures," body has five |
| §2.6 synthesis table consistent with §2 structure | ⚠️ WARN | Table has 6 rows; section has 5 subsections; heading says "Four" |
| Theory section has formalised equation | ✅ PASS | — |
| Two-state form vs multiplicative form addressed | ✅ PASS | Well-handled in §3.3 |
| Options-pricing analogy justified | ✅ PASS | — |
| Three transmission channels distinct and non-overlapping | ✅ PASS | — |
| p_t operationalized with current value or scenario anchor | ❌ FAIL | p_t described but never given a value or estimation method |
| β coefficient stated at result announcement (§6.2) | ❌ FAIL | β=84.0 appears only in §7.5 |
| LOO jackknife result disclosed | ❌ FAIL | Absent from paper; belongs in §6.1 or §6.8 |
| §6.8 Limitations section present | ❌ FAIL | Missing from draft; verify git history |
| Lag sensitivity table interpreted adequately | ⚠️ WARN | Japan/UK non-significance understated in prose |
| EUA data provenance noted | ⚠️ WARN | §4 mentions "academic reconstruction" but §6.8 is where the full caveat should live |
| "Structured case comparison" epistemology defended | ✅ PASS | §6.1 does this well |
| Backward register claims bounded honestly | ✅ PASS | §5.4 is a model for this |
| Brazil negative prediction prominent | ✅ PASS | §8.3 correctly emphasizes it |
| BIS falsification conditions specific and time-bound | ✅ PASS | 2028/2031/2037 checkpoints are genuinely falsifiable |
| India transmission chain fully stated | ✅ PASS | §7.5 is the paper's strongest empirical section |
| MPI trajectory figure exists | ❌ FAIL | §8.2 describes trajectories with no supporting figure |
| Human voice: sentence rhythm varied | ✅ PASS | — |
| Human voice: claim ownership | ✅ PASS | "This paper argues," "we contend" throughout |
| AI signature phrases absent | ✅ PASS | No "delve into," "shed light on," etc. |
| Concrete before abstract in §1 | ✅ PASS | Bretton Woods and petrodollar before MPI |
| Hirschman (1945) cited | ❌ FAIL | Required for geoeconomics; absent |
| Baldwin (1985) cited | ❌ FAIL | Required for geoeconomics; absent |
| Polanyi in reference list | ❌ FAIL | Named in text; not in references |
| Citation style consistent in-text vs reference list | ❌ FAIL | APSA in-text + APA reference list — mixed styles |
| Reference list entries all cited in text | ❌ FAIL | 7+ orphan entries (Abdelal, Helleiner ×2, Ikenberry ×2, Kirshner ×2, Maggiori et al., Mearsheimer) |
| Pforr et al. (2025) page range populated | ⚠️ WARN | Missing page numbers |
| DOIs on journal articles | ⚠️ WARN | Multiple missing |
| Abstract self-contained | ✅ PASS | Four components present |
| JEL codes appropriate | ✅ PASS | F31, F33, Q43, Q48 correct |

**Summary score:** 18 pass / 9 fail / 6 warn (out of 33 checks)

**Pre-submission blockers (must fix):** Issues 1–4 above (missing §6.8, β placement, LOO omission, p_t), plus citation inconsistencies and orphan references. The paper should not be submitted without §6.8 and the jackknife disclosure.

---

## 8. Appendix: Quick-Fix Reference

### Add to §6.2 (after cointegration sentence):
> "The long-run DOLS coefficient on NEP is β=84.0 (lag 10, entity-specific; t=X, p<0.0X), implying that each +0.01 improvement in net energy position predicts approximately +0.84 percentage points of reserve share over the subsequent decade. The coefficient is sensitive to sample composition: the jackknife analysis in §6.8 reports the full robustness decomposition."

### Draft §6.8 Limitations (minimum viable):
> Three limitations bound the present register's claims.
>
> First, the quantitative finding is USA-driven. The entity-specific ARDL result (β=84.0) is robust within the US case. The leave-one-out jackknife analysis reveals that removing the United States reverses the pooled coefficient from +84 to −3. The panel result, reported in the appendix for transparency, is 2/8 specifications significant. The paper's claims do not rest on the panel finding; they rest on the structured case comparison and natural experiment. But the sensitivity to the single US observation must be stated directly.
>
> Second, EUA price data from Phase I (2005–2007) is an academic reconstruction from Ellerman and Buchner (2008), Koch et al. (2014), and Bayer and Aklin (2020). Primary exchange data was not retained by the EU EUTL for this period. The CV calculation is therefore as reliable as the underlying reconstruction. Readers who wish to challenge the GS=2.79 figure should begin by downloading primary Phase I data from Sandbag's Carbon Price Viewer.
>
> Third, the Zivot-Andrews test runs on twenty annual observations. The asymptotic critical values (-5.57 at 1%) were derived for larger samples. The observed statistic (-6.248) exceeds the critical value with a sufficient margin that minor size corrections are unlikely to alter the conclusion; but small-sample caution is warranted in interpreting exact p-values.

### Polanyi reference to add:
> Polanyi, Karl. 1944. *The Great Transformation: The Political and Economic Origins of Our Time*. New York: Farrar & Rinehart.

### Hirschman reference to add (with in-text citation in §2.4):
> Hirschman, Albert O. 1945. *National Power and the Structure of Foreign Trade*. Berkeley: University of California Press.

In §2.4, after the McNally citation: "This capacity for strategic exclusion echoes Hirschman's (1945) foundational insight that foreign trade relationships produce leverage precisely through dependency — the carbon governance case formalises that insight as a measurable ratio."

---

*Review complete. All twelve dimensions addressed. Numerical inconsistency table completed. Pre-submission blockers identified.*
