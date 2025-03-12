import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the API endpoint
endpoint = "https://archive-api.open-meteo.com/v1/archive"

# Set the parameters
params = {
    "latitude": 34.685641569710285,
    "longitude": 135.5069510274213,
    "start_date": "2024-05-01",
    "end_date": "2024-05-05",
    "hourly": "temperature_2m",
    "timezone": "Asia/Tokyo"
}

# Make the API request
try:
    response = requests.get(endpoint, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    exit()  # Stop execution if API request fails

# Check if response is valid JSON
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    print("Error: Response is not valid JSON.")
    print(f"Response Content: {response.text}")  # Debugging output
    exit()

# Ensure API response contains expected data
if "hourly" not in data or "temperature_2m" not in data["hourly"]:
    print("Error: Missing expected data in API response.")
    print(f"API Response: {data}")  # Debugging output
    exit()

# Extract time and temperature data
times = data["hourly"]["time"]
temperatures = data["hourly"]["temperature_2m"]

# Create a DataFrame
df = pd.DataFrame({
    "time": times,
    "temperature_2m": temperatures
})

# Save to CSV
csv_file = "temperature_data.csv"
df.to_csv(csv_file, index=False)
if os.path.exists(csv_file):
    print(f"Data successfully saved to {csv_file}")
else:
    print(f"Error: Failed to save {csv_file}")
    exit()

# Load the temperature data from CSV
df = pd.read_csv(csv_file)

# Convert time column to datetime format
df["time"] = pd.to_datetime(df["time"])

# Extract date from timestamp
df["date"] = df["time"].dt.date

# Compute daily statistics
daily_summary = df.groupby("date")["temperature_2m"].agg(
    max_temp="max",
    min_temp="min",
    avg_temp="mean"
).reset_index()

# Save daily summary to CSV
summary_file = "daily_temperature_summary.csv"
daily_summary.to_csv(summary_file, index=False)
if os.path.exists(summary_file):
    print(f"Daily summary successfully saved to {summary_file}")
else:
    print(f"Error: Failed to save {summary_file}")
    exit()

# Load the daily temperature summary
df = pd.read_csv(summary_file)

# Convert date column to datetime format for better plotting
df["date"] = pd.to_datetime(df["date"])

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["max_temp"], marker="o", linestyle="-", label="Max Temperature", color="red")
plt.plot(df["date"], df["min_temp"], marker="o", linestyle="-", label="Min Temperature", color="blue")
plt.plot(df["date"], df["avg_temp"], marker="o", linestyle="-", label="Avg Temperature", color="green")

# Formatting the plot
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trends (Max, Min, Avg)")
plt.legend()
plt.grid(True)

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Save the plot as a JPG file
plot_file = "temperature_trends.jpg"
plt.savefig(plot_file, dpi=300, bbox_inches="tight")
plt.show()

# Confirm plot was saved
if os.path.exists(plot_file):
    print(f"Plot successfully saved as {plot_file}")
else:
    print(f"Error: Failed to save {plot_file}")