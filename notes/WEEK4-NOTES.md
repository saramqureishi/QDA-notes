# Week 4: Count Data & Table Analysis — Full Notes

> **Learning outcomes:** After this you can (1) recognise when data is "count data in a table",
> (2) test whether two categorical variables are related using chi-square or Fisher's exact test,
> and (3) interpret the result.

---

## 1. The gap this week fills

The lecture opens with a real story: clinicians found that a **shorter** antibiotic course seemed
to cause fewer post-op infections (3.6% vs 18.2%). They wrote it up... and got **rejected from the
journal** — because they only *reported the numbers*, they never **tested** whether the difference
was real or just chance.

> **The lesson:** having the counts and percentages is NOT the same as testing the hypothesis.
> (And it applies to AI too — don't trust a descriptive summary as if it answered the question.)

So far we've tested: a mean, a proportion, normality, equal variances, equal means. **None of those
fit this situation** — two categorical variables, and we want to know if they're *related*.

---

## 2. What is count data / a contingency table?

Lots of data comes as **counts** — number of patients with/without infection, number of people with
each hair+eye colour combination. When you cross two categorical variables you get a
**contingency table** (a.k.a. cross-tabulation):

```
              Blue Eyes   Brown Eyes
Fair Hair        38          11
Dark Hair        14          51
```

The question: **are hair colour and eye colour independent (unrelated), or is there a relationship?**

---

## 3. The hypotheses (ALWAYS the same for these tests)

- **H₀: the two variables are INDEPENDENT** (no relationship)
- **H₁: the two variables are NOT independent** (there is a relationship)

This never changes for a test of independence. Memorise it.

---

## 4. The logic: Observed vs Expected

The test compares what you **observed** against what you'd **expect if H₀ (independence) were true**.

### Computing expected counts
If the variables were independent, the expected count in each cell is:

```
E = (Row total × Column total) / Grand total
```

**Example** (fair hair & blue eyes): row total 49, column total 52, grand total 114
→ E = (49 × 52) / 114 = **22.35**
But we **observed 38**. That's a big gap → maybe they're NOT independent.

Full expected table:
```
              Blue Eyes   Brown Eyes   Row Total
Fair Hair       22.35       26.65         49
Dark Hair       29.65       35.35         65
Col Total        52          62          114
```
(Note: the row/column/grand totals stay identical — only the inside changes.)

---

## 5. The Chi-Square (χ²) test

The test statistic measures the total gap between observed and expected:

```
χ² = Σ (O − E)² / E
```
- Big χ² = observed is far from "independence expected" = evidence of a relationship.
- R converts χ² to a **p-value**, read exactly like every other test:
  - **p < 0.05 → reject H₀ → the variables ARE related**
  - p ≥ 0.05 → fail to reject → no evidence of a relationship

### In R
```r
chisq.test(mytable)
```
- R applies a **continuity correction** by default, so a by-hand answer will differ slightly.
  Disable it with `chisq.test(mytable, correct = FALSE)`.
- For the hair/eye example, χ² ≈ 35.3, p is tiny → **reject H₀ → hair and eye colour are linked.**

---

## 6. ⚠️ The CRITICAL assumption: expected counts ≥ 5

> **Chi-square is only reliable if all EXPECTED cell counts are ≥ 5.**

If any expected count is **< 5** (usually from a small sample), χ² is unreliable.
- **R won't stop you** — it still prints a p-value, with only a quiet warning
  *"Chi-squared approximation may be incorrect."* Easy to miss!
- **The fix:** use **Fisher's Exact Test** instead.

This is the week's single most important practical rule, and the "AI cautionary tale" at the end of
the lecture: a careless analyst (or LLM) runs `chisq.test` on a tiny table, ignores the warning, and
reports a bogus p-value. **Always check expected counts first.**

---

## 7. Fisher's Exact Test (for small samples)

When expected counts are small, use:
```r
fisher.test(mytable)
```
- It computes the **exact** probability of the observed table (and more extreme ones) — no
  large-sample approximation needed.
- Interpreted the same way: **p < 0.05 → reject independence.**
- **Employment example:** profession × employment status, small counts → use Fisher → p = 0.38 →
  **fail to reject H₀ → independent** (no link between profession and employment status here).
- Bonus: `fisher.test()` also reports an **odds ratio** (see effect size below).

**Handy shortcut:** the `gmodels` library's `CrossTable()` function picks the appropriate test for you.

---

## 8. Back to the antibiotics
```
              short-AB   long-AB
No infection     27         18
Infection         1          4
```
This has a cell (Infection + short-AB = 1) that will give a small expected count → use
**Fisher's exact test**. That's what the original researchers should have done to actually *test*
their hypothesis.

---

## 9. Effect size for tables (worth knowing)

p-value tells you *if* there's an association; effect size tells you *how strong*:
- **Odds ratio** (2×2 tables): how many times more likely the outcome is in one group. OR = 1 → no
  association; far from 1 → strong. `fisher.test()` reports it (antibiotics ≈ 5.8 → odds of infection
  ~5.8× higher in one group).
- **Cramér's V**: general association strength, 0 (none) to 1 (perfect); works for bigger tables.

---

## 10. Optional extras (good awareness, low priority)

- **Critical value method:** instead of comparing p to α, compare χ² to a critical value from the
  χ² distribution. df for an r×c table = (r−1)(c−1). For 2×2, df=1, critical value at 95% =
  `qchisq(0.95, 1)` = 3.84. χ²=35.3 > 3.84 → reject. (Same conclusion, different route.)
- **Goodness-of-fit test:** χ² can also test if ONE variable matches an expected distribution
  (e.g. is a die fair?). df = k−1 for k categories.
- **McNemar's test** (`mcnemar.test()`): for *paired/matched* categorical data (e.g. same patients
  before vs after) — χ² and Fisher assume **independent** samples.
- **Multiple testing:** test many pairs and some come up "significant" by chance. Bonferroni fix:
  divide α by the number of tests.
- **Simpson's Paradox:** an association in a pooled table can **reverse** when you split by a third
  variable (famous: Berkeley 1973 admissions). Always ask: is a hidden third variable driving this?

### Not assessed / real-world flavour
χ² and Fisher are **non-parametric** (no distribution assumption). Same table logic powers A/B
testing, epidemiology/vaccine studies, genomics case-control, churn analysis, and **auditing AI
systems for fairness** (group × outcome: are error rates independent of gender/ethnicity?).

---

## 11. Week 4 cheat sheet

1. **Two categorical variables + "are they related?" → contingency table + chi-square/Fisher.**
2. **H₀: independent. H₁: related.**
3. **E = (row total × col total) / grand total.**
4. **All expected counts ≥ 5 → `chisq.test()`. Any < 5 → `fisher.test()`.**
5. **p < 0.05 → reject H₀ → the variables ARE related.**
6. Report an **effect size** (odds ratio / Cramér's V) alongside p.
7. **Watch the "approximation may be incorrect" warning** — it means your sample is too small for χ².

### R commands
```r
mytable <- table(df$var1, df$var2)   # build the contingency table
chisq.test(mytable)                  # chi-square test of independence
chisq.test(mytable, correct = FALSE) # without continuity correction
fisher.test(mytable)                 # use when expected counts < 5
qchisq(0.95, df)                     # chi-square critical value
mcnemar.test(mytable)                # paired/matched categorical data
```
