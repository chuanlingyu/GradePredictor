import pandas as pd
import numpy as np


df = pd.read_csv("data/raw/student_performance_updated_1000.csv")

df = df.dropna()

df = df.drop(columns=["StudentID", "Name"])

df["Attendance"] = df[["AttendanceRate", "Attendance (%)"]].mean(axis=1)
df = df.drop(columns=["AttendanceRate", "Attendance (%)"])

df["Online Classes Taken"] = df["Online Classes Taken"].astype(int)

df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

df["ParentalSupport"] = df["ParentalSupport"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

df.to_csv("data/processed/cleaned_students.csv", index=False)