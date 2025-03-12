import requests
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import datetime, date

def get_hourly_temperature_data(latitude, longitude, start_date, end_date):
    """
    Retrieves hourly temperature data from the Open-Meteo API.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pandas.DataFrame: DataFrame containing hourly temperature data.
    """
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m"
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    data = response.json()
    df = pd.DataFrame(data)
    df_hourly = pd.DataFrame(df['hourly'])
    df_time = pd.DataFrame(df_hourly['hourly']['time'], columns =['time'])
    df_temperature_2m = pd.DataFrame(df_hourly['hourly']['temperature_2m'], columns =['temperature_2m'])
    df = pd.concat([df_time, df_temperature_2m], axis=1)
    df['time'] = pd.to_datetime(df['time'])
    return df

def calculate_daily_stats(df):
    """
    Calculates daily maximum, minimum, and average temperatures.

    Args:
        df (pandas.DataFrame): DataFrame with hourly temperature data.

    Returns:
        pandas.DataFrame: DataFrame containing daily temperature statistics.
    """
    df['date'] = df['time'].dt.date
    daily_stats = df.groupby('date')['temperature_2m'].agg(['max', 'min', 'mean'])
    daily_stats.rename(columns={'max': 'max_temp', 'min': 'min_temp', 'mean': 'avg_temp'}, inplace=True)
    return daily_stats

def plot_daily_temperature_changes(daily_stats, output_path="temperature_plot.jpg"):
    """
    Plots daily temperature changes and saves the plot to a file.

    Args:
        daily_stats (pandas.DataFrame): DataFrame with daily temperature statistics.
        output_path (str, optional): Path to save the plot. Defaults to "temperature_plot.jpg".
    """
    plt.figure(figsize=(12, 6))
    plt.plot(daily_stats.index, daily_stats['max_temp'], marker='o', label='Max Temperature')
    plt.plot(daily_stats.index, daily_stats['min_temp'], marker='o', label='Min Temperature')
    plt.plot(daily_stats.index, daily_stats['avg_temp'], marker='o', label='Avg Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Temperature Changes')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main(latitude, longitude, start_date, end_date, hourly_output_csv="hourly_temperature.csv", daily_output_csv="daily_temperature_stats.csv"):
    """
    Main function to orchestrate data retrieval, processing, and plotting.
    """
    hourly_data = get_hourly_temperature_data(latitude, longitude, start_date, end_date)
    hourly_data.to_csv(hourly_output_csv, index=False)

    daily_stats = calculate_daily_stats(hourly_data)
    daily_stats.to_csv(daily_output_csv)

    plot_daily_temperature_changes(daily_stats)

if __name__ == "__main__":
    latitude = 34.685641569710285
    longitude = 135.5069510274213
    start_date = "2024-05-01"
    end_date = "2024-05-05"
    main(latitude, longitude, start_date, end_date)
