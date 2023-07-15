import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Mapping of column headings to actual place names
PLACE_MAPPING = {
    "Kolkata": "Kolkata",
    "Guwahati": "Guwahati",
    "Siliguri": "Siliguri",
    "Jalpaiguri": "Jalpaiguri",
    "mjunction": "mjunction",
    "Cochin": "Cochin",
    "Coonoor": "Coonoor",
    "Coimbatore": "Coimbatore",
    "Tea Serve": "Tea Serve"
}

# Function to scrape the data for a given year
def scrape_data(year):
    url = f"https://www.teaboard.gov.in/WEEKLYPRICES/{year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table with the weekly average prices
    table = soup.find("table")

    if table is None:
        print(f"No table found for year {year}. Skipping...")
        return []

    # Extract the data from the table
    data = []
    rows = table.find_all("tr")
    for row in rows[2:]:
        columns = row.find_all("td")
        if len(columns) >= 10:
            week = columns[0].text.strip()
            for i in range(1, len(columns), 1):
                location = list(PLACE_MAPPING.keys())[i-1]
                average_price = columns[i].text.strip()
                formatted_week = pd.to_datetime(week, format="%d/%m/%Y").strftime("%d-%m-%Y")
                data.append((formatted_week, location, average_price))

    return data

# Main function to scrape data for all years and consolidate into a CSV file
def scrape_and_consolidate():
    years = range(2008, 2024)  # Adjust the range to include all desired years

    # Scrape data for each year
    all_data = []
    for year in years:
        data = scrape_data(year)
        all_data.extend(data)

    # Create a DataFrame from the scraped data
    df = pd.DataFrame(all_data, columns=["week", "location", "average_price"])

    # Save the DataFrame to a CSV file
    file_path = "tea_prices.csv"
    df.to_csv(file_path, index=False)

    print(f"Data saved to {file_path}")

# Run the main function
if __name__ == "__main__":
    scrape_and_consolidate()
