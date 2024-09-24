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
    links_title = [link for link in driver.find_elements(By.XPATH, "//main//article//a[@href]")]   #! Returning Tag, Title, Author all together
    links_author = [link for link in driver.find_elements(By.CLASS_NAME, "post-card-inline__author")]   #! Not returning anything

    links_name = []
    for link in links_title:
        link = link.text
        links_name.append(link)
    print(links_name)

    links_authors = []
    for link in links_authors:
        link = link.text
        links_authors.append(link)
    print(links_authors)

#? /html/body/div/div/div/div[2]/div[3]/main/div/div/div[3]/div[1]/div[2]/ul/li[1]/article
#? Aritcle Title: /html/body/div/div/div/div[2]/div[3]/main/div/div/div[3]/div[1]/div[2]/ul/li[1]/article/div/div[1]/a
# ^ find_elements(By. XPATH [@href])
#? Article Author: /html/body/div/div/div/div[2]/div[3]/main/div/div/div[3]/div[1]/div[2]/ul/li[1]/article/div/div[1]/div/p/a/span
# % find_elements(BY.Class_name)

# ws0.append(links_name)
# wb.save("cointelegraph.xlsx") 

    # # Get article url
    # article_links = []
    # article_info = []
    # for link in links_list:
    #     attr_link = link.get_attribute("href")
    #     article_links.append(attr_link)
    #     article_info.append(link.text)

    # # nested_list = [article_links, article_info]

    # for i, j, k in article_info:
    #     print(i,j,k)
    # ws0.append(article_info)
    





