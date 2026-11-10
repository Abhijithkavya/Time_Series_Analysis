import pandas as pd

# Load the CSV dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month into datetime format
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

# Display first five rows
print("Time Series Data:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

print("\nPractical 1 Completed!")