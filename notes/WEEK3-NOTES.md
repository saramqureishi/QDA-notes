# Week 3: Inferential Statistics Part 2 — Hypothesis Testing (Full Notes)

> **Learning outcomes:** write H₀/H₁, run the right test in R, interpret the p-value, and report effect size.
> Textbook: Crawley Ch. 6.

---

## 1. The question this week answers
Week 2: *"What range of values is plausible for the true value?"* (confidence interval)
**Week 3: *"Is this specific claim believable — or did I just get a fluke sample?"*** (hypothesis test)

## 2. The two hypotheses
| | Symbol | Meaning | Example (flour bags) |
|---|---|---|---|
| Null | H₀ | the claim / status quo — what we try to disprove | µ = 2 kg |
| Alternative | H₁ | what we suspect instead | µ ≠ 2 kg |

- **Two-sided:** H₁: µ ≠ µ₀ → `alternative = "two.sided"` (default)
- **One-sided:** H₁: µ > µ₀ → `"greater"` · H₁: µ < µ₀ → `"less"`
- Clue words: "different / working correctly" → two-sided; "increased / in excess of / more" → greater; "lighter / fewer / decreased" → less.

## 3. The p-value
> **If H₀ were true, what is the probability of seeing a sample this extreme (or more extreme)?**

- Small p → sample would be rare under H₀ → **reject H₀**
- Large p → sample is ordinary under H₀ → **fail to reject H₀**
- **"If the p-value is low, the null must go."** Rule: **p ≤ α → reject** (α usually 0.05; sometimes 0.01).
- ❌ The p-value is NOT the probability that H₀ is true.
- Say "fail to reject H₀", not "accept H₀" (absence of evidence ≠ proof).

## 4. The 4-step process (use this layout in every answer)
1. **State** H₀ and H₁
2. **Compute the test statistic** (R)
3. **Get the p-value** (R)
4. **Compare p to α and conclude in plain English, in context**

Test statistic idea: `(observed − value claimed by H₀) / standard error`. Far from the claim → big statistic → small p.

## 5. Which test for which question
| Question | R | H₀ |
|---|---|---|
| One mean vs claimed value (one-sample t) | `t.test(x, mu = v, alternative = ...)` | µ = v |
| One proportion vs claimed value | `prop.test(successes, n, p = v, alternative = ...)` | π = v |
| Is the data normal? | `shapiro.test(x)` + `qqnorm(x); qqline(x)` | data is normal |
| Two variances equal? | `var.test(x, y)` | σ₁² = σ₂² |
| Two means equal? | `t.test(x, y)` (Welch is used automatically if variances differ) | µ₁ = µ₂ |
| Two means, non-normal data (optional) | `wilcox.test(x, y)` | same location |

- **Reading `shapiro.test`:** p < 0.05 → **NOT normal**; p ≥ 0.05 → normality is a reasonable assumption.
- **Check normality within each group** before a two-sample t-test (a pooled column can fail just because it mixes groups).
- `prop.test` needs a large enough sample: n·π₀ ≥ 5 and n·(1−π₀) ≥ 5.

## 6. Effect size
- p tells you **whether** there is a difference; **effect size tells you how big it is**.
- **Cohen's d:** `library(effsize); cohen.d(x, y)` → roughly 0.2 small, 0.5 medium, **0.8+ large**.
- Huge samples can make a tiny difference "significant" → always report **p + effect size**.

## 7. Errors (NOT assessed — awareness only)
- **Type I (α):** rejecting H₀ when it is true (false alarm)
- **Type II (β):** failing to reject H₀ when it is false (missed effect). Power = 1 − β.

## 8. Lecture worked examples
- **Heights:** µ₀ = 143, x̄ = 148, s = 4.9, n = 30 → z = 5.6, p ≈ 0.0001 → **reject H₀**.
- **Gumball:** H₀: π = 0.5, H₁: π < 0.5, 42/100 red → p ≈ 0.07 → **fail to reject H₀**.
- **Gardens (ozone):** `t.test` p = 0.0011 → means differ; Cohen's d = −1.73 (large).

---

## 9. ✅ LAB 3 PART 1 — run by Sara in RStudio, with interpretation

| Example | Hypotheses | Key output | Decision (α = 0.05) | Plain-English conclusion |
|---|---|---|---|---|
| 1. Flour bags (n = 20) | H₀: µ = 2, H₁: µ ≠ 2 | t = −1.19, p = 0.2496, 95% CI (1.913, 2.024) | **Fail to reject** | No evidence the machine is off. 2.0 lies inside the CI, which agrees with the test. |
| 2. Drug therapy (43/50 = 0.86) | H₀: π = 0.75, H₁: π > 0.75 | p = 0.05124 | **Fail to reject (just)** | 86% looks better than 75%, but 0.05124 > 0.05. **Don't round the p-value.** |
| 3(i). Iris petal length | H₀: µ = 4, H₁: µ ≠ 4 | mean 3.758, p = 0.095 | **Fail to reject** | Mean petal length isn't significantly different from 4. |
| 3(ii). Normality, all iris | H₀: normal | Shapiro W = 0.876, p = 7.4e-10 | **Reject** | NOT normal. The column mixes 3 species, so it's 3 bell curves blended together. |
| 4(i). Normality by species | H₀: normal | versicolor p = 0.1585, virginica p = 0.1098 | **Fail to reject** | Each species is reasonably normal, so the t-test assumption holds. |
| 4(ii). Versicolor vs virginica | H₀: µ₁ = µ₂ | Welch t = −12.6, p < 2.2e-16, CI (−1.50, −1.09); means 4.26 vs 5.55 | **Reject** | Means differ. The CI excludes 0, which agrees with the test. |
| 4(iii). Effect size | — | Cohen's d = −2.52 (large) | — | The difference is significant **and** large. |
| 4(iv). Variances (optional) | H₀: equal variances | F = 0.099, p = 1.9e-13, CI (0.056, 0.174) | **Reject** | Setosa's variance is much smaller. The CI excludes 1. |

**Reading tricks learned:**
- A CI that **contains** the H₀ value (or 0 for a difference, or 1 for a ratio) → not significant. One that **excludes** it → significant.
- The warning `package 'effsize' was built under R version ...` is harmless.

## 10. ⏳ LAB 3 PART 2 (independent practice) — NOT DONE YET
Data: `BreastCancer_Wisconsin.csv` (diagnosis M/B, radius.mean, radius.sd, radius.max)
1. Synthetic diamonds: weights 0.46, 0.61, 0.52, 0.48, 0.57, 0.54. Is the mean **in excess of 0.5**? Test at **α = 0.01**, one-sided (`alternative = "greater"`).
2. Breast cancer: (a) read in · (b) explore · (c) proportion benign · (d) test H₀: π = 0.6 at α = 0.05 · (e) 95% CI for the proportion benign · (f) explore radius.mean · (g) is radius.mean different for B vs M? (check normality per group first) · (h) Cohen's d.
- Optional: repeat for radius.sd; compare with `wilcox.test`; what Type I / Type II errors would mean in a cancer-diagnosis setting.

## 11. Week 3 cheat sheet
1. Write H₀/H₁ (watch the direction words). 2. Pick the test from the table. 3. **p ≤ α → reject H₀.**
4. Check assumptions (normality per group; sample size for prop.test). 5. Cross-check with the CI. 6. Report the effect size.
