# AI was used to help generate this code

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

alpha = 0.05

# 1. Load main experiment data (not pilot data)
df = pd.read_csv("data/cookies.csv")

# 2. Basic checks
print("Missing values:\n", df.isna().sum())
print("\nCookies per group:\n", df["chilling_mins"].value_counts())

control = df[df["chilling_mins"] == 0]["diameter_cm"]
treatment = df[df["chilling_mins"] == 30]["diameter_cm"]

# 3. Descriptive statistics
print("\nSummary statistics:")
print(df.groupby("chilling_mins")["diameter_cm"].agg(["count", "mean", "std"]).round(3))

# 4. Check assumptions
# p > 0.05 means no clear evidence against normality.
print("\nShapiro-Wilk normality tests:")
print(f"0 minutes: p = {stats.shapiro(control).pvalue:.3f}")
print(f"30 minutes: p = {stats.shapiro(treatment).pvalue:.3f}")
print(f"Levene's test: p = {stats.levene(control, treatment).pvalue:.3f}")

# 5. Welch's two-sample t-test (does not require equal variances)
# Null: mean cookie diameter is the same for both chilling times.
# Alternative: mean cookie diameter differs between chilling times.
result = stats.ttest_ind(control, treatment, equal_var=False)
ci = result.confidence_interval(confidence_level=1-alpha)
difference = control.mean() - treatment.mean()

print("\nWelch's t-test:")
print(f"t = {result.statistic:.3f}, df = {result.df:.1f}, p = {result.pvalue:.4f}")
print(f"Mean difference (0 - 30 minutes) = {difference:.3f} cm")
print(f"95% confidence interval: [{ci.low:.3f}, {ci.high:.3f}] cm")

if result.pvalue < alpha:
    print("Reject the null: evidence of a difference in mean diameter.")
else:
    print("Fail to reject the null: insufficient evidence of a difference in mean diameter.")

# 6. Effect size (Cohen's d)
n1, n2 = len(control), len(treatment)
pooled_std = (((n1 - 1) * control.var() + (n2 - 1) * treatment.var()) / (n1 + n2 - 2)) ** 0.5
print(f"Cohen's d (0 - 30 minutes) = {difference / pooled_std:.3f}")

# 7. Compare the groups visually
fig, ax = plt.subplots(figsize=(5, 4))
ax.boxplot([control, treatment])
ax.set_xticks([1, 2], ["0 minutes", "30 minutes"])
ax.set_xlabel("Dough chilling time")
ax.set_ylabel("Cookie diameter (cm)")
ax.set_title("Cookie diameter by chilling time")
fig.tight_layout()
plt.show()
