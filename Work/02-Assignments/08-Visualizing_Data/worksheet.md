# 📝 Worksheet: 08 - Visualizing Data

Use this worksheet to reinforce object-oriented Matplotlib, pandas plotting, Seaborn, and chart design. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🖼️ Section 1: Matplotlib, Object-Oriented

1. What's the difference between `plt.title('X')` and `ax.set_title('X')`? When does the difference matter?  
   `Answer:` plt.title() works on the current plot, while ax.set_title() works on a specific axes object. The difference becomes important when a figure contains multiple subplots, which is why the object-oriented style (ax.set_title()) is generally preferred.
2. You're comparing three histograms in a 1 × 3 figure. Name two settings that make the panels fair to compare.  
   `Answer:` Use sharex=True and sharey=True so all panels have the same x- and y-axis scales, making comparisons fair and accurate.

---

### ✏️ Task: A Reusable Chart Function

```python
# Write plot_distribution(ax, series, title, unit) that draws a histogram on ax,
# marks the mean and median with vertical lines, and labels everything.
# Use it to build a 2 x 2 figure of Titanic Age, Fare (log scale!), SibSp, and Parch.
# Save the figure with fig.savefig().
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv('titanic.csv')

def plot_distribution(ax, series, title, unit):
    data = series.dropna()

    # Histogram
    ax.hist(data, bins=30, edgecolor="black", alpha=0.7)

    # Mean and median lines
    mean_val = data.mean()
    median_val = data.median()

    ax.axvline(mean_val, color="red", linestyle="--",
               linewidth=2, label=f"Mean = {mean_val:.2f}")
    ax.axvline(median_val, color="blue", linestyle="-",
               linewidth=2, label=f"Median = {median_val:.2f}")

    # Labels
    ax.set_title(title)
    ax.set_xlabel(unit)
    ax.set_ylabel("Count")
    ax.legend()

# Create 2x2 figure
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

plot_distribution(
    axes[0, 0],
    titanic["Age"],
    "Titanic Age Distribution",
    "Age (years)"
)

plot_distribution(
    axes[0, 1],
    titanic["Fare"],
    "Titanic Fare Distribution",
    "Fare ($)"
)
axes[0, 1].set_xscale("log")  # Log scale for Fare

plot_distribution(
    axes[1, 0],
    titanic["SibSp"],
    "Titanic SibSp Distribution",
    "Number of Siblings/Spouses"
)

plot_distribution(
    axes[1, 1],
    titanic["Parch"],
    "Titanic Parch Distribution",
    "Number of Parents/Children"
)

fig.suptitle("Titanic Distributions", fontsize=16)
fig.tight_layout()

fig.savefig("titanic_distributions.png", dpi=300, bbox_inches="tight")

plt.show()


### 🤖 Explain It

In your own words: why is a function that takes an `ax` argument more useful than a function that calls `plt.` directly?
`Answer: Passing ax makes the function reusable for any subplot and avoids relying on Matplotlib's current state, which is especially important when creating figures with multiple panels.`
---

## 🐼 Section 2: Plotting with Pandas

3. When you call `.plot.bar()` on a DataFrame, what does the index become, and what do the columns become?  
   `Answer:` When you call df.plot.bar(), the DataFrame index becomes the x-axis categories, and each column becomes a separate set of bars (a series) in the chart.`

4. Give one example of wide data and the same data in long form.  
   `Answer:` In wide data, each group/category is a separate column. In long data, the group names are values in a categorical column, and the measurements are in another column. Pandas .plot() commonly uses wide data, while Seaborn usually expects long data.

---

### ✏️ Task: Summary Table to Chart

```python
# Using pokemon.csv:
# 1. Build a crosstab of Generation vs. Legendary, normalized by row.
# 2. Plot it as a 100% stacked bar chart with a percent-formatted axis.
# 3. Melt the (un-normalized) crosstab into long form with columns Generation, Legendary, count.
```
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

poke = pd.read_csv('pokemon.csv')
# 1. Crosstab normalized by row
ct = pd.crosstab(
    poke["Generation"],
    poke["Legendary"],
    normalize="index"
)

# 2. 100% stacked bar chart
fig, ax = plt.subplots(figsize=(8, 5))

ct.plot(
    kind="bar",
    stacked=True,
    ax=ax
)

ax.set_title("Percentage of Legendary Pokemon by Generation")
ax.set_xlabel("Generation")
ax.set_ylabel("Percent")
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
ax.legend(title="Legendary")

fig.tight_layout()
plt.show()

# 3. Un-normalized crosstab melted to long form
ct_counts = pd.crosstab(
    poke["Generation"],
    poke["Legendary"]
)

long_ct = (
    ct_counts
    .reset_index()
    .melt(
        id_vars="Generation",
        var_name="Legendary",
        value_name="count"
    )
)
result table: 
   Generation Legendary  count
0           1     False    160
1           2     False    101
2           3     False    142
3           4     False    108
4           5     False    150
### 🤖 Explain It

In your own words: when would you plot with pandas `.plot`, and when would you switch to Seaborn?
`answer: Pandas .plot() is best for quick plots of already summarized data, while Seaborn is better for exploring distributions, relationships, and group comparisons in raw data.`
---

## 🌊 Section 3: Seaborn Distributions

5. Why can a histogram with `hue` and raw counts be misleading when the groups are very different sizes? What's the fix?  
   `Answer:` A histogram with hue and raw counts can be misleading because larger groups automatically produce taller bars. The fix is to plot percentages/proportions (e.g., stat='percent', common_norm=False) and often include the sample sizes (n=) for context.

6. Explain how a box plot's whiskers and dots connect to the 1.5 × IQR rule from Module 07.  
   `Answer:` The whiskers extend to the most extreme values within the 1.5 × IQR bounds, and any values beyond those bounds are shown as dots (outliers).

---

### ✏️ Task: Compare Distributions Four Ways

```python
# Using penguins.csv, for flipper_length_mm by species, make a 2 x 2 figure:
# a step histogram with hue, a KDE with hue, a box plot, and a violin plot.
# Use the same species order and the same colors in every panel.
```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data
penguins = pd.read_csv("penguins.csv")

# Consistent order and colors
SPECIES = ["Adelie", "Chinstrap", "Gentoo"]
SPECIES_COLORS = {
    "Adelie": "#4C72B0",
    "Chinstrap": "#DD8452",
    "Gentoo": "#55A868"
}

# Create 2x2 figure
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Step histogram with hue
sns.histplot(
    data=penguins,
    x="flipper_length_mm",
    hue="species",
    hue_order=SPECIES,
    palette=SPECIES_COLORS,
    element="step",
    stat="density",
    common_norm=False,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Flipper Length Distribution (Step Histogram)")

# 2. KDE with hue
sns.kdeplot(
    data=penguins,
    x="flipper_length_mm",
    hue="species",
    hue_order=SPECIES,
    palette=SPECIES_COLORS,
    common_norm=False,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Flipper Length Distribution (KDE)")

# 3. Box plot
sns.boxplot(
    data=penguins,
    x="species",
    y="flipper_length_mm",
    order=SPECIES,
    palette=SPECIES_COLORS,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Flipper Length by Species (Box Plot)")
axes[1, 0].set_xlabel("Species")
axes[1, 0].set_ylabel("Flipper Length (mm)")

# 4. Violin plot
sns.violinplot(
    data=penguins,
    x="species",
    y="flipper_length_mm",
    order=SPECIES,
    palette=SPECIES_COLORS,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Flipper Length by Species (Violin Plot)")
axes[1, 1].set_xlabel("Species")
axes[1, 1].set_ylabel("Flipper Length (mm)")

fig.suptitle(
    "Penguin Flipper Length Distributions by Species",
    fontsize=16
)
fig.tight_layout()

plt.show()
### 🤖 Explain It

In your own words: the overall penguin body-mass histogram looked like one lumpy pile, and its skew was only 0.47. What did coloring by species reveal, and why couldn't the skew statistic reveal it?
`Answer: The overall body-mass histogram looked like one lumpy distribution with a skew of only 0.47 because it combined all three penguin species into a single dataset. When the histogram was colored by species, it revealed that the "lumps" were actually separate distributions for Adelie, Chinstrap, and Gentoo penguins, each with different typical body masses. The skew statistic could not reveal this because skewness summarizes only the overall asymmetry of the combined distribution and does not show the presence of multiple groups or peaks.`
---

## 🔍 Section 4: Seaborn Relationships and Categories

7. What do the error bars on a default `sns.barplot()` mean? How would `errorbar='sd'` change them?  
   `Answer:` Default barplot() error bars show a confidence interval for the mean. Setting errorbar='sd' changes them to show ±1 standard deviation, indicating the spread of the observations within each group.

8. Why should you color a scatter plot by group before adding a trend line?  
   `Answer:` Coloring by group lets you see whether different groups follow different patterns. Without grouping, an overall trend line can hide or even reverse the relationships that exist within each group. For example, in the penguins data:

A single trend line through all species shows a negative relationship between bill depth and flipper length.
When points are colored by species, each species has its own positive trend.

This is an example of Simpson's paradox, where the overall trend differs from the trends within the groups.

---

### ✏️ Task: Reveal the Paradox

```python
# Using penguins.csv:
# 1. Draw one regplot of bill_length_mm vs. bill_depth_mm for all penguins.
# 2. Draw one regplot per species on a second panel, with r in each label.
# 3. Give each panel a title that states what it shows.
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
penguins = pd.read_csv("penguins.csv")

# Species order and colors
SPECIES = ["Adelie", "Chinstrap", "Gentoo"]
SPECIES_COLORS = {
    "Adelie": "#4C72B0",
    "Chinstrap": "#DD8452",
    "Gentoo": "#55A868"
}

# Create figure
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1. Overall regplot
sns.regplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    scatter_kws={"alpha": 0.6},
    line_kws={"color": "red"},
    ax=axes[0]
)

axes[0].set_title(
    "All Penguins: Bill Length and Bill Depth Show the Overall Relationship"
)
axes[0].set_xlabel("Bill Length (mm)")
axes[0].set_ylabel("Bill Depth (mm)")

# 2. One regplot per species
for species in SPECIES:
    subset = penguins[penguins["species"] == species]

    r = subset["bill_length_mm"].corr(
        subset["bill_depth_mm"]
    )

    sns.regplot(
        data=subset,
        x="bill_length_mm",
        y="bill_depth_mm",
        color=SPECIES_COLORS[species],
        scatter_kws={"alpha": 0.5},
        label=f"{species} (r={r:.2f})",
        ax=axes[1]
    )

axes[1].set_title(
    "Within Species: Bill Length and Bill Depth Relationship by Species"
)
axes[1].set_xlabel("Bill Length (mm)")
axes[1].set_ylabel("Bill Depth (mm)")
axes[1].legend(title="Species")

fig.tight_layout()
plt.show()
### 🤖 Explain It

In your own words: explain Simpson's paradox to someone who has never heard of it, using your chart from the task above.
`Answer: Simpson's paradox happens when a relationship that appears in the combined data changes or even reverses when the data are split into meaningful groups.

In my chart, the left panel shows all penguins together and suggests one overall relationship between bill length and bill depth. However, when I separated the data by species in the right panel, each species showed its own trend. The overall trend was being influenced by differences between species, not just the relationship within each species.

Because the species have different average bill sizes, combining them hides the true within-species patterns. Looking only at the combined data could lead to the wrong conclusion.`
---

## 🗣️ Section 5: Choosing and Telling

9. Name three things a bar chart's y-axis can do to mislead a reader.  
   `Answer:` A bar chart's y-axis can mislead by not starting at zero, using inconsistent scales between charts, or using misleading tick marks/intervals that distort the visual comparison.
10. What's the difference between a descriptive title and a finding title? Write one of each for the same chart.  
    `Answer:` A descriptive title describes the chart's contents such as "Survival Rate by Passenger Class" and a finding title states the main result or takeaway from the chart like "First-Class Passengers Survived at Much Higher Rates Than Third-Class Passengers".

---

### ✏️ Task: Makeover

```python
# Start with: titanic.groupby('Embarked')['Fare'].mean().plot.bar()
# Redesign it with the notebook 05 checklist: the right statistic for skewed data,
# readable port names, sorted bars, a highlight color, bar labels, and a finding title.
# Save the before and after versions.
```

import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv('titanic.csv')
# -------------------
# BEFORE
# -------------------
ax = titanic.groupby('Embarked')['Fare'].mean().plot.bar(
    figsize=(6, 4),
    title='Mean Fare by Embarkation Port'
)

ax.set_xlabel('Embarked')
ax.set_ylabel('Mean Fare ($)')

plt.tight_layout()
plt.savefig('fare_by_embarked_before.png', dpi=300)
plt.close()

# -------------------
# AFTER
# -------------------

# Use median instead of mean because Fare is strongly right-skewed
fare_med = (
    titanic.groupby('Embarked')['Fare']
    .median()
)

# Readable names
port_names = {
    'C': 'Cherbourg',
    'Q': 'Queenstown',
    'S': 'Southampton'
}

fare_med.index = fare_med.index.map(port_names)

# Sort bars by value
fare_med = fare_med.sort_values()

# Highlight the highest port
colors = ['lightgray'] * len(fare_med)
colors[-1] = 'steelblue'

fig, ax = plt.subplots(figsize=(7, 5))

# Bar labels

bars = ax.bar(
    fare_med.index,
    fare_med.values,
    color=colors
)

ax.bar_label(
    bars,
    fmt='$%.2f',
    padding=3
)



# Finding title
ax.set_title(
    'Passengers Embarking at Cherbourg Paid the Highest Typical Fare'
)

ax.set_xlabel('Embarkation Port')
ax.set_ylabel('Median Fare ($)')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout()

fig.savefig(
    'fare_by_embarked_after.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()
### 🤖 Explain It

In your own words: what's the difference between a chart made for exploration and a chart made for communication? Why do they need different amounts of polish?
`Answer: A chart made for exploration helps the analyst understand the data, look for patterns, identify outliers, test ideas, and check assumptions. It doesn't need to be highly polished because it is mainly for the analyst's own use.

A chart made for communication is designed to clearly explain a finding to other people, such as readers of a report or presentation. It should be polished, with clear labels, titles, annotations, colors, and formatting that guide the audience to the main takeaway.`
---

## 🧾 Submit Checklist

- [X] I built a multi-panel Matplotlib figure with `fig, ax`, shared axes, and `fig.savefig()`.
- [X] I used a log scale, a reference line, and a tick formatter where they helped.
- [x] I turned a pandas summary table into a chart, and reshaped data between wide and long.
- [X] I compared distributions across groups fairly (`common_norm=False`, shared axes, sample sizes).
- [X] I showed a relationship with a scatter plot colored by group, and explained my error bars.
- [X] I redesigned a default chart using the checklist, with a finding title.
- [X] I completed the "Explain It" prompts in my own words.
