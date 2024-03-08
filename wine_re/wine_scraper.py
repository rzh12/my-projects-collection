from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import re

# print(selenium)
# print(selenium.__version__)


def crawl_vivino_page(url: str) -> str:
    """
    Fetches the source code of a webpage from a given URL.

    Uses Selenium WebDriver to open Chrome browser, navigates to the specified URL, and retrieves the HTML source code of the page.

    Parameters:
        url (str): The URL of the webpage to be fetched.

    Returns:
        str: The source code of the webpage. Returns an empty string if an error occurs during the process.
    """
    page_source = ""
    # Set ChromeOptions to prefer English language for the webpage
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    try:
        scroll_pause_time = 2  # Set the time to pause between scrolls
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)

            # Calculate the new scroll height and compare it with the last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # Scroll up and down to trigger lazy loading if heights are unchanged
                driver.execute_script("window.scrollBy(0, -150);")
                time.sleep(scroll_pause_time)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_pause_time)

                # Check if the scroll height has changed
                final_height = driver.execute_script("return document.body.scrollHeight")
                if final_height == new_height:
                    # If there's no change, break the loop
                    break
            last_height = new_height

        page_source = driver.page_source

    except Exception as e:
        print(f"An error occurred while attempting to fetch the page: {e}")
    finally:
        driver.quit()

    return page_source


def parse_page(page_source):
    soup = BeautifulSoup(page_source, features="lxml")
    wine_info = soup.find_all('div', class_='wineInfo__wineInfo--Sx0T0')
    regions = soup.find_all('div', class_='wineInfoLocation__regionAndCountry--1nEJz')
    ratings = soup.find_all('div', class_='vivinoRating_averageValue__uDdPM')
    ratings_counts = soup.find_all('div', class_='vivinoRating_caption__xL84P')
    prices = soup.find_all('div', class_='addToCart__subText--1pvFt addToCart__ppcPrice--ydrd5')

    # Extract wine_info
    wineries_list = []
    names_list = []
    for ele in wine_info:
        # Extract winery
        winery = ele.find('div', class_='wineInfoVintage__truncate--3QAtw').text \
            if ele.find('div', class_='wineInfoVintage__truncate--3QAtw') else 'N/A'
        # Extract wine name
        name = ele.find('div', class_='wineInfoVintage__vintage--VvWlU wineInfoVintage__truncate--3QAtw').text \
            if ele.find('div', class_='wineInfoVintage__vintage--VvWlU wineInfoVintage__truncate--3QAtw') else 'N/A'
        wineries_list.append(winery)
        names_list.append(name)
    # print(wineries_list)
    # print(names_list)

    # Extract region
    regions_list = [region.text if region else "N/A" for region in regions]
    # print(regions_list)

    # Extract vintage
    vintages_list = [n[-4:] if n[-4:].isdigit() else "N/A" for n in names_list]
    # print(vintages_list)

    # Extract rating
    ratings_list = [rating.text if rating else "N/A" for rating in ratings]
    # print(ratings_list)

    # Extract n_of_ratings: original tokens are "###個評分"
    ratings_counts_r = [count.text if count else "N/A" for count in ratings_counts]
    ratings_counts_list = [re.findall(r'\d+', n)[0] if n != "N/A" else "N/A" for n in ratings_counts_r]
    # print(ratings_counts_list)

    # Extract price: original tokens are "線上商店在售$#"
    prices_r = [p.text if p else "N/A" for p in prices]
    prices_list = [re.findall(r'\d+', n.replace(',', ''))[0] if n != "N/A" else "N/A" for n in prices_r]
    # print(prices_list)

    data = {
        'Name': names_list,
        'Winery': wineries_list,
        'Region': regions_list,
        'Vintage': vintages_list,
        'Rating': ratings_list,
        'RatingsCount': ratings_counts_list,
        'Price': prices_list
    }
    df = pd.DataFrame(data)

    return df


def main():
    # This specific URL points to a page where certain filters have already been applied on Vivino
    url = "https://www.vivino.com/explore?e=eJwNxDEOgkAQBdDb_JJAtLD5oeEIJhTGmHF32GzCDmZYQW4vr3h9OHgfEc4GpImbeNYqM4rz0tywvA-61GxpfcmmLkmxeGTUNaDIj117QsnGFnt9PHnFhx2-FnXKppFqf7JAIdk"
    page_source = crawl_vivino_page(url)
    df = parse_page(page_source)
    df.to_csv('wine_red.csv', index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    main()
