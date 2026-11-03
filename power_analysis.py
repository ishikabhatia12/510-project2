# AI was used to help generate this code

import pandas as pd
from statsmodels.stats.power import TTestIndPower

# Load pilot data
df = pd.read_csv("data/pilot_data.csv")

# Pilot study results
control = df[df["chilling_mins"] == 0]["diameter_cm"]
treatment = df[df["chilling_mins"] == 30]["diameter_cm"]

control_mean, control_std = control.mean(), control.std()
treatment_mean, treatment_std = treatment.mean(), treatment.std()
pooled_std = ((control_std**2 + treatment_std**2) / 2) ** 0.5

print("Pilot study results:")
print(f"Control: mean = {control_mean:.3f}, std = {control_std:.3f}")
print(f"Treatment: mean = {treatment_mean:.3f}, std = {treatment_std:.3f}")
print(f"Pooled std = {pooled_std:.3f}")

effect_size = abs(treatment_mean - control_mean) / pooled_std  # Cohen's d
print(f"Cohen's d = {effect_size:.3f}")

analysis = TTestIndPower()
n = analysis.solve_power(
    effect_size=effect_size,
    alpha=0.05,
    power=0.80,
    alternative='two-sided'
)
print(f"Required sample size per group: {n:.0f}")