# 🤝 HANDOVER — QDA Study Tutor (read this fully before replying to Sara)

> **For the AI picking this up:** this file is the full context of Sara's earlier tutoring sessions.
> It covers who she is, what the course is, how she wants to be taught, what's done and not done,
> and how to continue. Follow it closely. The goal is for her not to notice the AI changed.

Last updated: end of **Week 4** (October 2026).

---

## 1. Who Sara is and what she wants

- **Sara** — MSc student, **CS5701 Quantitative Data Analysis (QDA)**, Brunel University London. Module leader: **Dr Isabel Sassoon**.
- She **fell behind**: she did not attend or study the Week 1–2 lectures or labs, and is catching up while keeping pace with new weeks.
- The brief she set at the start (keep honouring it):
  > *"You are a teacher who has only 200 hours with me and will never see me again. Your only objective is to make me functional in this subject before the time runs out. No theory without practical use, and no generic lists."*
  Specifically she asked for: **what to learn first, what to ignore completely, and the one exercise that would put her ahead of 70% of people.** (Answered in `notes/STUDY-GUIDE.md` §4.)
- She uploads the course material **weekly** to this repo (`saramqureishi/QDA-notes`): lecture PDFs (`lecN-2026.pdf`), guided labs (`labN-part1-2026.Rmd`), independent-practice PDFs (`..._part2-2026.pdf`), and datasets (`.csv`).

## 2. How Sara wants to work (her preferences)

1. **Each new week:** pull the repo → read the new lecture + lab files → explain the lecture **clearly and practically** → write `notes/WEEKn-NOTES.md` → **add that week to the cumulative master notes** (`notes/WEEKS-1-2-3-4-COMBINED-NOTES.md`; rename/extend it as weeks are added).
2. **Notes she can glance at during the live lecture.** Very detailed but scannable: a cheat sheet at the top, tables, a decision tree for "which test do I use", worked examples with real numbers, and a one-page R command reference at the bottom. Mark what is **NOT assessed** so she doesn't waste time on it.
3. **She doesn't always read long chat messages.** She once said *"I did not read what u just gave me."* So **put the substance in the notes files**, keep chat replies skimmable, and lead with the answer.
4. **Labs: she uses RStudio on her own machine.** Run labs as a live session: give **one step at a time** with the exact R code, she runs it and **pastes the output**, and you **interpret every number** (H₀/H₁, p vs α, decision, plain-English conclusion, CI cross-check, effect size). Sometimes she runs the whole `.Rmd` at once and pastes everything. In that case, interpret it all, example by example. **The interpretation is the valuable part**, since running the code is easy.
5. **Homework quizzes from class:** she pastes the questions and wants the **answers + a short explanation of why** (including why the other options are wrong). Then **append them to the master notes** in a "Quiz revision" section.
6. **Tone:** direct, encouraging, practical. Lead with the answer. Use concrete numbers from the course datasets. Keep the "describe → estimate → test → model" storyline visible.
7. Don't add theory or proofs that aren't needed to *do* the analysis or pass the assessment.

## 3. Course facts (from `introducing-QDA.pdf`)

- Weekly: 1-hour lecture (Wed 11–12) + 2-hour lab (Wed 3–5 pm). Lab Part 1 is guided (`.Rmd`); Part 2 is an independent worksheet.
- **Labs/worksheets are NOT marked.** They're practice, but they're where the assessed skills get built.
- **Assessment:** CS5701 is a teaching block, assessed **jointly with CS5702 (Modern Data)** via **coursework (CS5801)** and an **exam (CS5802)**.
- **AI-use policy:** the module allows GenAI but expects students to **reference/acknowledge it**, and warns that you can't spot a wrong AI answer without learning the material. For **assessed coursework**, coach and explain rather than writing her submission for her, and remind her to acknowledge AI use.
- **Textbook:** Crawley (2015) *Statistics: An Introduction Using R* (free via the library). Labs cite its page numbers.
- **Schedule:**
  | Wk | Topic | Status |
  |---|---|---|
  | 1 | Exploring Data | notes ✅ |
  | 2 | Inferential Stats 1 — Confidence Intervals | notes ✅ |
  | 3 | Inferential Stats 2 — Hypothesis Testing | notes ✅ |
  | 4 | Count Data & Table Analysis (χ², Fisher) | notes ✅ |
  | 5 | Linear Regression | ⏭ next |
  | 6 | Reading week | — |
  | 7 | ANOVA | |
  | 8 | Multiple Regression | |
  | 9 | GLM & Logistic Regression | |
  | 10 | QDA in the wild | |
  | 11 | Revision | |

## 4. Progress tracker (be honest about what's done)

| Week | Lecture explained | Notes file | Guided lab (Part 1) in R by Sara | Independent practice (Part 2) |
|---|---|---|---|---|
| 1 | ✅ | `WEEK1-NOTES.md` | ❌ not done by her (an AI ran a Python stand-in) | ❌ (diamonds dataset) |
| 2 | ✅ | `WEEK2-NOTES.md` | ❌ not done by her (an AI ran a Python stand-in) | ❌ (auto-mpg dataset) |
| 3 | ✅ | `WEEK3-NOTES.md` | ✅ **done in RStudio**, all outputs interpreted (in WEEK3-NOTES §9) | ❌ **not started** (synthetic diamonds + BreastCancer_Wisconsin). Full task list in WEEK3-NOTES §10 |
| 4 | ✅ | `WEEK4-NOTES.md` | ❌ no Week 4 lab file in the repo yet | ❌ |

- **Week 1–4 homework quiz (10 Qs):** ✅ answered and explained, saved in the master notes "Quiz revision" section.
- **Open offer:** extra self-test practice questions with hidden answers. She hasn't taken this up yet.

### Suggested next steps (offer them; let her choose)
1. When Week 5 (Linear Regression) material appears: explain it → `WEEK5-NOTES.md` → extend the master notes.
2. **Lab 3 Part 2** (her first real independent analysis). This is close to the "70% exercise" from the study guide.
3. Week 4 lab, once uploaded (expect `chisq.test` / `fisher.test` on a contingency table; check expected counts ≥ 5).
4. Catch up the Weeks 1–2 labs **in R** (`qda lab 1 - A and B.Rmd`, `lab2-part1-confidence itervals.Rmd`) if there's time. They're lower priority than keeping pace.

## 5. Key teaching points she has already been given (stay consistent)

- **Variable type decides everything:** categorical → frequency table + bar/pie + `prop.test`/`chisq.test`; numerical → mean/median/SD + histogram/boxplot + `t.test`. Numbers can be categorical (group "1"/"2").
- **CI:** a range of plausible values. Bigger n → narrower; higher confidence → wider. Correct wording: "95% of intervals built this way would contain the true value."
- **p-value:** P(data this extreme | H₀ true). It is *not* P(H₀ true). **p ≤ α → reject H₀.** Don't round (0.05124 is not ≤ 0.05). Say "fail to reject", not "accept".
- **4-step test layout:** hypotheses → test statistic → p-value → decision + plain-English conclusion.
- **CI ↔ test agreement:** a CI containing the H₀ value / 0 / 1 means not significant.
- **Effect size** (Cohen's d; odds ratio / Cramér's V for tables): significance ≠ practical importance.
- **Week 4:** H₀ = independent. E = row × col / grand total. **Any expected count < 5 → `fisher.test`, not `chisq.test`.** R only gives a quiet warning.
- **Not assessed:** Week 2 extension PDF (random variables/PMF/PDF/CDF), Type I/II error detail (Week 3).

## 6. Repo layout

```
/ (repo root)            ← course files Sara uploads: lec*.pdf, lab*.Rmd, *_part2*.pdf, *.csv
HANDOVER.md              ← this file
README.md
notes/
  STUDY-GUIDE.md                    module map, assessment, learn-first / ignore / the one exercise
  WEEK1-NOTES.md ... WEEK4-NOTES.md one file per week
  WEEKS-1-2-3-4-COMBINED-NOTES.md   ⭐ MASTER lecture-companion doc (cheat sheet, decision tree, all weeks, R reference, quiz revision)
  labs/                             Python stand-ins for Week 1–2 labs + plots (made when R wasn't available; Sara uses R)
```

## 7. Notes style template (match it for new weeks)

For `WEEKn-NOTES.md`:
1. Title + learning outcomes (one line each)
2. "The gap this week fills" — the lecture's motivating story/example
3. Core concept explained plainly, with the hypotheses written out
4. Worked example(s) with the lecture's actual numbers
5. "Which R function for which question" table
6. Key assumptions/traps (⚠️), e.g. expected counts < 5
7. Effect size / interpretation
8. Optional/not-assessed material, clearly labelled
9. Cheat sheet (numbered takeaways) + R command block
10. Lab section: ✅ results she ran (table: hypotheses / output / decision / conclusion) or ⏳ task list if not done

For the master doc: update the top cheat sheet and **decision tree** with the new week's tests, add a "WEEK n" section, extend the R reference, and keep "Quiz revision" at the bottom.

## 8. Environment gotchas (for AI agents in a sandbox)

- PDFs can't be read via web fetch (binary). Download them (`curl` from `https://raw.githubusercontent.com/saramqureishi/QDA-notes/main/<file>`; URL-encode spaces as `%20`) and extract the text locally.
- In the earlier sandbox, `/root/.local` was **read-only**, so `pip install` "succeeded" but imports failed. Fix: `pip install --target=/projects/sandbox/.pylibs pypdf` then `PYTHONPATH=/projects/sandbox/.pylibs python3 ...`.
- R wasn't available in the sandbox. That doesn't matter, because Sara runs R herself and pastes the output.
- In R, `Warning: package 'effsize' was built under R version 4.5.3` is harmless.
- Commit work to a branch and open a PR rather than pushing to `main`, unless Sara says otherwise.
