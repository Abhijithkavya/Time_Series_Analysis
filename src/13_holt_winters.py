import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

passengers = data['Passengers']

# Build Holt-Winters model
model = ExponentialSmoothing(
    passengers,
    trend='add',
    seasonal='mul',
    seasonal_periods=12
)

model_fit = model.fit()

# Forecast next 12 months
forecast = model_fit.forecast(12)

print("Holt-Winters Forecast:")
print(forecast)

# Plot graph
plt.figure(figsize=(12, 5))

plt.plot(passengers, label="Original Data")
plt.plot(forecast, label="Forecast")

plt.title("Holt-Winters Forecasting")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)
plt.savefig("outputs/plots/13_hot_winters.png", dpi=300)
plt.show()

print("Holt-Winters Completed!")