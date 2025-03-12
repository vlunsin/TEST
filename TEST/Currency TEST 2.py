import requests
import re
from openpyxl import Workbook

# Function to fetch and parse data from xe.com for a given date
def fetch_exchange_data(date):
    # Construct the URL for the given date
    url = f"https://www.xe.com/currencytables/?from=JPY&date={date}#table-section"
    
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the raw HTML content of the page
        html_content = response.text
        
        # Regular expression to match rows containing currency data
        pattern = r'<tr.*?>(.*?)</tr>'
        
        # Find all the rows (tr) in the table
        rows = re.findall(pattern, html_content, re.DOTALL)
        
        # Initialize a dictionary to hold currency exchange rates
        exchange_data = {}
        
        # Loop through each row to extract currency and exchange rate
        for row in rows:
            # Look for columns (td) within each row
            columns = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
            
            if len(columns) >= 2:  # Ensure there are enough columns
                currency = columns[0].strip()
                exchange_rate = columns[1].strip()
                exchange_data[currency] = exchange_rate
        
        return exchange_data
    else:
        print(f"Failed to retrieve data for {date}")
        return None

# Function to create an Excel file with separate sheets for each currency
def save_to_excel(data, filename):
    # Create a new Excel workbook
    workbook = Workbook()
    
    # Loop through the dictionary to create separate sheets for each currency
    for currency, exchange_rate in data.items():
        # Add a new sheet with the currency name as the sheet title
        sheet = workbook.create_sheet(currency)
        # Add the exchange rate data in the first cell
        sheet['A1'] = exchange_rate
    
    # Save the workbook to a file
    workbook.save(filename)

# Main function to handle the process for the specified dates
def main():
    # List of dates from 2024/05/01 to 2024/05/05
    dates = ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04', '2024-05-05']
    
    # Initialize a dictionary to store the complete data for all dates
    all_data = {}
    
    # Loop through each date to fetch the exchange rates
    for date in dates:
        print(f"Fetching data for {date}...")
        exchange_data = fetch_exchange_data(date)
        
        if exchange_data:
            # Store the exchange rates for each date
            all_data[date] = exchange_data
    
    # Save the data to an Excel file
    if all_data:
        save_to_excel(all_data, 'currency_exchange_data.xlsx')
        print("Data has been successfully saved to currency_exchange_data.xlsx.")
    else:
        print("No data was retrieved.")

# Run the main function
if __name__ == "__main__":
    main()