import joblib
import pandas as pd
from src.utils.course_loader import extract_info

CLASS_GPA_ARTIFACT_PATH = 'outputs/models/class_gpa_model.joblib'
STUDENT_GPA_ARTIFACT_PATH = 'outputs/models/student_gpa_model.joblib'
ARTIFACT_PATH = CLASS_GPA_ARTIFACT_PATH

def load_artifact(path=ARTIFACT_PATH):
    return joblib.load(path)

def predict_gpa(features, artifact=None):
    if artifact is None:
        artifact = load_artifact()

    model = artifact['model']
    feature_columns = artifact['feature_columns']

    row = pd.DataFrame([features])

    # Take whatever features I gave you, arrange them in the same order the model was trained with, and if a column is missing, fill it with 0
    row = row.reindex(columns=feature_columns, fill_value=0)

    predicted_gpa = model.predict(row)[0]

    return float(predicted_gpa)

def predict_course(subject, number, instructor, artifact=None):
    features = extract_info(subject, number, instructor)

    if features is None:
        return None
    
    return predict_gpa(features, artifact)


def predict_student_gpa(profile, artifact=None):
    if artifact is None:
        artifact = load_artifact(STUDENT_GPA_ARTIFACT_PATH)

    model = artifact['model']
    feature_columns = artifact['feature_columns']

    branch = str(profile.get("branch", "") or "").strip()
    row = {
        "Age": profile.get("age"),
        "Study_Hours_per_Day": profile.get("study_hours_per_day"),
        "Sleep_Hours": profile.get("sleep_hours"),
        "Screen_Time_Hours": profile.get("screen_time_hours"),
        "Attendance_Percentage": profile.get("attendance_percentage"),
        "Stress_Level_1_to_10": profile.get("stress_level"),
    }

    for column in feature_columns:
        if column.startswith("Branch_"):
            row[column] = 1 if column == f"Branch_{branch}" else 0

    frame = pd.DataFrame([row]).reindex(columns=feature_columns, fill_value=0)
    frame = frame.apply(pd.to_numeric, errors="coerce")

    if frame.isna().any(axis=None):
        missing = frame.columns[frame.isna().any()].tolist()
        raise ValueError(f"Missing or invalid student profile fields: {', '.join(missing)}")

    return float(model.predict(frame)[0])
