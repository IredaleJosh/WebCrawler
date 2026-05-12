# GET URL PAGE, EXTRACT THE QUOTES + AUTHORS, FIND NEXT PAGE
import requests
from bs4 import BeautifulSoup
import time

# STORE START PAGE
URL = "https://quotes.toscrape.com"

# Get the URL page
def get_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

# Extract quotes from the page, combining texts and authors
def get_quotes(soup):
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    page_text = []
    for q, a in zip(quotes, authors):
        page_text.append(q.get_text(strip=True) + " - " + a.get_text(strip=True))
    return " ".join(page_text)

# Find next page
def get_next_page(soup):
    next_btn = soup.find("li", class_="next")
    if next_btn:
        return URL + next_btn.a["href"]
    return None

# Combines Functions to:
# get start page, extract quotes and authors and repeat for each page
def crawl_site(start):
    url = start
    total_pages = {}
    while url:
        print(f"Fetching: {url}")
        page = get_page(url) 
        total_pages[url] = get_quotes(page)
        print("Waiting 6 Seconds")
        time.sleep(6) # POLITNESS WINDOW
        url = get_next_page(page)
    return total_pages