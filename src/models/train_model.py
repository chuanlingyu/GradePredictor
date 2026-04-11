import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle


def load_data(path):
    return pd.read_csv(path)


def split_data(df, target_col="Average_GPA"):
    df = df.dropna()

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X = pd.get_dummies(X, drop_first=True)

    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train, model_type="rf"):
    if model_type == "lr":
        model = LinearRegression()

    elif model_type == "rf":
        model = RandomForestRegressor(
            n_estimators=200,
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


def main():
    df = load_data("data/processed/cleaned_grades.csv")

    X_train, X_test, y_train, y_test = split_data(df)

    lr_model = train_model(X_train, y_train, model_type="lr")
    evaluate(lr_model, X_test, y_test, name="Linear Regression")

    rf_model = train_model(X_train, y_train, model_type="rf")
    evaluate(rf_model, X_test, y_test, name="Random Forest")



if __name__ == "__main__":
    main()