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
df = df.drop(columns=["GPA_Points"])

instructor_avg = df.groupby("Primary Instructor")["Average_GPA"].mean().round(2)

df["Instructor_Avg_GPA"] = df["Primary Instructor"].map(instructor_avg)

college_map = {
    "Engineering": ["CS","ECE","ME","CEE","TAM","AE","MSE","BIOE","CHBE","IE","NPRE","SE"],
    "LAS": ["MATH","STAT","PHYS","CHEM","ECON","PSYC","SOC","HIST","ENGL","PHIL","ANTH","LING","GEOG","GEOL","ATMS","ASTR","MCB","EPS"],
    "Business": ["ACCY","BADM","FIN","BUS"],
    "ACES": ["ABE","ACES","ANSC","CPSC","NRES","HORT","NUTR","FSHN","ALEC","AGCM"],
    "FAA": ["ARCH","ART","ARTD","ARTE","ARTF","ARTH","ARTJ","ARTS","MUS","MUSC","THEA","DANC","LA"],
    "Media": ["ADV","JOUR","MDIA","CMN"],
    "Education": ["CI","EDUC","EPSY","SPED"],
    "Languages": ["SPAN","FR","GER","CHIN","JAPN","KOR","ITAL","ARAB","RUSS"]
}

def map_college(subject):
    for college, subjects in college_map.items():
        if subject in subjects:
            return college
    return "Other"

df["College"] = df["Subject"].apply(map_college)

cols_to_drop = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F", "W", "Students", "Term", "Year", "YearTerm", "Course Title", "Sched Type", "Primary Instructor", "Course", "Subject"]

df = df.drop(columns=cols_to_drop)

df = pd.get_dummies(df, columns=["College"], drop_first=True)

Q1 = df['Average_GPA'].quantile(0.25)
Q3 = df['Average_GPA'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Average_GPA'] >= lower_bound) & (df['Average_GPA'] <= upper_bound)]

# mean = df['Average_GPA'].mean()
# std = df['Average_GPA'].std()
# df['']

df.to_csv("data/processed/cleaned_grades.csv", index = False)