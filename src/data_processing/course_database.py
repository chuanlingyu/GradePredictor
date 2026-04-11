import pandas as pd

df = pd.read_csv("data/raw/uiuc-gpa-dataset.csv")

df_new = df.iloc[:, [3, 4, -1]]

df_new.columns = ["subject", "number", "professor"]

df_new["professor"] = df_new["professor"].str.replace('"', '')

df_new.to_csv("data/processed/cleaned_course_database.csv", index = False)