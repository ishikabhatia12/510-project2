# AI was used to help generate this file

# Does Chilling Cookie Dough Change Cookie Diameter?

## Research Question
Does refrigerating cookie dough for 30 minutes affect baked cookie diameter compared with baking immediately?

- **H₀:** Chilling cookie dough for 30-minutes has no effect on the mean baked cookie diameter
- **H₁:** Chilling cookie dough for 30-minutes has no effect on the mean baked cookie diameter

## Experiment Summary
- **Independent variable:** Dough treatment (not chilled = 0 min, chilled = 30 min)
- **Dependent variable:** Baked cookie diameter (cm)
- **Controls:**
1. same recipe (https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/) and dough batch
2. oven temperature (375 degrees fareinheit)
3. bake time (10 mins)
4. cookie tray
5. cooling time before measuring (5 minutes)
- **Design:** 
1. 13 cookies per group (26 total), baked as two batches
2. I left my cookies to cool for 30 minuts in my fridge which was set to 37 degrees Fahrenheit
- **Baking procedure:** 
1. All dough balls were portioned from one dough batch. The not-chilled cookies were baked first, while the other dough chilled for 30 minutes
2. After that batch, the oven was turned off and allowed to cool, then preheated again to 375°F before the chilled cookies were baked, using the same temperature, bake time, and tray
- **Randomization:** 
1. Dough balls were numbered 1-26, and 13 were randomly chosen for chilling using a random number generator. The chosen balls were chilled for 30 minutes, and the others were baked right away. Baking order was not randomized: the not-chilled batch was baked first and the chilled batch second
2. I own two of the exact same trays, so chilled cookies were made on one tray, and room-temperature cookies made on another
- **Measurement:** 
1. Diameter was measured in cm with a measuring tape at the widest point to the nearest 0.01 cm. Measurements were taken after 5 minutes of cooling

## Repository Contents
```
.
├── data/
│   ├── pilot_data.csv     # Pilot study data (used only for the power analysis)
│   └── cookies.csv        # Main experiment data (raw; see "Data" below)
├── power_analysis.py      # Calculates the required sample size from the pilot
├── analysis.py            # Assumption checks, Welch's t-test, CI, effect size, plot
└── README.md
```

## Data
- `pilot_data.csv`: pilot measurements used to estimate the effect size and variability for the power analysis. Not included in the main analysis
- `cookies.csv`: main experiment data, one row per cookie

| Column | Description |
|---|---|
| `cookie_id` | Unique cookie identifier by row, not associated with assignment of cookies in either group |
| `chilling_mins` | 0 (baked immediately) or 30 (chilled 30 minutes) |
| `diameter_cm` | Baked cookie diameter in centimeters |

1. Pilot data follows above format as well

## Data Cleaning / Feature Engineering: 
No cookies were removed or altered. The only checks were for missing values and equal group sizes
No new fewatures were engineered 


## How to Reproduce
1. Clone the repository and open the project folder
2. Install the requirements (Python 3.9+):
   ```bash
   pip install pandas numpy matplotlib scipy statsmodels
   ```
3. Gather pilot data
    a. My pilot study does six each, but if able to perform pilot at larger scale for stronger results, user may do so
4. Run the power analysis:
   ```bash
   python power_analysis.py
   ```
5. Gather main data based on sample size receieved in power analysis
6. Run the main analysis
   ```bash
   python analysis.py
   ```

## Methods
- **Power analysis:** Cohen's d computed from the pilot's group means and pooled standard deviation, then used with `TTestIndPower` (α = 0.05, power = 0.80, two-sided) to solve for the required sample size per group.
- **Statistical test:** Welch's two-sample t-test, chosen because it compares two independent group means without assuming equal variances
a. Each cookie was only applied to one group. There was no correlation between cookies across groups. Though all cookies came from the same dough batch, this was intentional ino rder to ensure consistency across the board and avoid variation due to slight differences in dough. However, this is seen as consistency not dependence, therefore, we interpreted independence. 
- **Assumptions checked:** Normality within each group (Shapiro-Wilk) and equality of variances (Levene's test).
- **Also reported:** 95% confidence interval for the mean difference and Cohen's d.
- No post hoc tests are needed because there are only two groups.

## Main Results
| Group | n | Mean (cm) | SD (cm) |
|---|---|---|---|
| Not chilled | 13 | 7.945 | 0.210 |
| Chilled (30 min) | 13 | 7.753 | 0.164 |

- Shapiro-Wilk: p = 0.305 (not chilled), p = 0.381 (chilled); Levene: p = 0.641
- Welch's t-test: t = 2.588, df = 22.7, p = 0.0165
- Mean difference: 0.192 cm, 95% CI [0.038, 0.345]
- Cohen's d = 1.015

Chilled dough produced cookies that were about 0.19 cm narrower on average, and we reject H₀ at α = 0.05. See the written report for interpretation and limitations.