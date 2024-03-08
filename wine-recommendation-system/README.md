
## Wine Recommendation System (WRS)

>***The provided code, including the web scraping scripts and the resultant CSV data files, is intended solely for personal practice and technical discussion purposes, not intended for any commercial use. This project is designed to showcase programming skills and understanding of data manipulation and GUI development techniques.***

### Development Background

The diversity of wine choices often confuses consumers, especially those lacking professional knowledge, making it a challenge to select wines that fit personal taste and budget. WRS.v2 focuses on providing a simplified solution by intelligently recommending high-quality wines, making the selection process easy and enjoyable.

### Introduction

WRS is designed to simplify the wine selection process, specifically developed to help wine lovers find their ideal wine based on personal budget and preferences. The system covers a variety of wine types, including red, white, rosé, sparkling, dessert, and fortified wines. By instantaneously fetching and analyzing data of high-quality wines (rated 3.8 stars and above) with a price range of 0 to 10,000 TWD from [Vivino](https://www.vivino.com), it provides users with the latest market information and curated recommendations.

### Features 

WRS's main features include:

- **Filtering and Recommendation**: Not only does it filter based on budget and type, but it also recommends high-quality wines (i.e., those rated 3.8 stars and above) to the user.
- **Wine Type Selection**: Users can choose the type of wine they wish to explore based on personal preference.
- **Detailed Information Display**: It provides detailed information for filtered wines, including the winery, region, vintage, rating, number of reviews, and price.
- **Sorting Function**: Supports sorting the wine results by criteria such as price and rating, helping users easily find the most suitable choice.

## Packages Used

- **Selenium**: Utilized for simulating browser operations to fetch wine data from Vivino based on specific criteria instantaneously.
- **BeautifulSoup**: Employed to parse the HTML content fetched by Selenium, enabling accurate extraction of the required wine information.
- **Pandas**: Used for data cleaning and organization, transforming the raw data into a format suitable for analysis and display.
- **Tkinter**: Deployed to develop the graphical user interface (GUI), providing an intuitive and user-friendly experience for interacting with the system.

### How to Use

>To make showing how WRS works easier, I've already uploaded the data collected by the scraper as CSV files. So, you can skip the scraping part and go straight to using the Wine Recommendation System. Please note that due to potential updates or changes on Vivino's website, there might be discrepancies between the data you scrape and the CSV files provided here, which is to be expected.

#### How to Use the Scraper

The data source of the WRS is fetched from Vivino through a scraper. To run the scraper, you need to follow these steps:

1. **Install Necessary Python Packages**: Ensure `pandas`, `selenium`, and `beautifulsoup4` are installed in your system. Install them by running `pip install pandas selenium beautifulsoup4`.
2. **Download WebDriver**: Selenium requires a WebDriver corresponding to your browser to function. Download the WebDriver for your browser version from the official website, e.g., Chrome WebDriver can be downloaded from the Chrome WebDriver site.
3. **Set WebDriver Path**:  Set the path to the WebDriver in your Python program, or you can simply place the WebDriver in the same directory as your Python script.
4. **Run the Scraper Program**: Ensure your program is directed to the correct Vivino page URL and execute the program to fetch data. The program will automatically navigate the webpage and fetch wine information based on specified conditions.

#### How to Use WRS

The Wine Recommendation System provides a GUI that makes selecting and discovering ideal wines straightforward. Here are the steps to use the WRS system:

1. **Start the System**: Run the Python program for the WRS system. The system will start and display the GUI.
2. **Set Your Budget**: Enter the maximum amount you are willing to pay for wine (in New Taiwan Dollars) in the budget input box. This will serve as one of the filtering criteria.
3. **Select Wine Types**: Based on your preference, check one or more types of wine, such as red wine, white wine, etc. The system will filter the wines based on these selections.
4. **Submit Query**: Click the "查詢" button, and the system will filter wines based on the set budget and selected wine types, displaying a list of wines that meet the criteria.
5. **View Detailed Information**: In the results list, you can view detailed information for each wine, including the winery, region, vintage, rating, number of reviews, and price.
6. **Sort Results**: If needed, you can sort the results by criteria such as price and rating to help you easily find the wine that best matches your expectations.

### Notes

- Before using the scraper, ensure you comply with Vivino's terms of use and data scraping policy.
- Since the wine market and prices can change, the recommended wines and their prices are for reference only. It's advisable to reconfirm before purchasing.
- Make sure the installed WebDriver version matches your browser version to prevent compatibility issues from causing the scraper to malfunction.