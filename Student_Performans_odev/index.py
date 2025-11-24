import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# 1
df = pd.read_csv("./data/StudentsPerformance.csv")
# print(df.head())

# 2
# Number of women and men 
# gender = df["gender"].value_counts()
# print(gender)

# 3
#Let's look at the number of women and men using a histografm graph.
# plot() fonksiyonu grafiği oluşturur
plt.figure(figsize=(4,10))
gender = df["gender"].value_counts().plot(kind="bar")
plt.title("Number Of Women and Man")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

#4
#Let's see how many different groups there are in the race/ethnicity columns
race_ethnicity_count = df["race/ethnicity"].nunique()
print(race_ethnicity_count)

#5
#Let's visualize what we found above
plt.figure(figsize=(18,5))
race = df["race/ethnicity"].value_counts()
race.plot(kind="bar")
plt.title("Race / Ethnicity Group Count")
plt.xlabel("R/E")
plt.ylabel("Count")
plt.show()

#6
# Find the unique values in the #parental level of education column
education = df["parental level of education"].unique()
print(education)

#7 
# Find the unique value in the #lunch column
lunch = df["lunch"].unique()
print(lunch)

#8
#Find out how many people there are in each type(lunch)
lunch_count = df["lunch"].value_counts()
print(lunch_count)

#9
#Find the avarage math score , reading score,and writing score values for the values in the #gender column.
gender_means = df.groupby("gender")[["math score","reading score", "writing score"]].mean()
print(gender_means)

#9
#Find the avarage math score, reading score, writing score values of the values in the #race/ethnicity
race_score = df.groupby("race/ethnicity")[["math score","reading score", "writing score"]].mean()
print(race_score)

#10
#Find the avarage math score, reading score, writing score values of the values in the #education column
education_score = df.groupby("parental level of education")[["math score","reading score","writing score"]].mean()
print(education_score)

#11
#Find the avarage math score,reading score, writing score value of the values in the #lunch column
lunch_score = df.groupby("lunch")[["math score", "writing score","reading score"]].mean()
print(lunch_score)

#12
# Find the avarage math score, writing score, reading score values of the values in the test preparation course column
course_score = df.groupby("test preparation course")[["math score","writing score","reading score"]].mean()
print(course_score)