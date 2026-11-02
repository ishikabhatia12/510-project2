#AI helped generate this code

from statsmodels.stats.power import TTestIndPower
import math

# Published study results:
# No chilling: mean diameter = 6.800 cm
# Chilled 120 minutes: mean diameter = 6.167 cm
# Pooled standard deviation ≈ 0.129 cm

effect_size = (6.800 - 6.167) / 0.129

analysis = TTestIndPower()
n = analysis.solve_power(
    effect_size=effect_size,
    alpha=0.05,
    power=0.80,
    alternative='two-sided'
)

print(f"Required sample size per group: {math.ceil(n)}")