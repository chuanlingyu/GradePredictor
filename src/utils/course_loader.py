import pandas as pd

def load_course_dictionary():
    df = pd.read_csv("data/processed/cleaned_course_database.csv", index = False)
    
    df['subject'] = df['subject'].astype(str).str.strip().str.upper()
    df['course_code'] = df['course_code'].astype(str).str.strip()
    df['professor'] = df['professr'].astype(str).str.strip()

    course_dict = {}
    for _, row in df.iterrows():
        subject = row['subject']
        course_code = row['course_code']
        professor = row['proffesor']

        if subject not in course_dict:
            course_dict[subject] = {}

        if course_code not in course_dict[subject]:
            course_dict[subject][course_code] = set()

        course_dict[subject][course_code].add(professor)

        return course_dict