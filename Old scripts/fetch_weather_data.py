import requests
import csv

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
    
    # Save to CSV
    with open("weather_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Rain (mm)", "Wind Speed (m/s)"])
        for i in range(len(timestamps)):
            writer.writerow([timestamps[i], rain[i], wind_speed[i]])
    
    print("Weather data saved to weather_data.csv")

if __name__ == "__main__":
    fetch_weather_data()