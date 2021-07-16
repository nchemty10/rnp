from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from bs4 import BeautifulSoup, element

PATH = "/Users/nchemtytanyi/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

""" url = 'https://rnp.unicorn.com/NOM04/' """

""" r = requests.get(url) """
""" soup = BeautifulSoup(r.text, 'html.parser') """
driver.get('https://rnp.unicorn.com/NOM04/')
soup=BeautifulSoup(driver.page_source, 'html.parser')


# Click 'show data' button

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".color-schema-green.color-schema-success.uu5-bricks-button.usy-damas-core-bricks-form-submit-button.uu5-bricks-button-m.uu5-bricks-button-filled"))).click()

time.sleep(10)


main_table = soup.find('table', class_ = 'table table-striped table-condensed table-bordered pq-grid-header-table pq-wrap ') 


print(main_table)
""" print(soup) """