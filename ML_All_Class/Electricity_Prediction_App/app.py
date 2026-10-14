import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score

df = pd.read_csv(r"C:\Users\Pramod\OneDrive\AI Python\Senapati Sir\Class Document\ML_All_Class\Electricity_Prediction_App\electricity_bill_dataset.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

required_columns = [
    "MonthlyHours",
    "TariffRate",
    "ElectricityBill"]

df = df[required_columns].dropna()

# Feature eng
# Dataset bill relationship:
# ElectricityBill = MonthlyHours * TariffRate

df["BaseCost"] = df["MonthlyHours"] * df["TariffRate"]

X = df[["MonthlyHours", "TariffRate", "BaseCost"]]
Y = df["ElectricityBill"]

# Spliting dataset

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.25,
    random_state=0)

# Train the prediction model

model = LinearRegression()
model.fit(X_train, Y_train)

# Evolve

predictions = model.predict(X_test)

mae = mean_absolute_error(Y_test, predictions)
mse = mean_squared_error(Y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, predictions)

print("\n========== MODEL EVALUATION ==========")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


comparison = pd.DataFrame({
    "Actual Bill": Y_test.values[:10],
    "Predicted Bill": predictions[:10
]})

print(comparison.round(2).to_string(index=False))

# Test Custom Input
print("\n========== CUSTOM PREDICTION ==========")

monthly_hours = float(input("Enter Monthly Hours: "))
tariff_rate = float(input("Enter Tariff Rate: "))


# Validate user input
if not 0 < monthly_hours <= 744:
    raise ValueError("Monthly Hours must be between 1 and 744.")

if tariff_rate <= 0:
    raise ValueError("Tariff Rate must be greater than zero.")

# Prepare input for prediction
new_data = pd.DataFrame({
    "MonthlyHours": [monthly_hours],
    "TariffRate": [tariff_rate],
    "BaseCost": [monthly_hours * tariff_rate]
})

# Predict electricity bill
predicted_bill = model.predict(new_data)[0]

print("\n========== YOUR PREDICTION ==========")
print("Monthly Hours:", monthly_hours)
print("Tariff Rate:", tariff_rate)
print(f"Predicted Electricity Bill: Rs. {predicted_bill:.2f}")

# Plot Actual vs Predicted
plt.figure(figsize=(8, 5))
plt.scatter(Y_test, predictions, alpha=0.5)
plt.xlabel("Actual Electricity Bill")
plt.ylabel("Predicted Electricity Bill")
plt.title("Actual vs Predicted Electricity Bill")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ==========================================
# GRAPH 2: ACTUAL VS PREDICTED BILL
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    Y_test.values[:50],
    label="Actual Bill",
    marker="o"
)

plt.plot(
    predictions[:50],
    label="Predicted Bill",
    marker="x"
)

plt.title("Actual vs Predicted Electricity Bill")
plt.xlabel("Test Data Records")
plt.ylabel("Electricity Bill (Rs.)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ==========================================
# GRAPH 3: RESIDUAL ERROR PLOT
# ==========================================

residuals = Y_test.values - predictions

plt.figure(figsize=(9, 5))

plt.scatter(
    predictions,
    residuals,
    alpha=0.5
)

plt.axhline(y=0, linestyle="--")

plt.title("Residual Error Plot")
plt.xlabel("Predicted Electricity Bill (Rs.)")
plt.ylabel("Prediction Error (Rs.)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nAll Graphs Displayed Successfully!")

print("\nModel Testing Completed!")




# ==========================================
#  SAVE TRAINED MODEL
# ==========================================

import pickle
from pathlib import Path
25
MODEL_PATH = Path(
    r"C:\Users\Pramod\OneDrive\AI Python\Senapati Sir\Class Document\ML_All_Class\Electricity_Prediction_App\electricity_bill_model.pkl"
)

with open(MODEL_PATH, "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")
print("Model location:", MODEL_PATH)

