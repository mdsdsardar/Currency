**Currency Data Web Scraper**

This project scrapes live exchange rate data from a financial website and processes it into a structured format. The data is then written into a CSV file for further analysis.


**Project Overview**

The script is designed to extract currency exchange rate information from PB.pl using Python, BeautifulSoup, and requests libraries. 

It collects currency names, exchange rates, changes, percent changes, buy rates, sell rates, and dates. After extracting and processing the data, it stores the information in a CSV file.


**Requirements**

The script requires the following libraries:


**requests**: To make HTTP requests and retrieve the HTML content.

**beautifulsoup4**: To parse the HTML content and extract the desired data.

**pandas**: To structure the scraped data and save it to a CSV file.


**Script Explanation**

**1. Web Scraping:**
The script makes an HTTP request to the target URL, parses the HTML content using BeautifulSoup, and extracts data such as currency names, exchange rates, changes, buy rates, sell rates, and dates.

**2. Data Processing:**
The scraped data is stored in lists and then converted into a Pandas DataFrame for easy manipulation.

**3. Saving to CSV:**
The processed data is saved to a CSV file for later analysis or use.

**4. Handling Errors:**
Basic error handling is incorporated to ensure the program runs smoothly in case of any issues during the HTTP request or parsing.
