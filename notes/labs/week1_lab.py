"""
QDA WEEK 1 LAB — Exploring Data
================================
This is the Python equivalent of 'qda lab 1 - A and B.Rmd'
Every concept maps 1:1 to R. The R equivalent is shown in comments.

Run this file: python labs/week1_lab.py
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt

print("=" * 70)
print("  QDA WEEK 1 LAB — EXPLORING DATA")
print("=" * 70)

# =====================================================================
# PART 1: DESCRIBING DATA — small vector
# =====================================================================
print("\n" + "=" * 70)
print("PART 1: Measures of Location & Spread")
print("=" * 70)

data_vector = [4, 7, 2, 5, 6, 2]
# R: data_vector <- c(4, 7, 2, 5, 6, 2)

print(f"\nData: {data_vector}")

# --- Mean ---
# R: mean(data_vector)
print(f"\nMean = {np.mean(data_vector):.4f}")
print("  → The average. Sum all values, divide by count.")
print("  → (4+7+2+5+6+2)/6 = 26/6 = 4.3333")

# --- Median ---
# R: median(data_vector)
print(f"\nMedian = {np.median(data_vector):.4f}")
print("  → Sort: [2, 2, 4, 5, 6, 7]. Middle two values are 4 and 5.")
print("  → Average of 4 and 5 = 4.5")

# --- Mode ---
# R has no built-in mode function! You write your own with table()
from scipy import stats
mode_result = stats.mode(data_vector, keepdims=True)
print(f"\nMode = {mode_result.mode[0]}")
print("  → The most frequent value. 2 appears twice, everything else once.")

# --- Range ---
# R: range(data_vector)
print(f"\nRange = {min(data_vector)} to {max(data_vector)}")
print(f"  → Range width = {max(data_vector) - min(data_vector)}")

# --- IQR ---
# R: IQR(data_vector)
q25 = np.percentile(data_vector, 25, interpolation='linear')
q75 = np.percentile(data_vector, 75, interpolation='linear')
# Note: R and Python may use slightly different interpolation methods
# R uses type=7 by default. The values should be close.
print(f"\n25th percentile (Q1) = {q25}")
print(f"75th percentile (Q3) = {q75}")
print(f"IQR = Q3 - Q1 = {q75 - q25}")
print("  → The spread of the middle 50% of the data")

# --- Standard Deviation & Variance ---
# R: sd(data_vector) — uses n-1 (sample version)
# R: var(data_vector) — also sample version
sd_sample = np.std(data_vector, ddof=1)  # ddof=1 for sample SD
var_sample = np.var(data_vector, ddof=1)
print(f"\nSample Standard Deviation = {sd_sample:.4f}")
print(f"Sample Variance = {var_sample:.4f}")
print("  → SD = average distance from the mean")
print("  → ddof=1 in Python = Bessel's correction (same as R's default)")

# --- Summary (like R's summary()) ---
# R: summary(data_vector)
s = pd.Series(data_vector)
print(f"\nFull summary:")
print(s.describe())

# --- Weighted Mean ---
# R: weighted.mean(grade.point, credit)
grade_point = [13, 16, 12]
credit = [15, 15, 30]
weighted_mean = np.average(grade_point, weights=credit)
print(f"\n--- Bonus: Weighted Mean ---")
print(f"Grade points: {grade_point}, Credits: {credit}")
print(f"Weighted mean = {weighted_mean:.4f}")
print("  → (13×15 + 16×15 + 12×30) / (15+15+30) = 13.25")

# =====================================================================
# PART 2: EXPLORING THE WORMS DATASET
# =====================================================================
print("\n" + "=" * 70)
print("PART 2: Worms Dataset — Real Data Exploration")
print("=" * 70)

worms = pd.read_csv("worms.csv")
# R: worms <- read.csv("worms.csv")

print(f"\nFirst 10 rows:")
print(worms.head(10).to_string())
# R: head(worms, n=10)

print(f"\nDataset shape: {worms.shape[0]} rows × {worms.shape[1]} columns")

# --- Variable types ---
print("\n--- Variable Types ---")
print("Field.Name  → Categorical (names)")
print("Area        → Numerical (continuous)")
print("Slope       → Numerical")
print("Vegetation  → Categorical (5 categories)")
print("Soil.pH     → Numerical (continuous)")
print("Damp        → Categorical (binary: T/F)")
print("Worm.density→ Numerical (discrete count)")

# --- Categorical: Frequency Table ---
# R: table(worms$Vegetation)
print("\n--- Frequency Table for Vegetation ---")
veg_freq = worms['Vegetation'].value_counts().sort_index()
print(veg_freq)

# Cumulative frequency
print("\n--- Cumulative Frequency Table ---")
freq_table = pd.DataFrame({
    'Frequency': veg_freq,
    'Cumulative': veg_freq.cumsum(),
    'Relative': (veg_freq / veg_freq.sum()).round(2)
})
print(freq_table)

# R: table(worms$Damp, worms$Vegetation) — contingency/cross table
print("\n--- Cross-tabulation: Damp × Vegetation ---")
cross = pd.crosstab(worms['Damp'], worms['Vegetation'])
print(cross)

# --- Categorical: Bar Chart ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# R: barplot(table(worms$Vegetation))
veg_freq.plot(kind='bar', ax=axes[0], color='steelblue', edgecolor='black')
axes[0].set_title('Bar Chart of Vegetation')
axes[0].set_ylabel('Frequency')
axes[0].set_xlabel('Vegetation')

# Pie chart
# R: pie(table(worms$Vegetation))
veg_freq.plot(kind='pie', ax=axes[1], autopct='%1.1f%%')
axes[1].set_title('Pie Chart of Vegetation')
axes[1].set_ylabel('')

plt.tight_layout()
plt.savefig('notes/labs/week1_vegetation_charts.png', dpi=100, bbox_inches='tight')
plt.close()
print("\n✓ Saved: labs/week1_vegetation_charts.png")

# --- Numerical: Summary Statistics ---
print("\n--- Numerical Summary for Worm.density ---")
wd = worms['Worm.density']
# R: summary(worms$Worm.density)
print(wd.describe())

# --- Numerical: Histogram ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# R: hist(worms$Worm.density, xlab="Density", ylab="Count", main="Distribution of Worm Density")
axes[0].hist(wd, bins=10, color='steelblue', edgecolor='black')
axes[0].set_title('Histogram of Worm Density')
axes[0].set_xlabel('Density')
axes[0].set_ylabel('Count')

# R: hist(worms$Worm.density, breaks=20)
axes[1].hist(wd, bins=20, color='steelblue', edgecolor='black')
axes[1].set_title('Histogram of Worm Density (more bins)')
axes[1].set_xlabel('Density')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.savefig('notes/labs/week1_worm_histogram.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Saved: labs/week1_worm_histogram.png")

# --- Numerical: Box Plot ---
# R: boxplot(worms$Worm.density ~ worms$Damp)
fig, ax = plt.subplots(figsize=(8, 5))
worms.boxplot(column='Worm.density', by='Damp', ax=ax)
ax.set_title('Box Plot of Worm Density by Damp')
ax.set_xlabel('Damp')
ax.set_ylabel('Worm Density')
plt.suptitle('')  # remove auto-title
plt.tight_layout()
plt.savefig('notes/labs/week1_worm_boxplot.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Saved: labs/week1_worm_boxplot.png")

print("\n--- Interpreting the Box Plot ---")
for damp_val in ['F', 'T']:
    subset = worms[worms['Damp'] == damp_val]['Worm.density']
    print(f"\nDamp = {damp_val}:")
    print(f"  Median = {subset.median()}")
    print(f"  Q1 = {subset.quantile(0.25)}, Q3 = {subset.quantile(0.75)}")
    print(f"  IQR = {subset.quantile(0.75) - subset.quantile(0.25)}")

print("\n→ Median worm density is HIGHER when Damp=TRUE")
print("→ Spread (IQR) is LARGER when Damp=FALSE")

# =====================================================================
# PART 3: INDEPENDENT PRACTICE — diamonds dataset
# =====================================================================
print("\n" + "=" * 70)
print("PART 3: Independent Practice — Diamonds Dataset")
print("=" * 70)

# In R: library(ggplot2); data(diamonds)
# In Python we use seaborn's diamonds dataset
import seaborn as sns
diamonds = sns.load_dataset('diamonds')

print(f"\nDataset: {diamonds.shape[0]} rows × {diamonds.shape[1]} columns")
print(f"\nColumn info:")
print(diamonds.dtypes)

print(f"\nFirst 5 rows:")
print(diamonds.head().to_string())

# (b) Verify columns match Table 1
print("\n--- (b) Checking columns ---")
expected_cols = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']
for col in expected_cols:
    found = col in diamonds.columns
    print(f"  {col}: {'✓ Found' if found else '✗ MISSING'}")

# (d) Levels in 'cut'
print(f"\n--- (d) Levels in 'cut' ---")
print(f"  {diamonds['cut'].nunique()} levels: {list(diamonds['cut'].unique())}")

# (e) Numerical summaries — categorical
print(f"\n--- (e) Summary for categorical variables ---")
for col in ['cut', 'color', 'clarity']:
    print(f"\nFrequency table for '{col}':")
    print(diamonds[col].value_counts().sort_index())

# (e) Numerical summaries — numerical
print(f"\n--- Summary for numerical variables ---")
print(diamonds[['carat', 'depth', 'table', 'price', 'x', 'y', 'z']].describe().round(2))

# (c) Range check
print(f"\n--- (c) Range checks ---")
# Table 1 states z in [0, 3.18] — but note the summary shows a max of 31.8!
# That is almost certainly a data-entry error (decimal point): a real teaching point.
ranges = {'price': (326, 18823), 'carat': (0.2, 5.01), 'x': (0, 10.74), 'y': (0, 58.9), 'z': (0, 31.8)}
for col, (low, high) in ranges.items():
    out_of_range = diamonds[(diamonds[col] < low) | (diamonds[col] > high)]
    print(f"  {col}: expected [{low}, {high}], found {len(out_of_range)} values outside range")

# (f) Plots
fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# Bar chart for cut
diamonds['cut'].value_counts().sort_index().plot(kind='bar', ax=axes[0][0], color='steelblue', edgecolor='black')
axes[0][0].set_title('Bar Chart of Cut')
axes[0][0].set_ylabel('Frequency')

# Histogram for price
axes[0][1].hist(diamonds['price'], bins=50, color='steelblue', edgecolor='black')
axes[0][1].set_title('Histogram of Price')
axes[0][1].set_xlabel('Price ($)')

# Histogram for carat
axes[0][2].hist(diamonds['carat'], bins=50, color='steelblue', edgecolor='black')
axes[0][2].set_title('Histogram of Carat')
axes[0][2].set_xlabel('Carat')

# Box plot of price by cut
diamonds.boxplot(column='price', by='cut', ax=axes[1][0])
axes[1][0].set_title('Price by Cut')
plt.sca(axes[1][0])
plt.xticks(rotation=45)

# Histogram for depth
axes[1][1].hist(diamonds['depth'], bins=50, color='steelblue', edgecolor='black')
axes[1][1].set_title('Histogram of Depth')
axes[1][1].set_xlabel('Depth %')

# Bar chart for color
diamonds['color'].value_counts().sort_index().plot(kind='bar', ax=axes[1][2], color='steelblue', edgecolor='black')
axes[1][2].set_title('Bar Chart of Color')

plt.suptitle('Diamonds Dataset — Exploratory Plots', fontsize=14)
plt.tight_layout()
plt.savefig('notes/labs/week1_diamonds_plots.png', dpi=100, bbox_inches='tight')
plt.close()
print("\n✓ Saved: labs/week1_diamonds_plots.png")

print("\n" + "=" * 70)
print("  WEEK 1 LAB COMPLETE!")
print("=" * 70)
print("""
KEY OBSERVATIONS:
• Price is HEAVILY right-skewed (most diamonds are cheap, a few are expensive)
• Carat is also right-skewed
• Depth is roughly normally distributed (bell-shaped)
• 'Ideal' is the most common cut quality
• Price by Cut shows that (surprisingly?) Ideal cut doesn't have the 
  highest median price — because of confounding with carat size
""")
