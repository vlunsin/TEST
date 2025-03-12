import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_currency_data(date):
    """Retrieves currency data from xe.com for a given date."""
    url = f"https://www.xe.com/currencytables/?from=JPY&date={date}#table-section"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {date}: {e}")
        return None

def parse_currency_data(html_content):
    """Parses the HTML content to extract currency data."""
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'class': 'tbl-fixed history-rate-data'})
    if not table:
        print("Table not found in HTML content.")
        return None

    data = []
    rows = table.find_all('tr')
    for row in rows[1:]:  # Skip header row
        cols = row.find_all('td')
        if len(cols) == 5:
            currency_code = cols[0].text.strip()
            currency_name = cols[1].text.strip()
            units_per_jpy = cols[2].text.strip()
            jpy_per_unit = cols[3].text.strip()
            data.append([currency_code, currency_name, units_per_jpy, jpy_per_unit])
    return data

def create_excel_file(data_dict, output_filename="currency_data.xlsx"):
    """Creates an Excel file with each currency's data in a separate sheet."""
    with pd.ExcelWriter(output_filename, engine='xlsxwriter') as writer:
        for currency, data in data_dict.items():
            df = pd.DataFrame(data, columns=['Currency Code', 'Currency Name', 'Units per JPY', 'JPY per Unit'])
            df.to_excel(writer, sheet_name=currency, index=False)
    print(f"Excel file '{output_filename}' created successfully.")

def main(start_date, end_date):
    """Main function to retrieve, parse, and save currency data."""
    date_range = pd.date_range(start=start_date, end=end_date)
    currency_data = {}

    for date in date_range:
        date_str = date.strftime('%Y-%m-%d')
        html_content = get_currency_data(date_str)
        if html_content:
            data = parse_currency_data(html_content)
            if data:
                currency_data[date_str] = data

    # Restructure data for Excel export (group by currency code)
    currency_data_by_code = {}
    for date, daily_data in currency_data.items():
        for row in daily_data:
            currency_code = row[0]
            if currency_code not in currency_data_by_code:
                currency_data_by_code[currency_code] = []
            currency_data_by_code[currency_code].append(row + [date])  # Add date to the row

    # Create Excel file with separate sheets for each currency
    create_excel_file(currency_data_by_code)

if __name__ == "__main__":
    start_date = "2024-05-01"
    end_date = "2024-05-05"
    main(start_date, end_date)
