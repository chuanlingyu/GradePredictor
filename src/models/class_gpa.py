import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
from pathlib import Path

DATA_PATH = Path("data/processed/cleaned_grades.csv")
ARTIFACT_PATH = Path("outputs/models/class_gpa_model.joblib")


def load_data(path):
    return pd.read_csv(path)


def split_data(df, target_col="Average_GPA"):
    if target_col not in df.columns:
        raise ValueError(f"Missing target column: {target_col}")

    df = df.dropna().copy()

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X = pd.get_dummies(X, drop_first=True)

    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_class_gpa_model(X_train, y_train, model_type="rf"):
    if model_type == "lr":
        model = LinearRegression()

    elif model_type == "rf":
        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

    else:
        raise ValueError("model_type must be 'lr' or 'rf'")

    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test, name="Model"):
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
    df = load_data(DATA_PATH)

    X_train, X_test, y_train, y_test = split_data(df)

    lr_model = train_class_gpa_model(X_train, y_train, model_type="lr")
    evaluate(lr_model, X_test, y_test, name="Linear Regression")

    rf_model = train_class_gpa_model(X_train, y_train, model_type="rf")
    mae, rmse, r2 = evaluate(rf_model, X_test, y_test, name="Random Forest")

    save_path = save_artifact(
        rf_model,
        X_train.columns.tolist(),
        {
            "mae": mae,
            "rmse": rmse,
            "r2": r2,
        },
    )
    print(f"Saved class GPA model artifact to {save_path}")


if __name__ == "__main__":
    main()

