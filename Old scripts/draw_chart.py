import requests
import csv
import matplotlib.pyplot as plt
import pandas as pd

def fetch_weather_data():
    """
    Fetch historical weather data from Open-Meteo API for the specified location and date range.
    Save the results in a CSV file.
    """
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 30.21,
        "longitude": 10.00,
        "start_date": "2025-01-01",
        "end_date": "2025-02-01",
        "hourly": ["rain", "wind_speed_10m"],
        "timezone": "UTC"
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()
    
    # Extract relevant data
    hourly_data = data.get("hourly", {})
    timestamps = hourly_data.get("time", [])
    rain = hourly_data.get("rain", [])
    wind_speed = hourly_data.get("wind_speed_10m", [])
    
    # Check if data is fetched properly
    print(f"Fetched {len(timestamps)} timestamps")

    # Save to CSV
    with open("weather_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Rain (mm)", "Wind Speed (m/s)"])
        for i in range(len(timestamps)):
            writer.writerow([timestamps[i], rain[i], wind_speed[i]])
    
    print("Weather data saved to weather_data.csv")

def draw_chart():
    """
    Read the weather data from the CSV file and generate a line chart.
    Save the chart as a PNG file.
    """
    # Load the data
    df = pd.read_csv("weather_data.csv")
    
    # Check if the data is read correctly
    if df.empty:
        print("Error: No data in CSV file.")
        return
    
    print(f"Data loaded, {len(df)} rows")

    df["Time"] = pd.to_datetime(df["Time"])
    
    plt.figure(figsize=(12, 6))
    plt.plot(df["Time"], df["Rain (mm)"], label="Rain (mm)", color="blue")
    plt.plot(df["Time"], df["Wind Speed (m/s)"], label="Wind Speed (m/s)", color="red")
    
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("Rain and Wind Speed Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()
    
    # Save the chart as a PNG file
    plt.savefig("weather_chart.png")  # Save the figure to a file
    plt.close()  # Close the plot to avoid displaying it
    
    print("Chart saved as weather_chart.png")

if __name__ == "__main__":
    fetch_weather_data()
    draw_chart()