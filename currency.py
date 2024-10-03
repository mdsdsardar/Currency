import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_currency_data():
    # Download data from PB
    response = requests.get("https://notowania.pb.pl/instrument/PBWALEURPLN/eurpln")
    response.status_code

    # Check
    if response.status_code == 200:
        # Parse HTML data
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all rows of a table with currency data
        data_rows = soup.find_all('tr')
        currencies = []
        currency_exchange_rate = []
        changes = []
        percent_changes = []
        buy_rates = []
        sell_rates = []
        dates = []

        # Looping through rows and fetching data
        for row in data_rows:
            if row.find('th'):  # Skip header row
                continue  # Go to next loop iteration

            cells = row.find_all('td')
            currencies.append(cells[0].text.strip())  # Get currency name (remove spaces)
            currency_exchange_rate.append(cells[1].text.strip())  # Fetch currency exchange rate
            changes.append(cells[2].text.strip())  # Fetch Changes
            percent_changes.append(cells[3].text.strip())  # Fetch Percent Changes
            buy_rates.append(cells[4].text.strip())  # Fetch Buy Rates 
            sell_rates.append(cells[5].text.strip())  # Fetch Sell Rates
            dates.append(cells[6].text.strip())  # Fetch Date
        
        # Convert exchange rate to float
        currency_exchange_rate_float = []
        for k in currency_exchange_rate:
            currency_exchange_rate_float.append(float(k.replace(',', '.')))
        
        # Data Dictionary
        data = {
            "Currency": currencies,
            "Exchange Rate": currency_exchange_rate_float
        }

        # Create DataFrame from Dict
        currency_df = pd.DataFrame(data)

        # Add calculated EUR/PLN rate
        USD_PLN_rate = currency_df.loc[0, "Exchange Rate"]
        EUR_USD_rate = currency_df.loc[3, "Exchange Rate"]
        EUR_PLN_rate = round((USD_PLN_rate * EUR_USD_rate), 4)

        # Add new rows for EUR/PLN and PLN/PLN
        new_row = {"Currency": "EUR/PLN", "Exchange Rate": EUR_PLN_rate}
        currency_df.loc[len(currency_df)] = new_row
        currency_df.loc[len(currency_df)] = {"Currency": "PLN/PLN", "Exchange Rate": 1}

        # Add today's date to the DataFrame
        today = pd.to_datetime('today')
        currency_df['Date'] = today

        return currency_df
    else:
        print("Failed to fetch data from the website.")
        return None


def save_to_csv():
    currency_df = extract_currency_data()
    
    if currency_df is not None:
        # Save DataFrame to CSV
        currency_df.to_csv(r'C:\Users\Saad\Downloads\Task\Web scrapping\Cars\currency_data.csv', index=False)
        print("Data successfully saved to 'currency_data.csv'.")
    else:
        print("No data to save.")


if __name__ == "__main__":
    save_to_csv()
