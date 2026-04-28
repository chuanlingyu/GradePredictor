import pandas as pd

df = pd.read_csv("data/processed/cleaned_course_database.csv")
    
df['Subject'] = df['Subject'].astype(str).str.strip().str.upper()
df['Number'] = df['Number'].astype(str).str.strip()
df['Primary Instructor'] = df['Primary Instructor'].astype(str).str.strip().str.upper()

course_dict = {}
course_average_dict = {}

for _, row in df.iterrows():
    key = (row['Subject'], row['Number'], row['Primary Instructor'])

    course_dict[key] = {
        "Average_GPA": row["Average_GPA"],
        "Instructor_Avg_GPA": row["Instructor_Avg_GPA"],
        "College_ACES": row["College_ACES"],
        "College_Business": row["College_Business"],
        "College_Education": row["College_Education"],
        "College_Engineering": row["College_Engineering"],
        "College_FAA": row["College_FAA"],
        "College_LAS": row["College_LAS"],
        "College_Languages": row["College_Languages"],
        "College_Media": row["College_Media"],
        "College_Other": row["College_Other"],
    }

for (subject, number), group in df.groupby(["Subject", "Number"]):
    course_average_dict[(subject, number)] = {
        "Average_GPA": group["Average_GPA"].mean(),
        "Instructor_Avg_GPA": group["Instructor_Avg_GPA"].mean(),
        "College_ACES": group["College_ACES"].mode().iloc[0],
        "College_Business": group["College_Business"].mode().iloc[0],
        "College_Education": group["College_Education"].mode().iloc[0],
        "College_Engineering": group["College_Engineering"].mode().iloc[0],
        "College_FAA": group["College_FAA"].mode().iloc[0],
        "College_LAS": group["College_LAS"].mode().iloc[0],
        "College_Languages": group["College_Languages"].mode().iloc[0],
        "College_Media": group["College_Media"].mode().iloc[0],
        "College_Other": group["College_Other"].mode().iloc[0],
    }

# def check_exist(subject, number, professor="No input") -> tuple[bool, str]:
#     if subject not in course_dict:
#         return True, "This subject does not exist. Check the subject abbreviation carefully."
    
#     if number not in course_dict[subject]:
#         return True, "The course does not exist for the subject. Check the course number carefully."
    
#     if (not professor == "No input") and (professor not in course_dict[subject][number]):
#         return True, "This professor does not exist or didn't teach this course before. Check the course number carefully"
    
#     return False, ''

def extract_info(subject, number, instructor):

    subject = subject.strip().upper()
    number = str(number).strip()
    instructor = str(instructor or "").strip().upper()

    key = (subject, number, instructor)
    course_key = (subject, number)

    features = {"Subject": subject, "Number": int(number), "Instructor": instructor}

    if key in course_dict:
        features.update(course_dict[key])
    elif course_key in course_average_dict:
        features.update(course_average_dict[course_key])
    else:
        print("Course not found. Recheck your input")
        return None

    return features
