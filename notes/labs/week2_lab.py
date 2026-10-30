"""
QDA WEEK 2 LAB — Inferential Statistics: Confidence Intervals
=============================================================
Part 1: Confidence intervals for proportions and means (guided lab)
Part 2: Independent practice with auto-mpg dataset

R equivalents shown in comments throughout.
Run: python labs/week2_lab.py
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 70)
print("  QDA WEEK 2 LAB — CONFIDENCE INTERVALS")
print("=" * 70)

# =====================================================================
# PART 1: Guided Lab — Confidence Intervals (lab2-part1)
# =====================================================================
print("\n" + "=" * 70)
print("PART 1: Guided Lab — Confidence Intervals")
print("=" * 70)

# --- Recap: what types of plots suit which variable type? ---
print("""
Quick Recap from Week 1:
  Categorical variables → bar chart, pie chart
  Numerical variables   → histogram, box plot
""")

# =================================================================
# 1A. CONFIDENCE INTERVAL FOR A PROPORTION
# =================================================================
print("-" * 50)
print("1A. Confidence Interval for a Proportion")
print("-" * 50)

print("""
SCENARIO: A market research agency interviews a random sample of 1000 
people in London. 49% say they will vote Labour for Mayor.

Find the 95% and 90% confidence intervals for the TRUE proportion.
""")

# R: prop.test(490, 1000, conf.level = 0.95)
# Python equivalent using statsmodels or scipy

# Method 1: Manual calculation
n = 1000
p_hat = 490 / 1000  # = 0.49

# 95% CI
z_95 = stats.norm.ppf(0.975)  # R: qnorm(0.975) = 1.96
se = np.sqrt(p_hat * (1 - p_hat) / n)
ci_95_lower = p_hat - z_95 * se
ci_95_upper = p_hat + z_95 * se

print(f"Sample proportion (p̂) = {p_hat}")
print(f"Sample size (n) = {n}")
print(f"Z-value for 95% = {z_95:.4f}")
print(f"Standard error = sqrt(p̂(1-p̂)/n) = sqrt({p_hat}×{1-p_hat}/{n}) = {se:.4f}")
print(f"\n95% Confidence Interval:")
print(f"  p̂ ± Z × SE = {p_hat} ± {z_95:.4f} × {se:.4f}")
print(f"  = ({ci_95_lower:.4f}, {ci_95_upper:.4f})")
print(f"  Rounded: ({ci_95_lower:.2f}, {ci_95_upper:.2f})")

# 90% CI
z_90 = stats.norm.ppf(0.95)  # R: qnorm(0.95) = 1.645
ci_90_lower = p_hat - z_90 * se
ci_90_upper = p_hat + z_90 * se

print(f"\n90% Confidence Interval:")
print(f"  Z-value for 90% = {z_90:.4f}")
print(f"  = ({ci_90_lower:.4f}, {ci_90_upper:.4f})")
print(f"  Rounded: ({ci_90_lower:.2f}, {ci_90_upper:.2f})")

print(f"""
INTERPRETATION:
  "We are 95% confident that the true proportion of London voters 
   who would vote Labour is between {ci_95_lower:.2f} and {ci_95_upper:.2f}."

  "We are 90% confident that the true proportion is between 
   {ci_90_lower:.2f} and {ci_90_upper:.2f}."

NOTICE: The 90% CI is NARROWER than the 95% CI.
  → Lower confidence = narrower interval (less cautious)
  → Higher confidence = wider interval (more cautious)
""")

# Method 2: Using statsmodels (closer to R's prop.test)
from statsmodels.stats.proportion import proportion_confint
ci_low_95, ci_high_95 = proportion_confint(490, 1000, alpha=0.05, method='normal')
ci_low_90, ci_high_90 = proportion_confint(490, 1000, alpha=0.10, method='normal')
print(f"Verification using statsmodels:")
print(f"  95% CI: ({ci_low_95:.4f}, {ci_high_95:.4f})")
print(f"  90% CI: ({ci_low_90:.4f}, {ci_high_90:.4f})")

# =================================================================
# 1B. CONFIDENCE INTERVAL FOR THE MEAN
# =================================================================
print("\n" + "-" * 50)
print("1B. Confidence Interval for the Mean")
print("-" * 50)

# R: data <- read.csv("skewdata.csv")
data = pd.read_csv("skewdata.csv")

print(f"\nSkewdata dataset loaded: {len(data)} observations")
# R: summary(data)
print(f"\nSummary:")
print(data.describe().round(3))

# Histogram
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data['values'], bins=20, color='steelblue', edgecolor='black')
ax.set_title('Histogram of Values (skewdata)')
ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('notes/labs/week2_skewdata_histogram.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Saved: labs/week2_skewdata_histogram.png")
print("  → Notice this data is RIGHT-SKEWED (long tail to the right)")

# 95% CI for the mean using t.test
# R: t.test(data$values)
values = data['values'].values
n = len(values)
x_bar = np.mean(values)
s = np.std(values, ddof=1)

# t-test confidence interval
t_result = stats.ttest_1samp(values, popmean=0)  # we just want the CI
# More directly, compute it manually:
t_val_95 = stats.t.ppf(0.975, df=n-1)  # R: qt(0.975, df=n-1)
se = s / np.sqrt(n)

ci_95_lower = x_bar - t_val_95 * se
ci_95_upper = x_bar + t_val_95 * se

print(f"\n--- 95% Confidence Interval for the Mean ---")
print(f"  Sample mean (x̄) = {x_bar:.2f}")
print(f"  Sample SD (s) = {s:.2f}")
print(f"  n = {n}")
print(f"  df = n - 1 = {n-1}")
print(f"  t-value (0.975, df={n-1}) = {t_val_95:.4f}")
print(f"  Standard error = s/√n = {s:.2f}/√{n} = {se:.4f}")
print(f"  CI = x̄ ± t × SE = {x_bar:.2f} ± {t_val_95:.4f} × {se:.4f}")
print(f"  95% CI: ({ci_95_lower:.2f}, {ci_95_upper:.2f})")

# 90% CI
t_val_90 = stats.t.ppf(0.95, df=n-1)
ci_90_lower = x_bar - t_val_90 * se
ci_90_upper = x_bar + t_val_90 * se

print(f"\n--- 90% Confidence Interval for the Mean ---")
print(f"  t-value (0.95, df={n-1}) = {t_val_90:.4f}")
print(f"  90% CI: ({ci_90_lower:.2f}, {ci_90_upper:.2f})")

print(f"""
COMPARISON:
  95% CI: ({ci_95_lower:.2f}, {ci_95_upper:.2f})  width = {ci_95_upper - ci_95_lower:.2f}
  90% CI: ({ci_90_lower:.2f}, {ci_90_upper:.2f})  width = {ci_90_upper - ci_90_lower:.2f}

  → The 90% CI is NARROWER. Less confidence = narrower interval.
  → Same principle as with the proportion CI.
""")

# Visualise the CIs
fig, ax = plt.subplots(figsize=(10, 3))
ax.plot([ci_95_lower, ci_95_upper], [2, 2], 'b-o', linewidth=2, markersize=8, label='95% CI')
ax.plot([ci_90_lower, ci_90_upper], [1, 1], 'r-o', linewidth=2, markersize=8, label='90% CI')
ax.axvline(x=x_bar, color='green', linestyle='--', label=f'Sample mean = {x_bar:.2f}')
ax.set_yticks([1, 2])
ax.set_yticklabels(['90% CI', '95% CI'])
ax.set_xlabel('Value')
ax.set_title('Comparing 95% and 90% Confidence Intervals for the Mean')
ax.legend()
plt.tight_layout()
plt.savefig('notes/labs/week2_ci_comparison.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Saved: labs/week2_ci_comparison.png")

# =====================================================================
# PART 2: Independent Practice — auto-mpg dataset
# =====================================================================
print("\n" + "=" * 70)
print("PART 2: Independent Practice — auto-mpg Dataset")
print("=" * 70)

# R: read.csv("auto-mpg.csv")
mpg = pd.read_csv("auto-mpg.csv")

print(f"\nDataset: {mpg.shape[0]} rows × {mpg.shape[1]} columns")
print(f"\nFirst 5 rows:")
print(mpg.head().to_string())

# Step 5: Explore the data
print(f"\n--- Summary Statistics ---")
# Need to handle horsepower — it might have '?' values
print(f"\nData types:")
print(mpg.dtypes)

# Clean horsepower if needed
if mpg['horsepower'].dtype == 'object':
    print("\n⚠ 'horsepower' is stored as text — likely has missing values coded as '?'")
    mpg['horsepower'] = pd.to_numeric(mpg['horsepower'], errors='coerce')
    print(f"  Converted. Missing values: {mpg['horsepower'].isna().sum()}")

print(f"\nNumerical summary:")
print(mpg.describe().round(2))

# Step 5: Which continuous variables look normally distributed?
print(f"\n--- Checking for Normal Distribution ---")
continuous_cols = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes_flat = axes.flatten()

for i, col in enumerate(continuous_cols):
    ax = axes_flat[i]
    vals = mpg[col].dropna()
    ax.hist(vals, bins=30, color='steelblue', edgecolor='black', density=True, alpha=0.7)
    
    # Overlay a normal curve
    x_range = np.linspace(vals.min(), vals.max(), 100)
    ax.plot(x_range, stats.norm.pdf(x_range, vals.mean(), vals.std()), 'r-', linewidth=2)
    
    ax.set_title(f'{col} (mean={vals.mean():.1f}, sd={vals.std():.1f})')
    ax.set_xlabel(col)
    
    # Shapiro-Wilk test (if sample small enough) or visual check
    if len(vals) <= 5000:
        _, p_val = stats.shapiro(vals)
        normality = "Looks Normal" if p_val > 0.05 else "NOT Normal"
        ax.text(0.95, 0.95, f'{normality}\n(Shapiro p={p_val:.4f})', 
                transform=ax.transAxes, ha='right', va='top', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='wheat'))

# Remove extra subplot
axes_flat[5].axis('off')

plt.suptitle('auto-mpg: Distribution of Continuous Variables\n(Red curve = fitted Normal distribution)', fontsize=13)
plt.tight_layout()
plt.savefig('notes/labs/week2_mpg_distributions.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Saved: labs/week2_mpg_distributions.png")

for col in continuous_cols:
    vals = mpg[col].dropna()
    _, p_val = stats.shapiro(vals)
    skew = vals.skew()
    assessment = "≈ Normal" if abs(skew) < 0.5 and p_val > 0.01 else "NOT Normal (skewed or heavy-tailed)"
    print(f"  {col:15s}: skewness={skew:+.2f}, Shapiro p={p_val:.4f} → {assessment}")

# Step 6: 95% CI for a normally-distributed variable
print(f"\n--- Step 6: 95% CI for acceleration (closest to Normal) ---")
accel = mpg['acceleration'].dropna()
n = len(accel)
x_bar = accel.mean()
s = accel.std(ddof=1)
t_val = stats.t.ppf(0.975, df=n-1)
se = s / np.sqrt(n)
ci_lower = x_bar - t_val * se
ci_upper = x_bar + t_val * se

print(f"  Variable: acceleration")
print(f"  n = {n}, mean = {x_bar:.3f}, SD = {s:.3f}")
print(f"  t(0.975, df={n-1}) = {t_val:.4f}")
print(f"  SE = {s:.3f}/√{n} = {se:.4f}")
print(f"  95% CI: ({ci_lower:.3f}, {ci_upper:.3f})")
print(f"""
  INTERPRETATION: "We are 95% confident that the true mean acceleration 
  for this population of cars is between {ci_lower:.2f} and {ci_upper:.2f} seconds."
""")

# R equivalent:
# t.test(mpg$acceleration, conf.level = 0.95)

# Step 7 & 8: Proportion of cars from the 80s
print(f"--- Steps 7-8: Proportion of 80s cars ---")
print(f"  Model years in the data: {sorted(mpg['model year'].unique())}")

n_total = len(mpg)
n_80s = (mpg['model year'] >= 80).sum()
p_80s = n_80s / n_total

print(f"  Total cars: {n_total}")
print(f"  Cars from the 80s (model year ≥ 80): {n_80s}")
print(f"  Proportion from 80s: {p_80s:.4f} = {p_80s*100:.1f}%")

# 90% CI for this proportion
# R: prop.test(n_80s, n_total, conf.level = 0.90)
z_90 = stats.norm.ppf(0.95)
se_p = np.sqrt(p_80s * (1 - p_80s) / n_total)
ci_p_lower = p_80s - z_90 * se_p
ci_p_upper = p_80s + z_90 * se_p

print(f"\n  90% CI for proportion of 80s cars:")
print(f"  Z(0.95) = {z_90:.4f}")
print(f"  SE = sqrt(p̂(1-p̂)/n) = {se_p:.4f}")
print(f"  CI = {p_80s:.4f} ± {z_90:.4f} × {se_p:.4f}")
print(f"  90% CI: ({ci_p_lower:.4f}, {ci_p_upper:.4f})")
print(f"""
  INTERPRETATION: "We are 90% confident that the true proportion of 
  this car population that are from the 1980s is between 
  {ci_p_lower:.1%} and {ci_p_upper:.1%}."
""")

# Also compute 95% CI to compare
ci_p95_lower, ci_p95_upper = proportion_confint(n_80s, n_total, alpha=0.05, method='normal')
print(f"  For comparison, 95% CI: ({ci_p95_lower:.4f}, {ci_p95_upper:.4f})")
print(f"  90% CI width: {ci_p_upper - ci_p_lower:.4f}")
print(f"  95% CI width: {ci_p95_upper - ci_p95_lower:.4f}")
print(f"  → As expected, 95% CI is wider than 90% CI")

# Step 9: Track what happens to CI width
print(f"\n--- Step 9: Effect of Confidence Level on CI Width ---")
print(f"\nCI for mean acceleration at different confidence levels:")
print(f"{'Level':>10s} {'t-value':>10s} {'Lower':>10s} {'Upper':>10s} {'Width':>10s}")
print("-" * 55)
for level in [0.80, 0.85, 0.90, 0.95, 0.99]:
    t_v = stats.t.ppf(1 - (1-level)/2, df=n-1)
    lo = x_bar - t_v * se
    hi = x_bar + t_v * se
    width = hi - lo
    print(f"{level:>9.0%} {t_v:>10.4f} {lo:>10.3f} {hi:>10.3f} {width:>10.3f}")

print(f"\nCI for proportion of 80s cars at different confidence levels:")
print(f"{'Level':>10s} {'Z-value':>10s} {'Lower':>10s} {'Upper':>10s} {'Width':>10s}")
print("-" * 55)
for level in [0.80, 0.85, 0.90, 0.95, 0.99]:
    z_v = stats.norm.ppf(1 - (1-level)/2)
    lo = p_80s - z_v * se_p
    hi = p_80s + z_v * se_p
    width = hi - lo
    print(f"{level:>9.0%} {z_v:>10.4f} {lo:>10.4f} {hi:>10.4f} {width:>10.4f}")

print("""
KEY PATTERN: As confidence level increases, the CI gets WIDER.
  → You're trading precision for certainty.
  → 80% CI is narrow but you're less sure the true value is in it.
  → 99% CI is wide but you're very sure the true value is in it.
""")

# =====================================================================
# BONUS: Visualise the concept — sampling distributions
# =====================================================================
print("=" * 70)
print("BONUS: Simulating the Gumball Machine")
print("=" * 70)

np.random.seed(42)
true_proportion = 0.5  # The actual proportion of red sweets

# Take 1000 samples of 10 sweets each
n_samples = 1000
sample_size = 10
sample_proportions = []

for _ in range(n_samples):
    sample = np.random.binomial(1, true_proportion, sample_size)
    sample_proportions.append(sample.sum() / sample_size)

sample_proportions = np.array(sample_proportions)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histogram of sample proportions
axes[0].hist(sample_proportions, bins=11, color='red', edgecolor='black', alpha=0.7, density=True)
axes[0].axvline(x=true_proportion, color='blue', linestyle='--', linewidth=2, label=f'True proportion = {true_proportion}')
axes[0].axvline(x=sample_proportions.mean(), color='green', linestyle=':', linewidth=2, label=f'Mean of samples = {sample_proportions.mean():.3f}')
axes[0].set_title(f'Gumball Machine: 1000 samples of {sample_size} sweets')
axes[0].set_xlabel('Proportion of Red Sweets')
axes[0].set_ylabel('Density')
axes[0].legend()

# Show how CI narrows with more data
sample_sizes = [10, 30, 50, 100, 200, 500]
ci_widths = []
for ss in sample_sizes:
    # Simulate one large experiment
    samples = np.random.binomial(1, true_proportion, ss)
    p_hat = samples.mean()
    se = np.sqrt(p_hat * (1-p_hat) / ss)
    ci_widths.append(2 * 1.96 * se)  # width of 95% CI

axes[1].plot(sample_sizes, ci_widths, 'bo-', linewidth=2, markersize=8)
axes[1].set_title('95% CI Width vs Sample Size')
axes[1].set_xlabel('Sample Size')
axes[1].set_ylabel('CI Width')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('notes/labs/week2_gumball_simulation.png', dpi=100, bbox_inches='tight')
plt.close()
print("✓ Saved: labs/week2_gumball_simulation.png")

print(f"""
GUMBALL MACHINE RESULTS:
  True proportion of red sweets: {true_proportion}
  Mean of 1000 sample proportions: {sample_proportions.mean():.4f}
  
  In 97.5% of samples, the proportion was between:
    {np.percentile(sample_proportions, 1.25):.1f} and {np.percentile(sample_proportions, 98.75):.1f}
  
  This is the intuition behind a confidence interval!
""")

# =====================================================================
# SUMMARY TABLE: R ↔ Python command mapping
# =====================================================================
print("=" * 70)
print("QUICK REFERENCE: R vs Python commands")
print("=" * 70)
print("""
  TASK                      R COMMAND                       PYTHON EQUIVALENT
  ─────────────────────────────────────────────────────────────────────────────
  CI for proportion         prop.test(490, 1000,            proportion_confint(490, 1000,
                              conf.level=0.95)                alpha=0.05, method='normal')
  
  CI for mean               t.test(x, conf.level=0.95)      stats.ttest_1samp(x, 0)
                                                             or manual: x̄ ± t × (s/√n)
  
  Z critical value          qnorm(0.975)                    stats.norm.ppf(0.975)
  
  t critical value          qt(0.975, df=29)                stats.t.ppf(0.975, df=29)
  
  Normal density            dnorm(x, mean, sd)              stats.norm.pdf(x, mean, sd)
  
  Normal CDF                pnorm(x, mean, sd)              stats.norm.cdf(x, mean, sd)
  
  Histogram                 hist(x, breaks=20)              plt.hist(x, bins=20)
""")

print("\n" + "=" * 70)
print("  WEEK 2 LAB COMPLETE!")
print("=" * 70)
