import pandas as pd

df = pd.read_csv("data/raw/student_lifestyle_performance_dataset.csv")
df = df.drop(columns=["Residence"])
df = df.drop(columns=["Internal_Marks"])
df = df.drop(columns=["Diet_Type"])
df = df.drop(columns=["Stress_Level_1_to_10"])

df["GPA"] = ((df["CGPA"] / 10) * 4).round(2)
df = df.drop(columns=["CGPA"])

df.to_csv("data/processed/cleaned_students.csv", index = False)