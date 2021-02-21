from bs4 import BeautifulSoup as BS
from selenium import webdriver
from functools import reduce
import pandas as pd
import time

# function to load wunderground data (without this it has no records to show)
def render_page(url):
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r

def fahrenheit_to_celsius(tempinF):
    tempinC = round((tempinF -32)*(5/9),2)
    return tempinC
def inches_to_cm(inch):
    mm = round(inch * 25.4,2)
    return mm
# function to scrape wunderground
def scraper(page, dates):
    list_of_df = list()

    for d in dates:

        url = str(str(page) + str(d))

        r = render_page(url)

        soup = BS(r, "html.parser")
        container = soup.find('lib-city-history-observation')
        check = container.find('tbody')

        data = []

        for c in check.find_all('tr', class_='ng-star-inserted'):
            for i in c.find_all('td', class_='ng-star-inserted'):
                trial = i.text
