import pandas as pd
import numpy as np


df = pd.read_csv("data/raw/student_performance_updated_1000.csv")

df = df.dropna()

df = df[df["StudyHoursPerWeek"] >= 0]
df = df[df["AttendanceRate"] <= 100]



to_drop = ["Name","Gender","ParentalSupport","Online Classes Taken"]
df = df.drop(columns=to_drop)

df.to_csv("data/processed/cleaned_students.csv", index=False)