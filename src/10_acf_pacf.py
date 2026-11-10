import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Load dataset
data = pd.read_csv("data/airline_passengers.csv")

# Get passenger values
passengers = data['Passengers']

# Create ACF and PACF plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plot_acf(passengers, lags=30, ax=plt.gca())
plt.title("ACF Plot")

plt.subplot(1, 2, 2)
plot_pacf(passengers, lags=30, ax=plt.gca())
plt.title("PACF Plot")
plt.savefig("outputs/plots/10_acf_pacf.png", dpi=300)
plt.tight_layout()
plt.show()

print("ACF and PACF Analysis Completed!")