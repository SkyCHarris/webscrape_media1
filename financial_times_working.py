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

#! Paused due to issues with pulling up links, paywalls, etc.

# Set up a Selenium WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = driver.get("https://www.ft.com/crypto")

time.sleep(1)

# Get list of articles as web elements
article_elements = [link for link in driver.find_elements(By.XPATH, "//ul/li[1]/div[2]/div/div/div[1]//a")]
#? /html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/ul/li[1]/div[2]/div/div/div[1]/div[2]/a



# Get list of articles as links
article_links = []
for link in article_elements:
    attr_link = link.get_attribute("href")
    article_links.append(attr_link)
print(article_links)

# Loop through links
# author_links = []
# author_names = []
# for link in recent_article_links:
#     driver.get(link)
#     try:
#         author_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//article/div[2]/a[@href]"))).get_attribute("href")  # Get author link
#         author_name = driver.find_element(By.XPATH, "//article/div[2]/a[@href]").text
#         author_links.append(author_link)
#         author_names.append(author_name)
#     except TimeoutException:
#         continue