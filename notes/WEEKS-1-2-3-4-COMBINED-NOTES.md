# QDA — Combined Notes: Weeks 1, 2, 3 & 4
### (Lecture companion — glance at this while the lecture is running)

> **The whole story in one line:**
> **W1** describe your data → **W2** estimate the true value with a range (confidence interval) →
> **W3** test a claim about a mean/proportion (hypothesis testing) →
> **W4** test whether two *categorical* variables are related (tables).

---
---

# ⭐ THE QUICK-GLANCE CHEAT SHEET (read this if nothing else)

### STEP 0 — Decide variable type. It controls every choice.
- **Categorical** = labels (Grassland, M/B, TRUE/FALSE) → frequency table, bar/pie chart
- **Numerical** = quantities you can average (3.6, 148, 0.42) → mean/median/SD, histogram/box plot
- ⚠️ Numbers can be categorical (group "1"/"2"). Ask: *does averaging it make sense?*

### THE DECISION TREE — "which test do I use?"
```
What am I asking about?
├─ One MEAN vs a claimed value ............... t.test(x, mu = value)
├─ One PROPORTION vs a claimed value ......... prop.test(successes, n, p = value)
├─ Compare TWO means ......................... t.test(x, y)
├─ Compare TWO variances ..................... var.test(x, y)
├─ Is my data NORMAL? ........................ shapiro.test(x)  (+ qqnorm/qqline)
└─ Are TWO CATEGORICAL variables related?
      ├─ all expected counts ≥ 5 ............. chisq.test(table)
      └─ any expected count  < 5 ............. fisher.test(table)
```

### THE P-VALUE RULE (Weeks 3 & 4 core)
> **"If the p-value is low, the null must go."**
> **p ≤ 0.05 → reject H₀** (significant). **p > 0.05 → fail to reject H₀** (not enough evidence).

### CONFIDENCE INTERVAL rules (Week 2 core)
- Bigger sample → **narrower** CI. Higher confidence (95→99%) → **wider** CI.
- CI **contains** the claimed value → NOT significant. CI **excludes** it → significant.

### EFFECT SIZE (report alongside p — significance ≠ importance)
- Two means → **Cohen's d** (`cohen.d`): >0.8 = large.
- 2×2 table → **odds ratio** (from `fisher.test`), or **Cramér's V**.

---
---

# WEEK 1 — EXPLORING DATA (Descriptive Statistics)

## Why statistics? To separate a real signal from random noise.

## Two kinds of analysis
- **Descriptive** — summarise the data you have (W1).
- **Inferential** — use a sample to conclude about a population (W2+).

## Variable types — the master decision
| Type | What it is | Examples |
|---|---|---|
| **Categorical** | which category | Vegetation, Damp(T/F), diagnosis(M/B) |
| → binary | only 2 categories | TRUE/FALSE |
| **Numerical** | a number | Area, Worm.density, mpg, radius.mean |
| → discrete | whole counts | cylinders (4/6/8) |
| → continuous | any decimal | pH 4.1 |

## Describing CATEGORICAL
- **Frequency table** `table(df$col)` · relative freq = count/total · cumulative = running total.
- Plots: **bar chart** `barplot(table(df$col))`, pie chart.

## Describing NUMERICAL
**Location (centre):**
| Measure | Meaning | Outlier-sensitive? | R |
|---|---|---|---|
| Mean | sum/n | **YES** | `mean(x)` |
| Median | middle when sorted | **NO** | `median(x)` |
| Mode | most frequent | no | — |

Worked `4,7,2,5,6,2` → mean **4.33**, median **4.5**, mode **2**. Skew/outliers → trust median.

**Spread:** Range `range(x)` · IQR `IQR(x)` (middle 50%, robust) · SD `sd(x)` (avg distance from mean, uses n−1) · Variance `var(x)` = SD². `summary(x)` = min/Q1/median/mean/Q3/max.

**Plots:** Histogram `hist(x)` (shape) · Box plot `boxplot(y ~ group)` (median, box=Q1–Q3, whiskers, outliers; great for comparing groups).

---
---

# WEEK 2 — CONFIDENCE INTERVALS (Inferential Part 1)

## Sample → Population
| Term | Meaning |
|---|---|
| Population | whole group (usually unmeasurable) |
| Sample | the subset you measured |
| Parameter | true population value (unknown) |
| Statistic | value from your sample (estimate) |

Every estimate has **uncertainty**. A CI measures it.

## Gumball intuition
One grab of 10 is noisy; 1000 samples form a bell shape centred on the truth; the middle band = a confidence interval.

## What a CI IS
A **range of plausible values** for the true value. Structure: `estimate ± (confidence factor) × (standard error)`.
- ✅ "Repeat the sampling many times, ~95% of such intervals contain the true value."
- ❌ "95% chance the true value is in *this* interval." (Value is fixed; the *procedure* is 95% reliable.)

## Width rules
Bigger sample → narrower. Higher confidence → wider. More variable data → wider.

## The two CIs
- Proportion: `prop.test(490, 1000, conf.level=0.95)` → e.g. (0.46, 0.52).
- Mean: `t.test(x, conf.level=0.95)`.

## Z or t?
n ≥ 30 → Z fine; **n < 30 → t** (fatter tails, wider, honest). `t.test()` always uses t. Rivets (n=12): 95% CI (3.92, 4.36).

## Bootstrapping (optional)
Resample WITH replacement 1000×, take the mean each time, read 2.5th/97.5th percentiles. Distribution-free backup.

## Extension PDF = NOT ASSESSED
Vocab only: `dnorm`=density, `pnorm`=cumulative, `qnorm`=inverse (`qnorm(0.975)=1.96`), `rnorm`=random.

---
---

# WEEK 3 — HYPOTHESIS TESTING (Inferential Part 2)

## The question
W2: "what range is plausible?" **W3: "is this specific claim believable, or a fluke sample?"**

## The two hypotheses (MUST write)
| | Symbol | Meaning |
|---|---|---|
| Null | H₀ | the claim / status quo (trying to disprove) |
| Alternative | H₁ | what you suspect |

Two-sided `H₁: µ ≠ µ₀`; one-sided `µ > µ₀` or `µ < µ₀`.

## p-value — the heart
> p = "if H₀ were TRUE, how likely is a sample this extreme (or more) by chance?"
Small p → sample rare under H₀ → **reject H₀**. Large p → normal under H₀ → **fail to reject**.

## The 4-STEP PROCESS (exam skeleton)
1. State H₀/H₁. 2. Compute test statistic (R). 3. Get p-value (R). 4. Compare to α (0.05): `p ≤ α → reject H₀`.

## Which test (Week 3)
| Question | R | H₀ |
|---|---|---|
| Mean vs claimed (one-sample t) | `t.test(x, mu=v)` | µ = v |
| Proportion vs claimed | `prop.test(s, n, p=v)` | π = v |
| Is data normal? | `shapiro.test(x)` + `qqnorm/qqline` | data normal |
| Equal variances? | `var.test(x,y)` | variances equal |
| Equal means (2 samples)? | `t.test(x,y)` | µ₁ = µ₂ |
| 2 means, non-normal (opt) | `wilcox.test(x,y)` | distributions equal |

- **shapiro:** p < 0.05 → **NOT normal.**
- `t.test(x,y)` auto-uses **Welch** when variances differ.
- `alternative=` : `"two.sided"` (default), `"greater"`, `"less"`.

## Effect size (useful)
p says *whether*; **Cohen's d** says *how big*. `library(effsize); cohen.d(x,y)` → small/medium/large (>0.8). Report both.

## Errors — NOT assessed
Type I (α) = reject true H₀ (false alarm); Type II (β) = keep false H₀ (miss). Power = 1−β.

## Worked
- Heights µ₀=143, x̄=148, s=4.9, n=30 → z=5.6, p≈0.0001 → **reject**.
- Gumball H₀: π=0.5, H₁: π<0.5, p̂=0.42 → p≈0.07 → **don't reject**.
- Gardens `t.test` p=0.0011 → differ; `cohen.d`=−1.73 (large).

---
---

# WEEK 4 — COUNT DATA & TABLE ANALYSIS

## The gap it fills
Real researchers reported antibiotic infection counts (3.6% vs 18.2%) but got rejected — they never **tested** the hypothesis. Having numbers ≠ testing them. None of W1–3 tests fit "are two categorical variables related?"

## Contingency table
Cross two categorical variables into a counts table:
```
            Blue Eyes  Brown Eyes
Fair Hair      38          11
Dark Hair      14          51
```
Question: are hair & eye colour **independent**, or **related**?

## Hypotheses (always the same)
- **H₀: the two variables are INDEPENDENT** (no relationship).
- **H₁: they are NOT independent** (related).

## Observed vs Expected
Expected count if independent: **E = (row total × column total) / grand total**.
Fair hair & blue eyes: E = 49×52/114 = **22.35**, but observed **38** → big gap → maybe related.

## Chi-square test
`χ² = Σ (O − E)² / E`. Big χ² = far from independence.
```r
chisq.test(mytable)                  # default continuity correction
chisq.test(mytable, correct = FALSE) # without it
```
Hair/eye: χ²≈35.3, tiny p → **reject H₀ → hair & eye colour are linked.**
Read p like always: **p < 0.05 → variables ARE related.**

## ⚠️ CRITICAL assumption: all EXPECTED counts ≥ 5
If any expected count < 5 (small sample), χ² is **unreliable**. R still prints a p-value with only a
quiet warning *"approximation may be incorrect."* → **Use Fisher's exact test instead.**
```r
fisher.test(mytable)    # for small samples; also reports an odds ratio
```
Employment example: small counts → Fisher → p=0.38 → **fail to reject → independent.**
Antibiotics table has a count of 1 → use Fisher.

## Effect size for tables
**Odds ratio** (2×2, from `fisher.test`; OR=1 means no association; antibiotics ≈5.8) · **Cramér's V** (0–1, any size table).

## Optional awareness
- **Critical value route:** df=(r−1)(c−1); 2×2 → df=1; `qchisq(0.95,1)=3.84`; χ²=35.3>3.84 → reject.
- **Goodness-of-fit:** does ONE variable match an expected distribution (fair die?). df=k−1.
- **McNemar** (`mcnemar.test`): paired/matched categorical data (before/after same subjects).
- **Multiple testing:** many pairs → false positives; Bonferroni = α / number of tests.
- **Simpson's Paradox:** pooled association can reverse when split by a third variable (Berkeley 1973).
- χ²/Fisher are **non-parametric**; same logic powers A/B tests, epidemiology, genomics, AI fairness audits.

---
---

# 📋 ONE-PAGE R COMMAND REFERENCE

```r
# ---- READ & EXPLORE (W1) ----
df <- read.csv("file.csv"); head(df); summary(df)
table(df$catCol)                 # frequency table
barplot(table(df$catCol))        # bar chart
hist(df$numCol)                  # histogram
boxplot(df$num ~ df$group)       # box plot by group
mean(x); median(x); sd(x); var(x); IQR(x); range(x)

# ---- CONFIDENCE INTERVALS (W2) ----
prop.test(490, 1000, conf.level = 0.95)   # CI for a proportion
t.test(x, conf.level = 0.95)              # CI for a mean
qnorm(0.975)      # 1.96 (Z, 95%)
qt(0.975, df)     # t critical value

# ---- HYPOTHESIS TESTING: means & proportions (W3) ----
t.test(x, mu = 2.0, alternative = "two.sided")        # mean vs claimed
prop.test(43, 50, p = 0.75, alternative = "greater")  # proportion vs claimed
shapiro.test(x)                      # normality (p<0.05 => NOT normal)
qqnorm(x); qqline(x, col="steelblue", lwd=2)
var.test(x, y)                       # equal variances?
t.test(x, y)                         # two-sample means (auto-Welch)
wilcox.test(x, y)                    # non-parametric alt (optional)
library(effsize); cohen.d(x, y)      # effect size for two means

# ---- COUNT DATA / TABLES (W4) ----
mytable <- table(df$var1, df$var2)   # contingency table
chisq.test(mytable)                  # chi-square (expected counts >= 5)
chisq.test(mytable, correct = FALSE) # no continuity correction
fisher.test(mytable)                 # use when any expected count < 5
qchisq(0.95, df)                     # chi-square critical value
mcnemar.test(mytable)                # paired/matched categorical data

# ---- SUBSETTING ----
groupA <- subset(df, df$Species == "setosa")   # case-sensitive!
```

### How to READ any test output (works for every test)
1. Find the **p-value**. 2. Compare to **α = 0.05**.
3. `p ≤ 0.05` → **reject H₀** (there IS an effect / difference / relationship).
4. `p > 0.05` → **fail to reject H₀** (not enough evidence).
5. Note the **CI**: contains the claimed value / 0 / ratio 1 → agrees with "not significant".
6. Where relevant, report an **effect size** (Cohen's d / odds ratio / Cramér's V).


---
---

# 📝 QUIZ REVISION — Worked Answers (Weeks 1–4 practice)

> A set of worked quiz questions with answers + explanations. Great for revision because each one
> drills a decision you'll repeat in the exam: *variable type → right summary/plot → right test → right interpretation.*

### Q1. Visualising diamond weight (grams) — select all
**✅ Histogram + Boxplot.** Weight is **numerical (continuous)** → histogram (shape) and boxplot
(median/quartiles/outliers). Pie chart and bar chart are for **categorical** data. *Variable type decides the plot.*

### Q2. Measure of location for diamond weight — select all
**✅ Mean + Median.** A *measure of location* = the **centre**. SD and IQR are measures of **spread**, not location.

### Q3. Describing a categorical variable (eye colour)
**✅ Tabulating the data** (frequency table). Variance and median need numbers — can't apply them to categories.

### Q4. CI for a proportion (coffee vs tea)
**✅ `prop.test()`.** "Proportion who prefer coffee" = a **proportion**. `t.test()` is for a mean; `summary()` just describes.

### Q5. CI for the mean weight of diamonds
**✅ `t.test()`.** CI for a **mean** → `t.test()`. `prop.test()` is for proportions.

### Q6. "Bigger sample → wider CI" — True/False
**✅ FALSE.** Bigger sample → **narrower** CI (more data = more precision = less uncertainty).

### Q7. Test if pasta packets are *lighter* than 0.5 kg (n = 30 weights)
**✅ `t.test()`.** Testing a **mean**. "Lighter than" = one-sided:
`t.test(weights, mu = 0.5, alternative = "less")`.

### Q8. When to prefer a CI over a hypothesis test
**✅ When you want to estimate a RANGE of plausible values for a parameter.** That's what a CI does;
a hypothesis test instead evaluates a *specific claim*.

### Q9. p-value = 0.03 means...
**✅ "If H₀ is true, there's a 3% probability of observing a result this extreme or more extreme."**
Traps to avoid: it is NOT "3% chance H₀ is true", NOT "97% chance H₁ is true", and says nothing about effect size.

### Q10. Significant p (< 0.001) but tiny effect size (d = 0.05)
**✅ Statistically significant, but may NOT be practically meaningful.** The **big-sample trap**: huge
samples make trivial differences "significant". p and effect size measure different things — that's
exactly why you report **both**.

### 🔑 The two reusable skills these test
1. **Type → tool:** numerical → mean/median/SD + histogram/boxplot + `t.test`; categorical → frequency
   table + bar/pie + `prop.test`/`chisq.test`.
2. **Interpretation:** p-value = "chance of data this extreme IF H₀ true" (not P(H₀ true)); bigger
   sample → narrower CI; significance ≠ practical importance (report effect size).
