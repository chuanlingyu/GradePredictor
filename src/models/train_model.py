import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
import pickle

def load_data(path):
    return pd.read_csv(path)

def split_data(df):
    X = df.drop(columns=["Average_GPA"])
    y = df["Average_GPA"]

    return train_test_split(X, y, test_size=0.2, random_state=11)

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)

    print("MAE:", mean_absolute_error(y_test, preds))
    print("RMSE:", root_mean_squared_error(y_test, preds))
    print("R2:", r2_score(y_test, preds))

def save_model(model, path="model.pkl"):
    with open(path, "wb") as f:
        pickle.dump(model, f)

def main():
    df = load_data("../data/processed/cleaned_grades.csv")

    X_train, X_test, y_train, y_test = split_data(df)

    model = train_model(X_train, y_train)

    evaluate(model, X_test, y_test)

    save_model(model)

if __name__ == "__main__":
    main()