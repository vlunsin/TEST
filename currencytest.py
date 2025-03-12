import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta

def fetch_exchange_rates(driver, date, base_url):
    """Fetch exchange rates for a given date from XE.com using Selenium."""
    url = f"{base_url}{date}#table-section"
    driver.get(url)
    time.sleep(5)  # Allow time for JavaScript to load the table
    
    try:
        table = driver.find_element(By.CLASS_NAME, "currencytables__Table")
        rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip header row
        data = []
        
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:
                currency = cols[0].text.strip()
                code = cols[1].text.strip()
                rate = cols[2].text.strip()
                data.append([currency, code, float(rate), date])
        
        return data
    except Exception as e:
        print(f"No data found for {date}: {e}")
        return None

def fetch_and_save_exchange_rates(start_date, end_date):
    """Retrieve exchange rates for a date range and save them to an Excel file."""
    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Define the base URL for XE
    BASE_URL = "https://www.xe.com/currencytables/?from=JPY&date="
    
    # Collect all exchange rate data
    df_list = []
    date = start_date
    while date <= end_date:
        rates = fetch_exchange_rates(driver, date.strftime('%Y-%m-%d'), BASE_URL)
        if rates:
            df_list.extend(rates)
        date += timedelta(days=1)
    
    # Close WebDriver
    driver.quit()
    
    # Convert to DataFrame
    df = pd.DataFrame(df_list, columns=["Currency", "Code", "Rate", "Date"])
    
    # Ask user for file name
    output_file = input("Enter the name of the output Excel file (including .xlsx): ")
    
    # Create an Excel file with separate sheets per currency
    with pd.ExcelWriter(output_file) as writer:
        for currency_code in df["Code"].unique():
            df[df["Code"] == currency_code].to_excel(writer, sheet_name=currency_code, index=False)
    
    print(f"Data successfully saved to {output_file}")

# Define the date range
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 5, 5)

# Run the function
fetch_and_save_exchange_rates(start_date, end_date)
