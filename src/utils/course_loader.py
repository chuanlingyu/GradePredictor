import pandas as pd

df = pd.read_csv("data/processed/cleaned_course_database.csv")
    
df['Subject'] = df['Subject'].astype(str).str.strip().str.upper()
df['Number'] = df['Number'].astype(str).str.strip()
df['Primary Instructor'] = df['Primary Instructor'].astype(str).str.strip()

course_dict = {}
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

# def check_exist(subject, number, professor="No input") -> tuple[bool, str]:
#     if subject not in course_dict:
#         return True, "This subject does not exist. Check the subject abbreviation carefully."
    
#     if number not in course_dict[subject]:
#         return True, "The course does not exist for the subject. Check the course number carefully."
    
#     if (not professor == "No input") and (professor not in course_dict[subject][number]):
#         return True, "This professor does not exist or didn't teach this course before. Check the course number carefully"
    
#     return False, ''

def extract_info(subject, number, instructor):

    key = (subject, number, instructor)

    features = {"Subject": subject, "Number": number, "Instructor": instructor}

    if key in course_dict:
        features.update(course_dict[key])
    else:
        print("Course not found. Recheck your input")
        return None

    return features