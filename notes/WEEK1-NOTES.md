# Week 1: Exploring Data — Full Notes

> **Learning outcomes:** After this you can (1) classify variables as categorical or numerical,
> (2) pick the right summary (number or graph) for each type, and (3) do it in code.

---

## 1. Why statistics at all?

Not a philosophical question — a practical one. The lecturer uses a great example:

> How does AI recognise cats? It measures features (ear distance, body width/height ratio),
> builds a distribution of "normal" measurements from thousands of examples, and flags
> anything that falls outside that distribution. The maths behind that? Mean, standard
> deviation, probability distributions — all statistics.

Even LLMs (ChatGPT, Claude) predict the *next word* by computing a probability distribution
over all possible words. Statistics is the engine under AI. That's the motivation.

---

## 2. Two types of analysis (know the names)

| Type | What it does | This module |
|------|--------------|-------------|
| **Descriptive** | Describes the data you actually have. Summaries + plots. | **Week 1** (today) |
| **Inferential** | Uses a *sample* to say something about the larger *population*. | Weeks 2 onwards |

Week 1 is 100% descriptive. We are NOT making claims about the world yet — just looking at what's in front of us.

---

## 3. The ONE decision that controls everything: Variable Type

### Categorical variables
Record *which category* an observation belongs to.  
- Examples: `Vegetation` (Grassland, Arable, …), `Damp` (TRUE/FALSE), `car name`
- When there are only 2 categories → **binary** (like Damp: TRUE/FALSE)
- **Trick:** a column might look like numbers but actually be categorical. The `group` column with values 1 and 2 could be categorical (two treatment groups), not "the number one and the number two." ALWAYS check the context/metadata.

### Numerical (continuous) variables
Take actual numeric values you can do arithmetic on.  
- Examples: `Area` (3.6, 5.1, …), `Worm.density` (4, 7, 2, …), `mpg`, `weight`
- Can be discrete (integer-only, like cylinders: 4, 6, 8) or continuous (any decimal)

### Why this matters
| Decision point | If CATEGORICAL → | If NUMERICAL → |
|----------------|-------------------|----------------|
| Numerical summary | Frequency table (counts) | Mean, median, mode, SD, IQR, range |
| Graph | Bar chart or pie chart | Histogram or box plot |
| Inference (later) | Chi-square, proportions | t-test, confidence intervals, regression |

**If you classify a variable wrong, every subsequent choice is wrong.** This is genuinely the #1 skill in the module.

---

## 4. Describing CATEGORICAL variables

### Frequency table
Just count how many times each category appears.

| Vegetation | Frequency | Cumulative Frequency |
|-----------|-----------|---------------------|
| Arable | 3 | 3 |
| Grassland | 9 | 12 |
| Meadow | 3 | 15 |
| Orchard | 1 | 16 |
| Scrub | 4 | 20 |

- **Relative frequency** = frequency / total (gives proportions that sum to 1)
- **Cumulative frequency** = running total down the column

### Graphs for categorical: Bar chart and Pie chart
- **Bar chart:** x-axis = categories, y-axis = frequency. The gaps between bars matter — they signal these are distinct categories, not a continuous range.
- **Pie chart:** each slice proportional to frequency. Fine for a quick look; harder to compare precisely than a bar chart.

### R command (for reference)
```r
table(worms$Vegetation)           # frequency table
barplot(table(worms$Vegetation))  # bar chart
```

---

## 5. Describing NUMERICAL variables

### Measures of Location (= "where is the center?")

| Measure | What it is | Formula / Idea | Sensitive to outliers? |
|---------|-----------|----------------|----------------------|
| **Mean** | Arithmetic average | x̄ = sum / n | **YES** — one extreme value pulls it |
| **Median** | Middle value when sorted | Sort, pick the middle (or average of two middles) | **NO** — robust to extremes |
| **Mode** | Most frequent value | Just count | NO |

**When to use which:** If data is skewed or has outliers, the median is a safer summary than the mean. If the data is roughly symmetric, they'll be close to each other anyway.

#### Worked example (from the pre-reads)
Data: `4, 7, 2, 5, 6, 2`
- **Mode** = 2 (appears twice, everything else once)
- **Mean** = (4+7+2+5+6+2)/6 = 26/6 = **4.333**
- **Median** = sort → 2, 2, 4, 5, 6, 7 → middle two are 4 and 5 → (4+5)/2 = **4.5**

### Measures of Spread (= "how spread out is the data?")

| Measure | What it is | When useful |
|---------|-----------|-------------|
| **Range** | max − min | Quick look, but one outlier ruins it |
| **IQR** | 75th percentile − 25th percentile | Spread of the middle 50%; robust to outliers |
| **Standard Deviation (SD)** | Average distance from the mean | The most used measure; paired with the mean |
| **Variance** | SD² | Mathematically convenient, less interpretable |

#### The SD formula (sample version — this is what R/Python compute by default)
```
s = sqrt( sum((xi - x̄)²) / (n-1) )
```
- Why *n-1* and not *n*? Because we estimated the mean from the same data. Using n-1 (called **Bessel's correction**) prevents the spread being underestimated. The population version uses n.
- **Don't memorise the formula. Understand:** SD = "on average, how far are values from the mean?" Small SD = tightly clustered; large SD = widely spread.

#### Worked example
Data: `4, 7, 2, 5, 6, 2`, mean = 4.333
Squared deviations: 0.111 + 7.111 + 5.444 + 0.444 + 2.778 + 5.444 = 21.333
- **Sample variance** = 21.333/5 = 4.267 → **Sample SD** = √4.267 = **2.066**
- Population variance = 21.333/6 = 3.556 → Population SD = 1.886

R's `sd()` and `var()` give the sample version (2.066 and 4.267).

### Percentiles and IQR
- **k-th percentile** = the value below which k% of the data falls
- **25th percentile (Q1)** and **75th percentile (Q3)** are the most common
- **IQR = Q3 − Q1** = the spread of the middle half of the data

For the data `2, 2, 4, 5, 6, 7`:
- Q1 (25th percentile) = 2.5
- Q3 (75th percentile) = 5.75
- IQR = 5.75 − 2.5 = 3.25

### The `summary()` shortcut
In R: `summary(data_vector)` gives you min, Q1, median, mean, Q3, max — everything you need in one line.

### Graphs for numerical: Histogram and Box plot

**Histogram:**
- Splits the range into bins, counts how many values fall in each
- Shows the *shape* (symmetric? skewed? bimodal?)
- The `breaks` parameter controls how many bins — experiment with it

**Box plot (box-and-whisker):**
- The box = Q1 to Q3 (middle 50%)
- The line inside = median
- The whiskers extend to min/max (or 1.5×IQR from the box edges; points beyond are outliers)
- Great for **comparing** a numerical variable across categories (e.g., Worm density for Damp=TRUE vs FALSE)

### R commands (for reference)
```r
mean(x); median(x); sd(x); var(x); IQR(x); range(x)
summary(x)
hist(x)
boxplot(y ~ group)
```

---

## 6. Worms dataset walkthrough (the lab data)

The `worms.csv` dataset is from Crawley's textbook. It has 20 rows of garden field data.

**Variable classification exercise:**
| Column | Type | Reason |
|--------|------|--------|
| Field.Name | Categorical | Names/labels |
| Area | Numerical (continuous) | Field area in hectares |
| Slope | Numerical (could be discrete) | Slope in degrees |
| Vegetation | Categorical | Type of vegetation (5 levels) |
| Soil.pH | Numerical (continuous) | pH measurement |
| Damp | Categorical (binary) | TRUE/FALSE |
| Worm.density | Numerical (discrete) | Count of worms per unit |

This classification drives *every choice* you make in the lab.

---

## 7. Key takeaways — Week 1 cheat sheet

1. **Categorical → frequency table + bar chart / pie chart**
2. **Numerical → mean, median, SD, IQR + histogram / box plot**
3. **Always check the data type before choosing a technique** — numbers can be categorical
4. **Mean is sensitive to outliers; median is not** — report both when in doubt
5. **SD tells you how spread out the data is** — bigger SD = more spread
6. `summary()` in R is your best friend for a first look

---

## Lab: see `labs/week1_lab.py`
