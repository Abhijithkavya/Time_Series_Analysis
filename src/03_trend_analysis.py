import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

# Calculate 12-month moving average
data['Trend'] = data['Passengers'].rolling(
    window=12
).mean()

# Plot original data and trend
plt.figure(figsize=(12, 5))

plt.plot(data.index, data['Passengers'],
         label='Original Data')

plt.plot(data.index, data['Trend'],
         label='Trend (12-month Moving Average)')

plt.title("Airline Passenger Trend Analysis")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)
plt.savefig("outputs/plots/03_trend_analysis.png", dpi=300)
plt.show()

print("Trend Analysis Completed!")