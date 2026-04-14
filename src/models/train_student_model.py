import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("data\processed\cleaned_students.csv")


# =========================
# SPLIT DATA
# =========================
X = df.drop(columns=["FinalGrade"])
y = df["FinalGrade"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=11
)


# =========================
# TRAIN MODEL
# =========================
model = RandomForestRegressor(
    n_estimators=200,
    random_state=11
)

model.fit(X_train, y_train)


# =========================
# EVALUATE
# =========================
preds = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
print("RMSE:", root_mean_squared_error(y_test, preds))
print("R2:", r2_score(y_test, preds))