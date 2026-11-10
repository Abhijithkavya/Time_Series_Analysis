import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month into datetime
data['Month'] = pd.to_datetime(data['Month'])

# Extract month number
data['Month_Number'] = data['Month'].dt.month

# Calculate average passengers for each month
monthly = data.groupby('Month_Number')['Passengers'].mean()

# Display result
print("Average Monthly Passengers:")
print(monthly)

# Plot seasonal pattern
plt.figure(figsize=(10, 5))

plt.plot(monthly.index, monthly.values,
         marker='o')

plt.title("Monthly Seasonal Pattern")
plt.xlabel("Month")
plt.ylabel("Average Passengers")
plt.xticks(range(1, 13))
plt.grid(True)
plt.savefig("outputs/plots/04_seasonality_analysis.png", dpi=300)
plt.show()

print("Seasonality Analysis Completed!")