# Week 2: Inferential Statistics Part 1 — Full Notes

> **Learning outcomes:** After this you can (1) explain why we need inference (sample ≠ population),
> (2) interpret a confidence interval correctly in English, and (3) compute CIs for proportions
> and means in code.

---

## 1. The big idea: Descriptive → Inferential

**Week 1 question:** "What does this data I have look like?"  
**Week 2 question:** "What does this data tell me about the *larger world* it came from?"

This is the most important shift in the module. You're no longer just describing — you're making a claim about a population you haven't fully observed.

### Population vs. Sample

| Term | Meaning | Example |
|------|---------|---------|
| **Population** | The *entire* group you care about | All 12-year-olds in the UK |
| **Sample** | A smaller subset you actually measured | 10 classes of 12-year-olds in London |
| **Parameter** | The true value in the population (usually unknown) | True mean height of all 12-year-olds |
| **Statistic** | A value computed from your sample (your best guess) | Mean height from your 10 classes |

**The fundamental problem:** you can never measure the whole population. Your sample gives you an *estimate*, and that estimate has *uncertainty*. Statistics tells you how much uncertainty.

---

## 2. The Gumball Machine (the lecture's key intuition)

The lecturer uses a brilliant analogy. Picture a gumball machine:
- It's full of thousands of red and blue sweets — you can't see inside.
- Every coin gives you 10 random sweets.
- You want to know: **what proportion of ALL sweets is red?**

**One sample of 10:** 6 are red → proportion = 0.6. Is this the true proportion? Maybe, maybe not.

**Five samples of 10:** you get proportions 0.3, 0.4, 0.7, 0.5, 0.6. Mean = 0.5. Better, but still uncertain.

**1000 samples of 10:** now you have a *distribution* of sample proportions. It forms a bell shape centred around 0.5. You can now say:
- In 97.5% of samples, the number of reds was between 2 and 8 (proportion 0.2 to 0.8)
- So we're ~97.5% confident the true proportion is between 0.2 and 0.8

**This IS a confidence interval.** That's literally all it is — a range that captures the true value in a specified percentage of repeated samples.

### The key insight
The *more samples you take* (or the *bigger each sample is*), the **narrower** the interval gets → you're more precise.  
The *higher the confidence level* you demand (95% → 99%), the **wider** the interval gets → you need a bigger net to be more sure you've caught the true value.

---

## 3. Confidence Intervals — what they actually mean

### ⚠️ THE correct interpretation (exam-grade wording):
> "If we repeated this sampling process many times and computed a 95% CI each time,
> approximately 95% of those intervals would contain the true population parameter."

### ❌ THE common WRONG interpretation:
> "There is a 95% probability that the true value is in this interval."
> (This is wrong because the true value is fixed — it's either in the interval or it's not.
> The 95% refers to the *procedure*, not to any single interval.)

For practical purposes in this module: think of a 95% CI as "a range of plausible values for the true population parameter."

### The formula structure (don't memorise; understand the pieces)
```
CI = point estimate ± (critical value × standard error)
```
- **Point estimate:** your sample statistic (sample mean x̄, or sample proportion p)
- **Critical value:** how many standard errors wide the interval needs to be for your chosen confidence level (Z=1.96 for 95%, Z=1.645 for 90%)
- **Standard error:** the standard deviation of the *sampling distribution* — basically, how much your estimate would bounce around if you took many samples

---

## 4. Confidence Interval for a PROPORTION

**Scenario:** You surveyed 1000 Londoners and 490 say they'll vote Labour. What's the 95% CI for the true proportion?

**The setup:**
- Sample proportion: p = 490/1000 = 0.49
- Sample size: n = 1000
- Confidence level: 95% → Z = 1.96

**The formula:**
```
p ± Z × sqrt(p(1-p)/n)
= 0.49 ± 1.96 × sqrt(0.49 × 0.51 / 1000)
= 0.49 ± 1.96 × 0.0158
= 0.49 ± 0.031
= (0.459, 0.521)
```

**Interpretation:** "We are 95% confident that the true proportion of London voters who would vote Labour is between approximately 0.46 and 0.52."

### R command
```r
prop.test(490, 1000, conf.level = 0.95)
```
- First argument: number of "successes"
- Second argument: total sample size
- Result includes the CI bounds

### Note: sample size matters
The formula only works well when np > 5 and n(1-p) > 5 (the "large sample" condition). With small samples, use `binom.test()` instead.

---

## 5. Confidence Interval for a MEAN

**Two versions depending on sample size:**

### When n ≥ 30 (use Z — the Normal distribution)
```
CI = x̄ ± Z × (s / √n)
```
- x̄ = sample mean
- s = sample standard deviation
- n = sample size
- Z = 1.96 (for 95%)

### When n < 30 (use t — Student's t-distribution)
```
CI = x̄ ± t × (s / √n)
```
- Same idea, but t > Z (the interval is wider) because with small samples, there's more uncertainty
- t value depends on **degrees of freedom** (df = n - 1) and confidence level
- For 95% CI with n=12: t(0.025, 11) = 2.20

### Why t instead of Z?
- With small samples, our estimate of the standard deviation (s) is itself uncertain
- The t-distribution has **fatter tails** than the normal distribution → wider intervals → more honest about our uncertainty
- As n gets bigger, t approaches Z. By n=30 they're practically identical.

### R command
```r
t.test(data$values, conf.level = 0.95)
```
R's `t.test()` always uses the t-distribution (which is the safe/correct default).

### Worked example: Shearing strength
12 steel rivets measured: 4.01, 4.28, 4.43, 4.04, 3.74, 4.43, 3.89, 4.73, 3.68, 4.55, 4.10, 3.77
- x̄ = 4.1375
- s = 0.344
- n = 12 → use t because n < 30
- t(0.025, 11) = 2.20
- CI = 4.1375 ± 2.20 × (0.344/√12) = 4.1375 ± 0.218 = **(3.92, 4.36)**

**Interpretation:** "We are 95% confident that the true mean shearing strength of this type of rivet is between 3.92 and 4.36 tonnes."

---

## 6. What affects CI width? (important exam question)

| Change | Effect on CI width | Why |
|--------|-------------------|-----|
| **Increase sample size** | **Narrower** ↓ | More data → less uncertainty |
| **Increase confidence level** (90%→95%→99%) | **Wider** ↑ | Need a wider net to be more confident |
| **Larger standard deviation in data** | **Wider** ↑ | More variability → harder to pin down |

This is a common exam/coursework question. Know it cold.

---

## 7. Bootstrapping (optional but useful to understand)

What if your data isn't normally distributed? The t-based CI assumes rough normality.

**Bootstrapping** doesn't assume any distribution:
1. Take your original sample of n values
2. Draw a new sample of n values *with replacement* (some values repeat, some are skipped)
3. Compute the mean of this resample
4. Repeat 1000 times → you now have 1000 bootstrapped means
5. The 2.5th and 97.5th percentiles of those 1000 means = your 95% CI

It's a "let the data speak for itself" approach. The extension PDF calls it a **non-parametric method** (no assumption about the distribution shape). Not assessed directly but good to know.

---

## 8. What to ignore from the Week 2 extension PDF

The extension PDF covers random variables, PMF, PDF, CDF, and formal probability theory. It explicitly says **"not assessed."** 

What's useful from it (just vocabulary):
- **d, p, q, r prefixes** in R: `dnorm` = density, `pnorm` = cumulative probability, `qnorm` = quantile (inverse CDF), `rnorm` = random sample. You'll use `qnorm(0.975)` = 1.96 and `qt(0.975, df)` for finding critical values.
- The Binomial distribution models count-of-successes (like red gumballs). The Normal distribution is the bell curve. The t-distribution is a fatter-tailed bell curve for small samples.

Everything else in that PDF — skip it.

---

## 9. Key takeaways — Week 2 cheat sheet

1. **Sample ≠ Population.** Every sample statistic is an estimate with uncertainty.
2. **Confidence Interval = point estimate ± (critical value × standard error)**
3. **For proportions:** use `prop.test(successes, total, conf.level)`
4. **For means:** use `t.test(data, conf.level)` — R handles t vs Z for you
5. **95% CI means:** if you repeated the procedure many times, 95% of intervals would contain the true value
6. **Bigger sample → narrower CI.** Higher confidence → wider CI.
7. **n < 30 → use t.** n ≥ 30 → Z is fine, but t.test() works always.

---

## Lab: see `labs/week2_lab.py`
