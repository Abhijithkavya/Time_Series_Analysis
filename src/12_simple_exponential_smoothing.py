import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

passengers = data['Passengers']

# Build SES model
model = SimpleExpSmoothing(
    passengers,
    initialization_method="estimated"
)

model_fit = model.fit()

# Forecast next 12 months
forecast = model_fit.forecast(12)
# Save Holt-Winters forecast results
import os

os.makedirs("outputs", exist_ok=True)

forecast_results = forecast.to_frame(
    name="Predicted Passengers"
)

forecast_results.index.name = "Month"

forecast_results.to_csv(
    "outputs/holt_winters_results.csv"
)

print("Holt-Winters results saved successfully!")
# Save forecast results
import os

os.makedirs("outputs", exist_ok=True)

forecast_results = forecast.to_frame(
    name="Predicted Passengers"
)

forecast_results.index.name = "Month"

forecast_results.to_csv(
    "outputs/simple_exponential_smoothing_results.csv"
)

print("SES results saved successfully!")
print("Future Passenger Forecast:")
print(forecast)

# Plot graph
plt.figure(figsize=(12, 5))

plt.plot(passengers, label="Original Data")
plt.plot(forecast, label="SES Forecast")

plt.title("Simple Exponential Smoothing")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)
plt.savefig("outputs/plots/12_simple_exponential_smooting.png", dpi=300)
plt.show()

print("SES Completed!")