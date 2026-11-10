import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert date
data['Month'] = pd.to_datetime(data['Month'])

# Set date as index
data.set_index('Month', inplace=True)

# Calculate rolling mean
rolling_mean = data['Passengers'].rolling(window=12).mean()

# Calculate rolling standard deviation
rolling_std = data['Passengers'].rolling(window=12).std()

# Plot original data
plt.figure(figsize=(12, 5))
plt.plot(data['Passengers'], label='Original Data')

plt.plot(rolling_mean, label='Rolling Mean')
plt.plot(rolling_std, label='Rolling Standard Deviation')

plt.title("Stationarity Analysis")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)
plt.savefig("outputs/plots/05_stationarity_analysis.png", dpi=300)
plt.show()

print("Stationarity Analysis Completed!")