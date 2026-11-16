# 📝 Quiz: 07 - Describing Data

36 questions covering types of data, center and spread, shape and outliers, comparing groups, and relationships and correlation. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Types of Data

**1.** (Short Answer) What's the difference between a column's **dtype** and its **measurement scale**?
`Answer: Dtype is how the data is stored in pandas (e.g., int64, float64, object, category, bool).
 Measurement scale describes what the values mean and what kinds of analysis are appropriate (e.g., nominal, ordinal, interval, ratio).`
**2.** (Multiple Choice) Titanic's `Pclass` is stored as `1`, `2`, `3`. Its measurement scale is:
A) Nominal  B) Ordinal  C) Interval  D) Ratio
Answer: B) Ordinal
**3.** (Multiple Choice) Which scale has a true zero that means "none of it"?
A) Nominal  B) Ordinal  C) Interval  D) Ratio
Answer: D) Ratio
**4.** (True/False) Temperature in °C is ratio data, because 20°C is twice 10°C.
Answer: false
**5.** (Short Answer) Is "number of siblings aboard" discrete or continuous? How can you tell?
`Answer: Discrete. The number of siblings aboard can only take whole-number counts (0, 1, 2, 3, ...). You cannot have 2.5 siblings aboard, so the values are countable and separate rather than continuous.`
**6.** (Code Tracing) What prints?
```python
s = pd.Series([True, False, True, True])
print(s.mean())
```
`Answer: 0.75`
**7.** (Short Answer) Why is `titanic['PassengerId'].mean()` meaningless, even though pandas computes it without complaint?
`Answer: This relates more to the fact that PassengerId is an identifier (nominal-like data encoded as numbers) than to it being ordinal. The numbers are labels, not ranks or measurements. titanic['PassengerId'].mean() is meaningless because PassengerId is just an ID number used to identify passengers. Although it is stored as a numeric dtype, averaging ID values does not describe anything about the passengers. The numbers have no quantitative meaning, so the mean is not interpretable.`
**8.** (Short Answer) What does `ordered=True` in `pd.CategoricalDtype([...], ordered=True)` let you do that a plain `str` column can't?
`Answer: ordered=True tells pandas that the categories have a meaningful order. This allows you to compare and sort values (, >, sort_values(), min(), max()) according to that order. A plain string column can store the labels, but it doesn't know their intended ranking.`
---

## Section B — Center and Spread

**9.** (Short Answer) Which is more robust to outliers, the mean or the median? Why?
`Answer: The median is more robust to outliers because it depends only on the middle value(s) after sorting the data, not on the magnitude of extreme values. In contrast, the mean uses every value, so a very large or very small outlier can pull it up or down substantially.`
**10.** (Code Tracing) What prints?
```python
s = pd.Series([2, 4, 4, 6, 100])
print(s.median(), s.mode()[0])
```
`Answer: 4.0 4`
**11.** (Short Answer) A column's mean is much larger than its median. What does that suggest?
`Answer: If a column's mean is much larger than its median, the distribution is likely right-skewed (positively skewed). This often suggests there are a few very large values or outliers pulling the mean upward.`
**12.** (Multiple Choice) `pd.Series(data).std()` and `np.std(data)` give slightly different answers because:
A) NumPy rounds  B) pandas skips NaN  C) they use different default `ddof`  D) one is variance
`Answer: C) they use different default `ddof` `
**13.** (Short Answer) What's the IQR, and how do you compute it in pandas?
`Answer: The IQR (Interquartile Range) is the difference between the third quartile (Q3, 75th percentile) and the first quartile (Q1, 25th percentile). It measures the spread of the middle 50% of the data.`
**14.** (Short Answer) In `.describe()`, a column's `count` is 714 but the DataFrame has 891 rows. What does that tell you?
`Answer: The column contains missing values. The count in .describe() reports only non-missing values, so if the DataFrame has 891 rows but the column's count is 714, then 177 entries are missing (NaN).`
**15.** (Short Answer) You fill 177 missing ages with the median age. What happens to the standard deviation, and why?
`Answer: The standard deviation will generally decrease because median imputation adds many values at the center and artificially reduces variability.`
**16.** (Short Answer) Which spread statistic pairs naturally with the median, and which with the mean?
`Answer: The median is resistant to outliers, and the IQR is also resistant to outliers because it uses only the middle 50% of the data.
The mean is affected by outliers, and the standard deviation is also affected by outliers because both use every value. `
---

## Section C — Shape and Outliers

**17.** (Multiple Choice) A column with `.skew()` of 4.8 is:
A) roughly symmetric  B) strongly left-skewed  C) strongly right-skewed  D) heavy-tailed but symmetric
`Answer: C) strongly right-skewed`
**18.** (Short Answer) Write the formulas for the lower and upper fences of the 1.5 × IQR rule.
`Answer: Lower fence: Q1−1.5×IQR
Upper fence: Q3+1.5×IQR where IQR=Q3−Q1.`
**19.** (Short Answer) On Titanic fares, the IQR rule flags 116 values but the |z| > 3 rule flags only 20. Why are z-scores less sensitive on a skewed column?
`Answer: Titanic fares are strongly right-skewed. Extreme high fares inflate the mean and standard deviation, which reduces many z-scores and causes the ∣z∣>3|z| > 3∣z∣>3 rule to miss outliers. The IQR rule is more sensitive in this situation because it is based on quartiles and is less influenced by extreme values. In other words, IQR rule is more robust because it uses Q1, Q3, and the IQR, which are much less affected by extreme fares. That's why it flags 116 fare values while the ∣z∣>3|z| > 3∣z∣>3 rule flags only 20.`

**20.** (True/False) Any value flagged as an outlier should be removed before analysis.
`Answer: False`
**21.** (Short Answer) Name two things you can do with a real-but-extreme value instead of deleting it.
`Answer: Two good alternatives to deleting a real but extreme value are:

1. Keep it and use robust statistics, such as the median and IQR, which are less affected by extreme values.

2. Analyze it separately or transform the data, for example by using a log transformation on a highly skewed variable like Titanic Fare, or by reporting results with and without the extreme values to see how much they influence the conclusions.`
**22.** (Short Answer) Why can a value be an outlier within its group but not in the whole dataset (or the other way around)?
`Answer: A value can be an outlier within its group but not in the whole dataset because different groups can have different centers and spreads (distributions). A value that is unusual for one group may be normal when compared to all observations combined. Conversely, a value may appear normal within its group but become an outlier in the full dataset if its entire group is far from the others.
---

## Section D — Comparing Groups

**23.** (Short Answer) More 3rd-class passengers survived than 2nd-class passengers, but 3rd class had the lower survival rate. How can both be true?
`Answer: 3rd class had a larger number of passengers, so it could have more survivors in total while still having a lower percentage of passengers survive.`
**24.** (Code Tracing) What does this compute?
```python
titanic.groupby('Sex')['Survived'].mean()
```
`Answer: It computes the survival rate (proportion survived) for males and females.`
**25.** (Multiple Choice) In `pd.crosstab(df['class'], df['Sex'], normalize='index')`, what adds up to 100%?
A) each row  B) each column  C) the whole table  D) nothing; it's counts
`Answer: A) each row `
**26.** (Short Answer) What's the difference between what `pd.crosstab()` and `pivot_table()` compute?
`Answer: pd.crosstab() is mainly used to compute counts or frequencies for combinations of categorical variables (and can optionally show row/column percentages with normalize=).
pivot_table() is more flexible and computes summary statistics (mean, median, count, sum, etc.) using an aggregation function specified by aggfunc.`
**27.** (Short Answer) Why should a group summary always include the group's size?
`Answer: A group summary should include the group's size (n) because summary statistics can be misleading without knowing how many observations they are based on. Results from a group with 10 observations are generally less reliable than results from a group with 1,000 observations. And helps judge the reliability and interpretability of the results.`
**28.** (Short Answer) Cherbourg passengers survived at a higher rate than other ports. Explain how ticket class could be a **confounder** here.
`Answer: Ticket class could be a confounder because passengers embarking at Cherbourg were more likely to be First Class passengers, and First Class passengers had higher survival rates. As a result, Cherbourg's higher survival rate may be partly due to its mix of ticket classes rather than the embarkation port itself causing better survival.`
**29.** (Short Answer) What does `observed=True` do in a `groupby` on a categorical column?
`Answer: observed=True tells groupby() to include only the category levels that actually appear in the data.`
---

## Section E — Relationships and Correlation

**30.** (Short Answer) Why is covariance hard to interpret on its own, and how does correlation fix that?
`Answer: Covariance is hard to interpret on its own because its value depends on the units and scales of the variables. For example, changing a variable from dollars to cents changes the covariance. Covariance is unit-dependent and has no fixed scale, so its magnitude is difficult to interpret. Correlation fixes this by standardizing the relationship to a scale from -1 to 1, making it easier to interpret and compare across different variables.`
**31.** (Multiple Choice) r = −0.85 means:
A) a weak negative linear relationship  B) a strong negative linear relationship  C) 85% of y is caused by x  D) no relationship
`Answer: B) a strong negative linear relationship`
**32.** (Short Answer) Give two situations where Spearman is a better choice than Pearson.
`Answer: Spearman is preferred when (1) the relationship is monotonic but not linear and (2) the data contain outliers or strong skewness.`
**33.** (True/False) If r = 0, the two columns have no relationship at all.
`Answer: False`
**34.** (Short Answer) Name three explanations for a correlation besides "A causes B."
`Answer: Confounding variables, reverse causation, and coincidence/random chance are three common explanations for a correlation other than "A causes B."`
**35.** (Short Answer) What is Anscombe's quartet, and what lesson does it teach?
`Answer: Anscombe's quartet shows that datasets can have the same statistics but completely different shapes and relationships. The lesson is to plot your data and not rely only on numerical summaries.`
**36.** (Short Answer) In the penguins data, bill length and depth correlate at −0.24 overall but +0.39 to +0.65 within each species. What's this called, and what causes it here?

`Aswer: Within each species, bill length and bill depth are positively correlated, but when all species are combined, differences between species reverse the overall relationship, producing a negative correlation. because Species is the confounding variable.`