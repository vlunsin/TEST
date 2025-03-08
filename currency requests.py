import requests
import pandas as pd
import time
import random
from io import StringIO

# Define base URL and date range
base_url = "https://www.xe.com/currencytables/?from=JPY&date={date}#table-section"
dates = ["2024-05-01", "2024-05-02", "2024-05-03", "2024-05-04", "2024-05-05"]

# User-Agent rotation
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
]

# List to store all data
all_data = []

# Loop through each date and scrape data
for date in dates:
    url = base_url.format(date=date)
    headers = {"User-Agent": random.choice(user_agents)}

    print(f"Fetching data for {date}...")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data for {date}. Status Code: {response.status_code}")
        print(response.text[:500])  # Print part of response to debug
        continue

    # Read HTML tables using pandas
    try:
        tables = pd.read_html(StringIO(response.text))
    except Exception as e:
        print(f"Error reading tables for {date}: {e}")
        continue

    if not tables:
        print(f"No table found for {date}")
        continue

    # Extract exchange rate table
    df = tables[0]

    # Rename columns for clarity
    df.columns = ["Currency Code", "Currency Name", "Units per JPY", "JPY per Unit"]

    # Add date column
    df["Date"] = date

    # Store data
    all_data.append(df)

    # Respectful scraping: Wait before the next request
    time.sleep(random.uniform(3, 6))  # Random delay

# Check if any data was scraped
if not all_data:
    print("No data collected. Exiting.")
    exit()

# Combine all data into a single DataFrame
final_df = pd.concat(all_data, ignore_index=True)

# Create a dictionary to store data by currency code
currency_data = {}

# Split data by currency code and save to a dictionary
for currency_code in final_df["Currency Code"].unique():
    currency_data[currency_code] = final_df[final_df["Currency Code"] == currency_code]

# Save the data to an Excel file with each currency in a separate sheet
with pd.ExcelWriter("currency_exchange_rates.xlsx") as writer:
    for currency_code, data in currency_data.items():
        safe_currency_code = "".join(c for c in currency_code if c.isalnum())[:31]  # Excel sheet name fix
        data.to_excel(writer, sheet_name=safe_currency_code, index=False)

print("Data has been saved to 'currency_exchange_rates.xlsx'")

# Create a dictionary to store data by currency code
currency_data = {}

# Split data by currency code and store it in a dictionary
for currency_code in final_df["Currency Code"].unique():
    currency_data[currency_code] = final_df[final_df["Currency Code"] == currency_code]

# Save the data to an Excel file with each currency in a separate sheet
excel_filename = "currency_exchange_rates.xlsx"

with pd.ExcelWriter(excel_filename) as writer:
    for currency_code, data in currency_data.items():
        # Ensure sheet names are Excel-compatible (Max 31 characters, no special chars)
        safe_currency_code = "".join(c for c in currency_code if c.isalnum())[:31]
        data.to_excel(writer, sheet_name=safe_currency_code, index=False)

print(f"Data has been successfully saved to '{excel_filename}'")