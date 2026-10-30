# CS5701 Quantitative Data Analysis (QDA) — Your Study Guide

> A plain-English map of the whole module, what matters, what to ignore,
> and how you'll be assessed. Read this once before anything else.

---

## 1. What this module actually is

QDA = **using statistics to tell the difference between a real signal and random noise.**

That's the whole thing. Every technique in the course answers one of three questions:

1. **What does this one variable look like?** (describe it) — Week 1
2. **What can a sample tell me about the whole population it came from?** (infer it) — Weeks 2–4
3. **How do variables relate to / predict each other?** (model it) — Weeks 5–11

The quote the lecturer opens with sums up the philosophy:
> "The numbers have no way of speaking for themselves. We speak for them. We imbue them with meaning." — Nate Silver

The tool is **R / RStudio** (we're using Python here as a stand-in to learn the *concepts* — the ideas are identical; only the syntax differs).

---

## 2. The module in one table (week by week)

| Week | Topic | One-line meaning |
|------|-------|------------------|
| 1 | Exploring Data | Describe one variable: types, summaries, plots |
| 2 | Inferential Statistics Part 1 | Confidence intervals: how sure are we about a sample estimate? |
| 3 | Inferential Statistics Part 2 | Hypothesis testing: is this difference real? |
| 4 | Count Data & Table Analysis | Chi-square, contingency tables |
| 5 | Linear Regression | Predict a number from another number |
| 6 | **READING WEEK** | (no new material) |
| 7 | ANOVA | Compare means across 3+ groups |
| 8 | Multiple Regression | Predict from several variables at once |
| 9 | GLM & Logistic Regression | Predict a yes/no outcome |
| 10 | QDA in the wild | Real applications |
| 11 | Revision | Exam prep |

Notice the staircase: **describe → infer → model.** Each week stands on the one before. If Week 1–3 are solid, the rest is variations on a theme.

---

## 3. Assessment — how you're graded

This is important and often misunderstood:

- QDA (CS5701) is a **teaching block**. It is assessed **jointly** with CS5702 (Modern Data) through two shared assessment blocks:
  - **Coursework** (coded CS5801)
  - **Exam** (coded CS5802)
- Both assessments cover **CS5701 + CS5702 material combined.**
- **The weekly labs and worksheets are NOT marked.** They say this repeatedly. They are practice. ("QDA is not a spectator sport.")

**What this means for you strategically:** the labs are where you *actually learn the thing that gets examined.* Nobody grades them, so most people half-do them — and that is exactly the gap you can exploit (see the "70%" exercise below).

**Textbook:** Crawley, M.J. (2015) *Statistics: An Introduction Using R*, Wiley. Available free as a digital download via the university library. This is THE reference — page numbers are cited throughout the labs.

---

## 4. Your teacher's answer: first / ignore / the one exercise

You asked me, as someone with limited time, for three things. Here they are, specific to QDA:

### (a) What to learn FIRST (the load-bearing 20%)
1. **Variable types** — categorical vs numerical. *Everything* downstream (which plot, which test, which model) is decided by this one classification. Get it wrong and every later step is wrong.
2. **The sample → population leap.** Understand *why* we never have the whole population, only a sample, and that every number we compute from a sample is a guess with uncertainty attached. This single idea is the soul of Weeks 2–11.
3. **Reading a confidence interval in words.** If you can correctly say out loud what "95% CI = [0.46, 0.52]" means, you understand inference. Most students can compute it but cannot say what it means.

### (b) What to IGNORE completely (for now / for passing)
- **Memorising formulas.** You will never hand-derive the t-interval formula in a way that matters. R/Python compute it. Understand *what goes in and what comes out*, not the algebra.
- **The Week 2 "Extension" PDF** (random variables, PMF/PDF/CDF measure-theory definitions, the integral notation). The document itself says **"not assessed."** Skim it once for vocabulary; do not study it.
- **Proofs and the formal definition** `P(A(X) ≤ θ ≤ B(X)) = 1−α`. Know it exists; don't lose a minute memorising it.
- Manual percentile interpolation by hand. Know the *idea* (it splits the data); let the computer do the arithmetic.

### (c) The ONE exercise that puts you ahead of 70%
> **Take ONE real dataset you've never seen, and in a single clean document go
> end-to-end: classify every column by type → make the correct summary and the
> correct plot for each → pick one numerical variable and compute + interpret
> its 95% confidence interval in a full English sentence → change the confidence
> level and explain why the interval width changed.**

Why this beats months of passive study: it forces you to make the *type decision*, the *tool decision*, and the *interpretation* in one connected chain. That chain — not any single fact — is what the coursework and exam test. Most students who've "studied for months" can define a confidence interval but freeze when handed a raw CSV and asked "so what?". Do this once, honestly, and you've done the thing the module is actually about. (The `auto-mpg` lab below is exactly this exercise — do it for real, don't just read it.)

---

## 5. How to use these notes

- `WEEK1-NOTES.md` and `WEEK2-NOTES.md` — the explained lessons.
- `labs/` — runnable code for every lab. Run them, read the output, change a number, re-run. That's the loop.
- Each week you share, I'll add a new `WEEKn-NOTES.md` and the matching labs.

A note on tooling: the course uses **R**. This sandbox doesn't have R, so the labs here are written in **Python** (pandas/scipy/matplotlib). Every concept maps 1:1. I give you the **R command alongside the Python** in the notes so you're never lost in a real lab. The statistics are identical.
