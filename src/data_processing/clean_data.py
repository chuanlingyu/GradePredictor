import pandas as pd

df = pd.read_csv('data/raw/uiuc-gpa-dataset.csv')
df = df.dropna(subset=['Primary Instructor'])
df["Course"] = df["Subject"] + " " + df["Number"].astype(str)
df["GPA_Points"] = (
    (df["A+"] *  4.0) +
    (df["A"] * 4.0) +
    (df["A-"] * 3.7) +
    (df["B+"] * 3.3) +
    (df["B"] * 3.0) +
    (df["B-"] * 2.7) +
    (df["C+"] * 2.3) +
    (df["C"] * 2.0) +
    (df["C-"] * 1.7) +
    (df["D+"] * 1.3) +
    (df["D"] * 1.0) +
    (df["D-"] * 0.7) +
    (df["F"] * 0.0)
).round(2)

df["Average_GPA"] = (df["GPA_Points"] / df["Students"]).round(2)

df.to_csv("data/processed/cleaned_grades.csv", index = False)