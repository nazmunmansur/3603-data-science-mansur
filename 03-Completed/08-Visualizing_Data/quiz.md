# 📝 Quiz: 08 - Visualizing Data

36 questions covering object-oriented Matplotlib, plotting with pandas, Seaborn distributions, Seaborn relationships and categories, and choosing and designing charts. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Matplotlib, Object-Oriented

**1.** (Short Answer) In `fig, ax = plt.subplots()`, what's the difference between `fig` and `ax`?
`Answer: fig (Figure) = the entire canvas or window that holds everything.
ax (Axes) = a single plotting area inside the figure, where you actually draw charts.`
**2.** (Short Answer) Why does the object-oriented style scale better than `plt.title()`/`plt.xlabel()` calls when a figure has several charts?
`Answer: The object-oriented style scales better because each chart has its own Axes (ax) object, so you can control titles, labels, legends, and formatting for each plot independently. With plt.title() and plt.xlabel(), Matplotlib only modifies the current axes, which becomes confusing when a figure contains multiple charts.`
**3.** (Code Tracing) How many axes does this create, and how do you reach the bottom-right one?
```python
fig, axes = plt.subplots(2, 3)
```
`Answer: plt.subplots(2, 3) creates 6 Axes objects arranged in 2 rows and 3 columns.`
**4.** (Short Answer) What does `sharey=True` do, and why does it matter when comparing panels?
`Answer: sharey=True makes all panels use the same y-axis scale. This matters because it allows you to compare values across panels fairly. Without it, each panel could have a different y-axis range, making differences look larger or smaller than they really are.`
**5.** (Short Answer) When is a log-scale axis a good idea? What value can't it show?
`Answer: A log-scale axis is useful when data spans a very large range of values or grows exponentially, making it easier to see patterns that would be compressed on a regular scale. It cannot show zero (0) because the logarithm of 0 is undefined. It also cannot show negative values. For example, stock prices, population growth, and income distributions are often plotted on a log scale.`
**6.** (Multiple Choice) Which formatter displays `0.25` on an axis as `25%`?
A) `StrMethodFormatter('{x:.0%}')`  B) `PercentFormatter(xmax=1)`  C) `PercentFormatter(xmax=100)`  D) `ax.set(percent=True)`
`Answer: B) `PercentFormatter(xmax=1)` `
**7.** (Short Answer) Why should you call `fig.savefig()` before `plt.show()`, and why `plt.close(fig)` inside a loop?
`Answer: Call fig.savefig() before plt.show() because show() may clear or close the figure depending on the environment. Saving first ensures the image is written correctly to disk.
Call plt.close(fig) inside a loop to free memory and prevent too many open figures from accumulating when creating many plots.`
**8.** (Short Answer) In `ax.annotate('Peak', xy=(5, 10), xytext=(7, 12), arrowprops=...)`, what do `xy` and `xytext` each mean?
`Answer: xy gives the coordinates of the point being labeled, while xytext gives the coordinates where the annotation text is placed.`
---

## Section B — Plotting with Pandas

**9.** (Short Answer) When pandas plots a DataFrame, what becomes the x-axis, and what becomes each line or set of bars?
`Answer: The DataFrame's index becomes the x-axis, and each column is plotted as a separate line or set of bars. This allows multiple variables to be compared on the same chart.`
**10.** (Code Tracing) What kind of chart does this draw, and what are the bar labels?
```python
titanic['Embarked'].value_counts().plot.barh()
```
`Answer: This draws a horizontal bar chart (barh) showing the count of passengers from each Embarked port. The bar labels are the embarkation codes from the Series index: C, Q, and S (unless they were mapped to full names beforehand).`
**11.** (Short Answer) You plot a `pivot_table` with classes as the index and sexes as the columns. How do you switch the chart to group by sex instead?
`Answer: Use .T to transpose the pivot table (or swap the index and columns when creating it). This makes sex the x-axis grouping variable instead of class.`
**12.** (Short Answer) What does a 100% stacked bar chart show, and which `crosstab` argument produces the right table for it?
`Answer: A 100% stacked bar chart shows the relative percentages (composition) of subgroups within each category, with each bar totaling 100%. Use normalize='index' in pd.crosstab() to create the appropriate table. `
**13.** (Short Answer) What's the difference between wide and long data? Which does pandas `.plot` expect, and which does Seaborn expect?
`Answer: Wide data stores each variable in a separate column, while long data stores variables and values in separate columns, often with multiple rows per category. Pandas .plot() generally expects wide-form data, whereas Seaborn generally expects long-form (tidy) data.`
**14.** (Short Answer) Should you sort the bars of an ordinal category (like ticket class) by value? Why or why not?
`Answer: No. For an ordinal category such as ticket class (1st, 2nd, 3rd), you should keep the bars in their natural order rather than sorting by value. Sorting by value can hide the meaningful sequence of the categories and may make the chart misleading. The order itself carries information, so preserving it helps the reader interpret the data correctly.`
---

## Section C — Seaborn: Distributions

**15.** (Short Answer) What's the difference between an axes-level and a figure-level Seaborn function? Give one example of each.
`Answer: Axes-level functions draw on a single Axes (ax) object. They're used when you want precise control over where a plot goes in a multi-panel figure. Examle of Axes-level: sns.scatterplot(), sns.histplot(), sns.boxplot()
Figure-level functions create and manage an entire Figure, often with multiple subplots automatically. Example of Figure-level are sns.relplot(), sns.catplot(), sns.displot(), sns.lmplot().`
**16.** (Short Answer) What does `hue='species'` do in `sns.histplot()`?
`Answer: hue='species' splits the histogram by species and gives each species a different color, allowing you to compare their distributions on the same plot.`
**17.** (Multiple Choice) Two groups have 500 and 50 rows. To compare the **shapes** of their distributions, use:
A) `stat='count'`  B) `multiple='stack'`  C) `stat='percent', common_norm=False`  D) `binwidth=1`
`Answer: C) `stat='percent', common_norm=False`.`
**18.** (Short Answer) Explain each part of a box plot: the box, the line inside it, the whiskers, and the dots.
`Answer: Box: Extends from the 1st quartile (Q1, 25th percentile) to the 3rd quartile (Q3, 75th percentile), showing the middle 50% of the data.
Line inside the box: The median (50th percentile).
Whiskers: Extend to the most extreme values that are not considered outliers, typically up to 1.5 × IQR beyond Q1 and Q3.
Dots (points beyond the whiskers): Outliers, values more than 1.5 × IQR below Q1 or above Q3.`
**19.** (Short Answer) Name one thing a violin plot shows that a box plot hides, and one thing a strip plot shows that a violin hides.
`Answer: A violin plot shows the shape and density of the distribution (for example, multiple peaks or clusters) that a box plot hides and might reveal that a group has two peaks (bimodal). A strip plot shows the individual data points, letting you see exact values, sample size, and gaps that a violin plot hides and might show that there are only 10 observations and exactly where each one falls.`
**20.** (Short Answer) How do you read a group's median from an ECDF plot?
`Answer: On an ECDF (Empirical Cumulative Distribution Function) plot, the median is the x-value where the ECDF reaches 0.5 (50%). Find 0.5 on the y-axis, move across to the curve, and then down to the x-axis to read the median value.`
**21.** (True/False) A KDE curve always stays within the actual range of the data.
`Answer: False`
**22.** (Short Answer) Why does `showfliers=False` make sense when you draw a strip plot on top of a box plot?
`Answer: showfliers=False hides the outlier points in the box plot because the overlaid strip plot already shows every individual data point, including the outliers. This prevents the outliers from being plotted twice and makes the chart less cluttered.`
---

## Section D — Seaborn: Relationships and Categories

**23.** (Short Answer) Name two ways to reduce overplotting in a scatter plot.
`Answer: Transparency (alpha) makes dense areas appear darker, revealing where many points overlap. A log scale can spread out crowded values (such as low fares), making patterns easier to see when the data are highly skewed.`
**24.** (Short Answer) In the penguins data, one `regplot` line through all the points slopes down, but one line per species slopes up. What's this called, and what's the lesson for fitting trend lines?
`Answeer: This is Simpson's paradox: when the overall relationship in the combined data differs from, or even reverses, the relationship within the individual groups. In the penguins data, the trend line for all species combined slopes downward, but the trend line within each species slopes upward. The lesson is that you should check for important grouping variables (such as species) before interpreting a single overall trend line, because aggregate data can be misleading.`
**25.** (Short Answer) Why did the four Anscombe datasets get identical lines from `lmplot`?
`Answer: The four Anscombe datasets have nearly identical summary statistics, including the same mean, variance, correlation, and linear regression equation. Because lmplot fits the same least-squares regression line from those statistics, it produces identical lines for all four datasets. However, the actual point patterns are very different.`
**26.** (Short Answer) What's the difference between `countplot` and `barplot`?
`Answer: countplot shows the number of observations in each category.
barplot shows a summary statistic (by default, the mean) for each category.`
**27.** (Multiple Choice) `sns.barplot(..., errorbar='sd')` draws error bars showing:
A) the 95% confidence interval  B) the standard error  C) one standard deviation of the individual values  D) the IQR
`Answer: C) one standard deviation of the individual values`
**28.** (Short Answer) What does Seaborn's default error bar on a `barplot` represent?
`Answer: By default, Seaborn's barplot() shows a 95% confidence interval (CI) for the mean, not the spread of the individual data values.`
**29.** (Short Answer) What does a `pointplot` with crossing or diverging lines tell you?
`Answer: Crossing or diverging lines in a pointplot indicate a possible interaction between variables. The effect of one variable is different for different groups, so the overall trend may not apply equally to all categories.`
**30.** (Short Answer) Should a correlation heatmap use a diverging or a sequential color map? What about a heatmap of survival rates? Why?
`Answer A correlation heatmap should use a diverging colormap because correlations have a meaningful center at 0 and can be both positive and negative. The colors can show negative correlations on one side, positive correlations on the other, and 0 as a neutral color.

A survival-rate heatmap should use a sequential colormap because survival rates go from low to high (for example, 0% to 100%) and do not have negative values. Darker or more intense colors represent higher rates.`
---

## Section E — Choosing and Telling

**31.** (Short Answer) Why must bar charts start at zero, when line charts don't have to?
`Answer: Bar charts should start at zero because viewers compare bar lengths to judge values. A truncated axis can distort those comparisons. Line charts can use a non-zero axis because they are used to show trends and changes rather than compare lengths directly.`
**32.** (Short Answer) Name the chart you'd choose for each: (a) the distribution of one numeric column, (b) the mix of categories within each group, (c) the relationship between two numeric columns.
`Answer: (a) Histogram for the distribution of one numeric column.
 (b) 100% stacked bar chart for the mix of categories within each group.
 (c) Scatter plot for the relationship between two numeric columns.`
**33.** (Short Answer) What's a palette dictionary, and why use one across a whole report?
`Answer: Using the same palette dictionary throughout a report ensures that a category always has the same color in every chart. This makes the visualizations easier to read and prevents confusion that could occur if the same category appears in different colors across plots.`
**34.** (Short Answer) Rewrite this descriptive title as a finding title: "Mean Body Mass by Species."
`answer: Gentoo Penguins Have the Highest Mean Body Mass, Followed by Chinstrap and Adelie`
**35.** (True/False) Every bar in a bar chart should have its own distinct color.
`Answer: False`
**36.** (Short Answer) Give two reasons to look at a chart **and** the matching numbers, rather than just one of them.
`Answer: Charts reveal patterns such as outliers, clusters, skewness, bimodal distributions, and Simpson's paradox that may not be obvious from the numbers alone.
Numbers provide exact values (means, medians, percentages, correlations, sample sizes), allowing you to quantify what you see in the chart and verify your conclusions. 
So using both reduces the risk of drawing misleading conclusions from either one alone.`