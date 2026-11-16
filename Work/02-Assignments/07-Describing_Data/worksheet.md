# 📝 Worksheet: 07 - Describing Data

Use this worksheet to reinforce the descriptive workflow: what each column means, what's typical, how much it varies, what's unusual, how groups differ, and which columns move together. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🏷️ Section 1: Types of Data

1. Classify each as nominal, ordinal, interval, or ratio: `zip code`, `t-shirt size (S/M/L/XL)`, `year of birth`, `monthly rent`.  
   `Answer:` zip-code: nominal, tshit size: ordinal, year of birth: interval, monthly rent is ratio
2. A column has dtype `int64` and only 4 distinct values. Name two things it might really be, and how you'd decide.  
   `Answer:` An int64 column with only 4 distinct values might be an ordinal category or a nominal category coded as numbers. To decide, look at what the values mean, not just the dtype.

---

### ✏️ Task: Record the Meaning

```python
# Using titanic.csv:
# 1. Convert Embarked to 'category' and map C/Q/S to 'Cherbourg'/'Queenstown'/'Southampton'.
# 2. Create an ordered 'class' column (3rd < 2nd < 1st).
# 3. Print the share of passengers above 3rd class, using a comparison on 'class'.
```
import pandas as pd

titanic = pd.read_csv("titanic.csv")

# 1. Convert Embarked to category and map codes to names
titanic["Embarked"] = (
    titanic["Embarked"]
    .map({
        "C": "Cherbourg",
        "Q": "Queenstown",
        "S": "Southampton"
    })
    .astype("category")
)

# 2. Create an ordered class column (3rd < 2nd < 1st)
class_type = pd.CategoricalDtype(
    categories=["3rd", "2nd", "1st"],
    ordered=True
)

titanic["class"] = (
    titanic["Pclass"]
    .map({
        3: "3rd",
        2: "2nd",
        1: "1st"
    })
    .astype(class_type)
)

# 3. Print the share of passengers above 3rd class
share_above_3rd = (titanic["class"] > "3rd").mean()

print(f"Share above 3rd class: {share_above_3rd:.1%}")
``` prints out: Share above 3rd class: 44.9%```
### 🤖 Explain It

In your own words: why does it matter whether a variable is nominal or ordinal before you compute anything with it? What could go wrong if you averaged an ordinal column's codes?
`Answer: Before computing statistics, you need to know whether a variable is nominal or ordinal because the measurement scale determines which calculations are meaningful. Averaging an ordinal column's codes can be misleading because the numeric codes represent ranks, not necessarily equal intervals between categories.`
---

## 🎯 Section 2: Center and Spread

3. Why is the median usually reported for house prices instead of the mean?  
   `Answer:` The median is preferred because house prices are usually right-skewed with a few very expensive properties, and the median is more robust to those extreme values.

4. You compute a standard deviation with pandas and get 14.53, and a classmate uses NumPy and gets 14.52. Who's wrong?  
   `Answer:` Neither is wrong. They are using different default ddof values, which leads to slightly different standard deviation calculations.

---

### ✏️ Task: Compare Center and Spread

```python
# Using pokemon.csv:
# For Attack, print the mean, median, std, and IQR.
# Then do the same for Legendary Pokémon only.
# Which group is more spread out, by std and by IQR? Do the two measures agree?
```
# Attack stats for all Pokémon
attack_all = {
    'mean': poke['Attack'].mean(),
    'median': poke['Attack'].median(),
    'std': poke['Attack'].std(),
    'iqr': poke['Attack'].quantile(0.75) - poke['Attack'].quantile(0.25)
}

print("All Pokémon")
for k, v in attack_all.items():
    print(f"{k:>6}: {v:.2f}")

# Attack stats for Legendary Pokémon only
legendary = poke[poke['Legendary']]

attack_legendary = {
    'mean': legendary['Attack'].mean(),
    'median': legendary['Attack'].median(),
    'std': legendary['Attack'].std(),
    'iqr': legendary['Attack'].quantile(0.75) - legendary['Attack'].quantile(0.25)
}

print("\nLegendary Pokémon")
for k, v in attack_legendary.items():
    print(f"{k:>6}: {v:.2f}")

```Prints out:
All Pokémon
  mean: 79.00
median: 75.00
   std: 32.46
   iqr: 45.00

Legendary Pokémon
  mean: 116.68
median: 110.00
   std: 30.35
   iqr: 31.00
   ```
```# Which group is more spread out, by std and by IQR? Do the two measures agree?
By standard deviation, all Pokémon are more spread out (32.46 vs. 30.35). By IQR, all Pokémon are also more spread out (45.00 vs. 31.00). The two measures agree that Attack has greater variability in the full Pokémon dataset than in the Legendary subset.```

### 🤖 Explain It

In your own words: two classes have the same average exam score, but very different standard deviations. Describe what being a student in each class might be like.
`Answer: If two classes have the same average exam score but different standard deviations, the class with the smaller standard deviation would have most students scoring close to the average. Students in that class would perform fairly similarly. The class with the larger standard deviation would have a wider range of scores, with some students doing very well and others doing poorly, even though the average score is the same.`
---

## 📐 Section 3: Shape and Outliers

5. A column has mean 50, median 38, and `.skew()` of 2.1. Describe its shape.  
   `Answer:` The distribution is strongly right-skewed (positively skewed). The mean (50) is much higher than the median (38), which suggests that a relatively small number of very large values are pulling the mean upward. The skewness of 2.1 confirms a long right tail. This pattern is consistent with the presence of high outliers or extreme values on the upper end of the distribution.

6. Name one situation where you **should** remove an outlier, and one where you shouldn't.  
   `Answer:` Remove an outlier: when it is clearly a data-entry or measurement error, such as a passenger age of 500 years or a negative fare. These values are not realistic and can distort the analysis. Do not remove an outlier: when it is a real but unusual observation, such as a very expensive Titanic ticket fare or a Legendary Pokémon with exceptionally high stats. These values may be important to understanding the data.

---

### ✏️ Task: Outlier Report

```python
# Using penguins.csv (drop the 2 rows with no measurements first):
# 1. Write or copy iqr_fences(series, k=1.5).
# 2. Count outliers in body_mass_g overall, then within each species.
# 3. Print the flagged rows. Are any of them impossible values?
```
import pandas as pd

penguins = pd.read_csv('penguins.csv')
MEASUREMENTS_1 = [
    'bill_length_mm',
    'bill_depth_mm',
    'flipper_length_mm',
    'body_mass_g'
]
# Drop rows missing any measurement
clean = penguins.dropna(subset=MEASUREMENTS_1).copy()

# 1. IQR fence function
def iqr_fences(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr

# 2. Count outliers overall
low, high = iqr_fences(clean['body_mass_g'])

overall_outliers = (
    (clean['body_mass_g'] < low) |
    (clean['body_mass_g'] > high)
)

print(f'Overall outliers: {overall_outliers.sum()}')

# Count outliers within each species
for species, group in clean.groupby('species', observed=True):

    low, high = iqr_fences(group['body_mass_g'])

    outliers = (
        (group['body_mass_g'] < low) |
        (group['body_mass_g'] > high)
    )

    print(f'{species}: {outliers.sum()} outliers')

# 3. Print flagged rows (overall)
flagged = clean.loc[
    overall_outliers,
    ['species', 'island', 'sex', 'body_mass_g']
]

print(flagged)
```prints out: 
Overall outliers: 0
Adelie: 0 outliers
Chinstrap: 2 outliers
Gentoo: 0 outliers
Empty DataFrame
Columns: [species, island, sex, body_mass_g]
Index: []
```
The IQR rule found 0 outliers overall, but 2 body-mass outliers within the Chinstrap species. This shows that a value can be unusual within a species even if it is not unusual in the combined dataset. None of the flagged values appear impossible; they are likely real but extreme body masses rather than data-entry errors.
### 🤖 Explain It

In your own words: explain to a classmate why "outlier" and "error" aren't the same thing, using an example from the Titanic fares.
`Answer: An outlier is not necessarily an error. An outlier is simply a value that is unusually far from the rest of the data, while an error is a value that is incorrect or impossible. For example, some Titanic first-class passengers paid very high fares, and those fares may be flagged as outliers, but they are real observations and should not automatically be removed. In contrast, a fare of -$50 or a fare recorded in the wrong units would be an error because it is not a valid value. Errors should be corrected or treated as missing data (NaN), while real outliers should usually be investigated rather than deleted.`
---

## 👥 Section 4: Comparing Groups

7. When should you compare groups with counts, and when with rates?  
   `Answer:` Compare counts when the total number of cases matters, such as the number of Titanic 3rd-class passengers or the total number of survivors. Compare rates when groups have different sizes and you want a fair comparison of outcomes. For example, when comparing survival between 2nd and 3rd class, the survival rate is more informative because there were many more 3rd-class passengers. Looking at rates helps explain why 3rd class had a lower chance of survival even if more 3rd-class passengers survived in total. 

8. What's the difference between `normalize='index'` and `normalize='columns'` in `pd.crosstab()`? Write a question each one answers.  
   `Answer:` normalize='index' gives row percentages and answers questions about the composition of each row group. For example: "Within each passenger class, what percentage are male and what percentage are female?"normalize='columns' gives column percentages and answers questions about the composition of each column group. For example: "Within all females (or within all males), what percentage belong to each passenger class?"
---

### ✏️ Task: Survival Table

```python
# Using titanic.csv:
# 1. Bin Age into child (0-12), teen (13-18), adult (19-60), senior (61+) with pd.cut().
# 2. Build a pivot_table of survival rate with age group as rows and Sex as columns.
# 3. Add the group sizes (a second pivot_table with aggfunc='size').
# Which cell has the highest rate? Is its group big enough to trust?
```
import pandas as pd

titanic = pd.read_csv("titanic.csv")

# 1. Create age groups
titanic["age_group"] = pd.cut(
    titanic["Age"],
    bins=[0, 12, 18, 60, float("inf")],
    labels=["child", "teen", "adult", "senior"],
    include_lowest=True
)

# 2. Survival-rate pivot table
survival_rate = (
    titanic.pivot_table(
        values="Survived",
        index="age_group",
        columns="Sex",
        aggfunc="mean",
        observed=True
    ) * 100
).round(1)

print("Survival Rate (%)")
print(survival_rate)

# 3. Group-size pivot table
group_sizes = titanic.pivot_table(
    values="Survived",
    index="age_group",
    columns="Sex",
    aggfunc="size",
    observed=True
)

print("\nGroup Sizes")
print(group_sizes)

highest_rate = survival_rate.stack().idxmax()
highest_value = survival_rate.stack().max()

print("Highest rate:")
print(highest_rate, highest_value)

``prints out: 

Survival Rate (%)
Sex        female  male
age_group              
child        59.4  56.8
teen         75.0   8.8
adult        77.9  18.5
senior      100.0  10.5

Group Sizes
Sex        female  male
age_group              
child          32    37
teen           36    34
adult         190   363
senior          3    19

Highest rate:
('senior', 'female') 100.0
``
The highest survival rate is for senior females, at 100%. However, this group contains only 3 passengers, so the result is probably not large enough to trust as a reliable estimate. With such a small sample size, even one additional non-survivor would change the survival rate dramatically.
### 🤖 Explain It

In your own words: what's a confounder? Describe one in the Titanic data, and how you'd check for it with a table.
`Answer: A confounder is a variable that is related to both the explanatory variable and the outcome, making it seem like one variable causes the other when part of the relationship is actually due to the confounder.

Titanic example: Suppose we find that passengers who embarked at Cherbourg had a higher survival rate than passengers from other ports. That does not necessarily mean the port itself improved survival. A possible confounder is passenger class (Pclass):

Cherbourg had a larger share of 1st-class passengers.
1st-class passengers had a higher survival rate.
Therefore, part of Cherbourg's higher survival rate may be explained by its passenger-class mix rather than the embarkation port itself.
---

## 🔗 Section 5: Relationships and Correlation

9. When would you use Spearman instead of Pearson?  
   `Answer:` Use Spearman instead of Pearson when the relationship is not linear but still follows a general increasing or decreasing trend, or when the data contain outliers or are highly skewed. Spearman uses ranks rather than the raw values, making it less sensitive to extreme observations.

10. A news story says "cities with more ice-cream sales have more drownings." Give a likely confounder.  
    `Answer:` The confounder is hot weather (or summer season), which increases both ice-cream sales and swimming activity, leading to more drownings.

---

### ✏️ Task: Correlation Report

```python
# Using pokemon.csv:
# 1. Compute the Pearson and Spearman correlation matrices of the six stats.
# 2. List the three strongest pairs (use the upper triangle).
# 3. Recompute r(Attack, Defense) for Legendary and non-Legendary separately.
```
import numpy as np
import pandas as pd

poke = pd.read_csv("pokemon.csv")

stats = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

# 1. Correlation matrices
pearson_corr = poke[stats].corr(method='pearson')
spearman_corr = poke[stats].corr(method='spearman')

print("Pearson")
print(pearson_corr.round(3))

print("\nSpearman")
print(spearman_corr.round(3))

# 2. Three strongest Pearson pairs
upper = pearson_corr.where(
    np.triu(np.ones(pearson_corr.shape, dtype=bool), k=1)
)

pairs = (
    upper.stack()
    .rename('r')
    .sort_values(key=abs, ascending=False)
)

print("\nTop 3 Pearson pairs")
print(pairs.head(3).round(3))

# 3. r(Attack, Defense) overall and by Legendary status
print(
    "\nOverall:",
    round(poke['Attack'].corr(poke['Defense']), 3)
)

for legendary, group in poke.groupby('Legendary'):
    r = group['Attack'].corr(group['Defense'])

    print(
        f'Legendary={legendary}: '
        f'r = {r:.3f} (n = {len(group)})'
    )
``prints out: 
Pearson
            HP  Attack  Defense  Sp. Atk  Sp. Def  Speed
HP       1.000   0.422    0.240    0.362    0.379  0.176
Attack   0.422   1.000    0.439    0.396    0.264  0.381
Defense  0.240   0.439    1.000    0.224    0.511  0.015
Sp. Atk  0.362   0.396    0.224    1.000    0.506  0.473
Sp. Def  0.379   0.264    0.511    0.506    1.000  0.259
Speed    0.176   0.381    0.015    0.473    0.259  1.000

Spearman
            HP  Attack  Defense  Sp. Atk  Sp. Def  Speed
HP       1.000   0.566    0.433    0.471    0.493  0.266
Attack   0.566   1.000    0.515    0.362    0.321  0.373
Defense  0.433   0.515    1.000    0.314    0.579  0.093
Sp. Atk  0.471   0.362    0.314    1.000    0.572  0.460
Sp. Def  0.493   0.321    0.579    0.572    1.000  0.321
Speed    0.266   0.373    0.093    0.460    0.321  1.000

Top 3 Pearson pairs
Defense  Sp. Def    0.511
Sp. Atk  Sp. Def    0.506
         Speed      0.473
Name: r, dtype: float64

Overall: 0.439
Legendary=False: r = 0.437 (n = 735)
Legendary=True: r = -0.211 (n = 65)
``
The strongest Pearson correlations were Defense-Sp. Def (r = 0.511), Sp. Atk-Sp. Def (r = 0.506), and Sp. Atk-Speed (r = 0.473). Attack and Defense are moderately positively correlated overall (r = 0.439) and among non-Legendary Pokémon (r = 0.437), but the correlation is weakly negative among Legendary Pokémon (r = -0.211). This suggests the Attack-Defense relationship differs for Legendary Pokémon and that subgroup analysis can reveal patterns hidden in the combined data.
### 🤖 Explain It

In your own words: Anscombe's four datasets all have r = 0.82. What does that teach you about reporting a correlation without a plot? What's the danger of a single summary number?
``Answer: Anscombe's quartet shows that datasets can have the same summary statistics, including the same correlation (r = 0.82), but very different patterns when plotted. This teaches us that reporting a correlation without a graph can be misleading.

The danger of a single summary number is that it hides important features of the data, such as outliers, clusters, nonlinear relationships, or unusual distributions. Two datasets can have the same correlation yet tell completely different stories, so it is important to visualize the data with a scatterplot instead of relying only on the correlation coefficient.``
---

## 🧾 Submit Checklist

- [X] I built a data dictionary that separates dtype from measurement scale.
- [X] I used an ordered category and computed a proportion from a boolean column.
- [X] I reported center and spread that fit a column's shape, and explained `ddof`.
- [X] I flagged outliers with the IQR rule, inspected them, and decided what to do with them.
- [X] I compared groups with sizes and rates, using a crosstab and a pivot table.
- [X] I computed Pearson and Spearman correlations and explained a possible confounder.
- [X] I completed the "Explain It" prompts in my own words.
