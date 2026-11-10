import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

# Calculate Moving Average
data['Moving_Average'] = data['Passengers'].rolling(window=12).mean()

# Calculate EWMA
data['EWMA'] = data['Passengers'].ewm(span=12).mean()

# Plot results
plt.figure(figsize=(12, 5))

plt.plot(data['Passengers'], label='Original Data')
plt.plot(data['Moving_Average'], label='Moving Average')
plt.plot(data['EWMA'], label='EWMA')

plt.title("Moving Average and EWMA")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)
plt.savefig("outputs/plots/08_moving_average_ewma.png", dpi=300)
plt.show()

print(data.tail())
print("\nMoving Average and EWMA Completed!")