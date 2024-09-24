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

url = driver.get("https://techcrunch.com/category/fintech/")

time.sleep(1)

# Get list of Fintech articles as headline text
article_headlines = [link.text for link in driver.find_elements(By.XPATH, "//main//div//h2/a")]
print(article_headlines)

# Get list of Fintech articles as article link
article_links = [link for link in driver.find_elements(By.XPATH, "//main//div//h2/a")]

article_links_list = []
for link in article_links:
    art_link = link.get_attribute("href")
    article_links_list.append(art_link)
print(article_links_list)

# Get list of Fintech article authors
# As Web element
article_author_element = [author for author in driver.find_elements(By.XPATH, "//a[contains(@href,'author')]")]
# As author name text
article_author_name = [author.text for author in article_author_element]
print(article_author_name)

# Get article author url to author page
article_author_link = []
for author in article_author_element:
    author_link = author.get_attribute("href")
    article_author_link.append(author_link)
print(article_author_link)


#TODO: Add to excel sheet

wb = Workbook()
ws0 = wb.worksheets[0]
ws0.title = 'Techcrunch Fintech Articles and Authors'

nested_list = [article_headlines, article_links_list, article_author_name, article_author_link]

for list in nested_list:
    ws0.append(list)

# # ws0.append(article_headlines, article_links, article_author_name, article_author_link)
# a = pd.DataFrame({'Article Headlines': article_headlines,
#                    'Article Links': article_links,
#                    'Article Author Name': article_author_name,
#                    'Article Author Link': article_author_link})

# df = pd.DataFrame.from_dict(a, orient='index')
# df = df.transpose()

# # ws0.append(df)
# df.to_excel("techcrunch.xlsx")

wb.save("techcrunch.xlsx")

#! Some articles have multiple authors, not sure how to fix