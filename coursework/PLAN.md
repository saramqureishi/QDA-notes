# CS5801 Coursework Plan (SID 2605197)

Deadline: 4 Jan 2027, 11:00 (WiseFlow). Aim to finish by ~14 Dec (Brunel closes 14 Dec to 1 Jan).

## The big picture
You have a gym-member dataset (240 rows after subsetting). Two questions:
1. What drives `monthly_spend` (a number)? -> linear regression
2. What drives `cancelled` (Yes/No)? -> logistic regression

Before modelling, clean the data and explore it.

## Two files, two jobs
- **Supporting.Rmd** = your workbench. All code, all experiments. Not marked, but must run and back up your claims.
- **Submission.Rmd** = your report. The only file marked. Short, specific, 1600 words max.

Workflow: do the work in supporting -> copy the best bits of code into submission -> write the explanations.

## Steps
| # | Stage | Do in supporting | Write in submission | Needs (course week) |
|---|---|---|---|---|
| 0 | Setup: install R packages, run the subset code | yes | 1.1 (code only, 5 marks) | now |
| 1 | Data quality: find problems | 1.A-1.D chunks (done, to run) | 1.2 plan (150w), 1.3 three issues (250w) | now |
| 2 | Cleaning: fix the 3 issues | cleaning chunks | 1.4 (200w) | now |
| 3 | EDA: plots and tables for both outcomes | many plots | pick best 3 + explain (250w) | Wk 1 |
| 4 | Model monthly_spend (linear regression) | start model, try others, compare, check diagnostics | 3.1 (250w), 3.2 (150w) | Wk 5 and 8 |
| 5 | Model cancelled (logistic regression, use step()) | same | 4 (350w) | Wk 9 |
| 6 | Polish: word count, typos, AI disclosure, rename files, run both end to end | | | |

## Watch-outs
- Do not use `membership_status` to predict `cancelled`: suspended = cancelled in all 50 cases (data leakage).
- Every section is specific to YOUR data. No textbook definitions.
- Disclose AI use (name the tool). Write text in your own words.
- Do not put install.packages() in either file.
- Rename files before submitting: 2605197-submission-26-27.Rmd and 2605197-supporting-26-27.Rmd.
