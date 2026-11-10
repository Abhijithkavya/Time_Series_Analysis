import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

# Apply first order differencing
data['Differenced'] = data['Passengers'].diff()

# Plot original and differenced data
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(data['Passengers'])
plt.title("Original Time Series")

plt.subplot(2, 1, 2)
plt.plot(data['Differenced'])
plt.title("First Order Differencing")
plt.savefig("outputs/plots/07_differencing.png", dpi=300)
plt.tight_layout()
plt.show()

print(data.head(10))
print("\nDifferencing Completed!")