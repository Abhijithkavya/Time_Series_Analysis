import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Convert Month to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Set Month as index
data.set_index('Month', inplace=True)

# Perform decomposition
result = seasonal_decompose(
    data['Passengers'],
    model='multiplicative',
    period=12
)

# Display decomposition graph
result.plot()
plt.suptitle("Time Series Decomposition")
plt.savefig("outputs/plots/09_decomposition.png", dpi=300)
plt.tight_layout()
plt.show()

print("Decomposition Completed!")