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
    main_table = pd.DataFrame({"Col1" : [0,1,2,3], "col2" : [10, 20, 30, 40]})
    return main_table

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

        # Creates path, opens browser then opens URL 
        PATH = "/Users/nchemtytanyi/Documents/chromedriver"
        driver = webdriver.Chrome(PATH)
        driver.get('https://rnp.unicorn.com/NOM04/')

        # Click 'show data' button
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".color-schema-green.color-schema-success.uu5-bricks-button.usy-damas-core-bricks-form-submit-button.uu5-bricks-button-m.uu5-bricks-button-filled"))).click()

        # Parses HTML 
        soup=BeautifulSoup(driver.page_source, 'html.parser')

        time.sleep(10)

        # Create table from HTML
        main_table = pd.read_html(str(soup))

        # Join 2 data frames together and write to csv file
        with open('final_rnp.csv','w+') as f:
            for df in main_table:
                df.to_csv(f)
else:
    print("No Internet Connection")

