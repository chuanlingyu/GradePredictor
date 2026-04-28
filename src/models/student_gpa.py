from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path("data/processed/cleaned_students.csv")
ARTIFACT_PATH = Path("outputs/models/student_gpa_model.joblib")


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def split_data(df, target_col="GPA"):
    if target_col not in df.columns:
        raise ValueError(f"Missing target column: {target_col}")

    df = df.dropna().copy()
    X = df.drop(columns=[target_col])
    y = df[target_col]

    X = pd.get_dummies(X, drop_first=False)

    return train_test_split(X, y, test_size=0.2, random_state=3)


def train_student_gpa_model(X_train, y_train):
    model = GradientBoostingRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=3,
        random_state=3,
    )
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test, name="Student GPA Model"):
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    print(f"\n{name} Results:")
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2:", r2)

    return float(mae), float(rmse), float(r2)


def save_artifact(model, feature_columns, metrics, path=ARTIFACT_PATH):
    artifact = {
        "model": model,
        "feature_columns": feature_columns,
        "metrics": metrics,
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, path)
    return path


def main():
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)

    model = train_student_gpa_model(X_train, y_train)
    mae, rmse, r2 = evaluate(model, X_test, y_test)

    save_path = save_artifact(
        model,
        X_train.columns.tolist(),
        {
            "mae": mae,
            "rmse": rmse,
            "r2": r2,
        },
    )
    print(f"Saved student GPA model artifact to {save_path}")


if __name__ == "__main__":
    main()
