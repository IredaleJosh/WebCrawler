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
# stores in format with url, quotes, raw text and next page
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
    total_pages = []
    # Check for Error Codes
    response = requests.get(url)
    if response.status_code != 200:
        return total_pages
    while url:
        print(f"Fetching: {url}")
        # Main
        page = get_page(url) 
        quotes = get_quotes(page)
        curr_url = url
        url = get_next_page(page)
        # Infinite Loop
        if url == curr_url:
            url = None
        total_pages.append({
            "page" : curr_url,
            "text": quotes,
            "next page" : url
        })
        print("Waiting 6 Seconds")
        time.sleep(6) # POLITNESS WINDOW
    return total_pages

# crawl a single page
def crawl_single_page(start):
    single_page = {}
    print(f"Fetching: {start}")
    page = get_page(start)
    single_page[start] = get_quotes(page)
    return single_page