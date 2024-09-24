# Webscrape The Defiant Media Outlet

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import openpyxl
from openpyxl.workbook import Workbook
from openpyxl import Workbook
from openpyxl.writer.excel import ExcelWriter
import xlsxwriter

# Set up a Selenium WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# List of page URLs
url_bitcoin = "https://cointelegraph.com/tags/bitcoin"
url_blockchain = "https://cointelegraph.com/tags/blockchain"
url_business = "https://cointelegraph.com/tags/business"
url_defi = "https://cointelegraph.com/tags/defi"

# As a list to loop through
url_list = [url_bitcoin, url_blockchain, url_business, url_defi]

wb = Workbook()
ws0 = wb.worksheets[0]
ws0.title = 'Cointelegraph'


# Loop through pages, links, authors, author links
for url in url_list:
    driver.get(url)

    # Wait for the page to load 
    time.sleep(1) 

    # Get list of articles as web elements
    links_title = [link for link in driver.find_elements(By.XPATH, "//main//article/div/div[1]/a/span")]   #TODO: Working, add authors
    #? /html/body/div/div/div/div[2]/div[3]/main/div/div/div[3]/div[1]/div[2]/ul/li[1]/article/div/div[1]/a/span
    links_author = [link for link in driver.find_elements(By.XPATH, "//main//article/div/div[1]/div/p/a/span")]
    #? /html/body/div/div/div/div[2]/div[3]/main/div/div/div[3]/div[1]/div[2]/ul/li[1]/article/div/div[1]/div/p/a/span


    links_title_text = []
    for link in links_title:
        link = link.text
        links_title_text.append(link)
    print(links_title_text)

    links_author_text = []
    for link in links_author:
        link = link.text
        links_author_text.append(link)
    print(links_author_text)

    nested_list = [links_title_text, links_author_text]

    for sub_list in nested_list:
        ws0.append(sub_list)

wb.save("cointelegraph.xlsx") 

#TODO: Add author links, author socials

    





