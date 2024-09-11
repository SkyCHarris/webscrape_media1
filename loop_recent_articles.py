
# Loop Through Recent Articles for Article Link, Author Name, Author Page

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
from openpyxl import Workbook

# Set up a Selenium WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to The Defiant website
url_defi = "https://thedefiant.io/news/DeFi"
url_cefi = "https://thedefiant.io/news/cefi"
url_tradfi_fintech = "https://thedefiant.io/news/tradfi-and-fintech"
url_blockchains = "https://thedefiant.io/news/blockchains"
url_nfts_web3 = "https://thedefiant.io/news/nfts-and-web3"
url_people = "https://thedefiant.io/news/people"
url_markets = "https://thedefiant.io/news/markets"
url_regulation = "https://thedefiant.io/news/regulation"
url_hacks = "https://thedefiant.io/news/hacks"
url_research_opinion = "https://thedefiant.io/news/research-and-opinion"
url_pressreleases = "https://thedefiant.io/news/press-releases"
url_sponsored = "https://thedefiant.io/news/sponsored"
url_deepnewz = "https://thedefiant.io/news/deep-newz"

url_list = [url_defi, url_cefi, url_tradfi_fintech, url_blockchains, url_nfts_web3, url_people,
url_markets, url_regulation, url_hacks, url_research_opinion, url_pressreleases, url_sponsored, url_deepnewz ]

for url in url_list:
    driver.get(url)

    # Wait for the page to load 
    time.sleep(1) 

    # Get list of Recent Articles as web elements
    links_list = [link for link in driver.find_elements(By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a")]
    print(links_list)

    # Get list of Recent Articles as links
    recent_article_links = []
    for link in links_list:
        attr_link = link.get_attribute("href")
        recent_article_links.append(attr_link)
    print(recent_article_links)

    # Loop through links
    author_links = []
    author_names = []
    for link in recent_article_links:
        driver.get(link)
        # nav_to_article = driver.get(recent_article_links[0]) # Navigate to first DeFi Recent Articles link
        author_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//article/div[2]/a[@href]"))).get_attribute("href")  # Get author link
        author_name = driver.find_element(By.XPATH, "//article/div[2]/a[@href]").text
        author_links.append(author_link)
        author_names.append(author_name)
        
        # Nested list of article link, author name, and author link
        nested_list = [recent_article_links, author_names, author_links]
        
        wb = Workbook() # Creates new workbook
        ws = wb.active  # Get active sheet (default 1st)

        # Append sublists to separate rows
        for sub_list in nested_list:
            ws.append(sub_list)
    print(author_links)
    print(author_names)
    time.sleep(3)

wb.save("test1.xlsx")    # Save workbook










