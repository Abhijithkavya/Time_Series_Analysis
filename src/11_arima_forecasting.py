import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

passengers = data['Passengers']

# Split training and testing data
train = passengers[:-12]
test = passengers[-12:]

# Build ARIMA model
model = ARIMA(train, order=(1, 1, 1))
model_fit = model.fit()

# Forecast next 12 months
forecast = model_fit.forecast(steps=12)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(test, forecast))
# Save ARIMA forecast results
import os

os.makedirs("outputs", exist_ok=True)

results = pd.DataFrame({
    "Actual Passengers": test,
    "Predicted Passengers": forecast
})

results.to_csv(
    "outputs/arima_forecast_results.csv",
    index=True
)

print("ARIMA results saved successfully!")
print("RMSE:", rmse)
print("Forecasted Passengers:")
print(forecast)

print("\nRMSE:", rmse)

# Plot actual and predicted values
plt.figure(figsize=(12, 5))

plt.plot(train, label="Training Data")
plt.plot(test, label="Actual Data")
plt.plot(forecast, label="ARIMA Forecast")

plt.title("ARIMA Passenger Forecasting")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)
plt.savefig("outputs/plots/11_arima_forecasting.png", dpi=300)
plt.show()

print("ARIMA Forecasting Completed!")