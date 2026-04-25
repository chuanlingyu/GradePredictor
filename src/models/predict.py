import joblib
import pandas as pd
from src.utils.course_loader import extract_info

ARTIFACT_PATH = 'outputs/models/model.joblib'

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