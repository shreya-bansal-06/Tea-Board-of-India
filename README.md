# Tea-Board-of-India
The task involves scraping data from the "WEEKLY AVERAGE PRICES OF TOTAL TEA SOLD AT INDIAN AUCTION" table on the Tea Board of India website (https://www.teaboard.gov.in/WEEKLYPRICES/2023) for all available years i.e. from 2008 to 2023.

## Usage
1. Install the required dependencies by running the following command:
2. Run the script by executing the following command:
3. The script will scrape the data for each year from 2008 to 2023 and consolidate it into a CSV file named `tea_prices.csv`.
4. The CSV file will be saved in the same directory where the script is located.

## Additional-Notes
- Make sure you have a stable internet connection for the script to successfully scrape the data.
- The script utilizes the `requests`, `beautifulsoup4`, and `pandas` libraries. If you encounter any import errors, ensure that these dependencies are properly installed.
- The script may take some time to execute, depending on the number of years being scraped.
- The CSV file contains three columns: "week" (formatted as DD-MM-YYYY), "location", and "average_price".
- The "location" column corresponds to the different places listed in the weekly average prices table on the Tea Board of India website.
- If any year's data is not available or the table is not found for a particular year, a message will be printed indicating the skipped year.
- Please refer to the script's code comments for more detailed explanations of the implementation.

## CSV-File
[Uploading tea_prices.csv…]()


