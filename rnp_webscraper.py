"""
A webscraper to collect and store data, in order to predict future gas demands.
by: Nchemty Tanyi
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import socket
from bs4 import BeautifulSoup

# Function that returns data frame
def return_data_frame ():
    # Creates path, opens browser then opens URL 
    PATH = "/Users/nchemtytanyi/Documents/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get('https://rnp.unicorn.com/NOM04/')

    # Click 'show data' button
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".color-schema-green.color-schema-success.uu5-bricks-button.usy-damas-core-bricks-form-submit-button.uu5-bricks-button-m.uu5-bricks-button-filled"))).click()

    # Parses HTML 
    soup=BeautifulSoup(driver.page_source, 'html.parser')

    time.sleep(10)

    # Create list object of data frames
    list_of_tables = pd.read_html(str(soup))
    headers = list_of_tables[0]
    headers = headers.loc[2].values
    data = list_of_tables[1]
    data.columns = headers 
    return list_of_tables[0],list_of_tables[1]

# Checks internet connection
def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

if __name__ == '__main__':

    if(is_connected()): 
        headers,list_of_tables = return_data_frame()  
        print(list_of_tables) 
        print(headers)


    else:
        print("No Internet Connection")

