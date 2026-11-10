import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month into datetime
data['Month'] = pd.to_datetime(data['Month'])

# Extract passenger values
passengers = data['Passengers']

# Perform ADF test
result = adfuller(passengers)

# Display results
print("ADF Test Results")

print("ADF Statistic:", result[0])
print("p-value:", result[1])
print("Number of Lags:", result[2])
print("Observations:", result[3])
# Check stationarity
if result[1] <= 0.05:
    print("Data is Stationary")
else:
    print("Data is Non-Stationary")
plt.savefig("outputs/plots/06_adf_test.png", dpi=300)