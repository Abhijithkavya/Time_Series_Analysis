import pandas as pd
import matplotlib.pyplot as plt
import os

# Get project folder location
project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load CSV file
file_path = os.path.join(project_folder, "data", "airline_passengers.csv")
data = pd.read_csv(file_path)

# Convert Month column into datetime
data["Month"] = pd.to_datetime(data["Month"])

# Create output folder automatically
output_folder = os.path.join(project_folder, "outputs", "plots")
os.makedirs(output_folder, exist_ok=True)

# Create time series graph
plt.figure(figsize=(12, 5))

plt.plot(
    data["Month"],
    data["Passengers"],
    color="blue",
    marker="o",
    label="Monthly Passengers"
)

# Add graph details
plt.title("Monthly Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.legend()
plt.grid(True)

# Save graph
image_path = os.path.join(
    output_folder,
    "02_time_series_visualization.png"
)

plt.tight_layout()
plt.savefig(image_path, dpi=300)

# Display graph
plt.show()

print("Graph saved successfully!")
print("Saved location:", image_path)