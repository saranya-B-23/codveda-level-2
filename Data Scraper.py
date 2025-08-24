"""
Level 2
Task 2: Data Scraper
Develop a Web Scraper to extract specific data from a website (eg., news headlines, product prices).
"""

import requests
from bs4 import BeautifulSoup
import csv

# Retrieve the web page content
url = 'https://www.bbc.com/news'
response = requests.get(url)
if response.status_code != 200:
    print(f'Failed to retrieve the webpage. Status code:{response.status_code}')
    exit()

# Parse the HTMl content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract specific data (eg., news headlines)
headlines = []
for item in soup.find_all('h3', class_='gs-c-promo-heading__title'):
    title = item.get_text(strip=True)
    link = item.find_parent('a')['href']
    if not link.startswith('http'):
        link = 'https://www.bbc.com' + link
    headlines.append({'title': title, 'link': link})

# Save the scraped data into csv file
csv_file = 'news_headlines.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link'])
    writer.writeheader()
    for headline in headlines:
        writer.writerow(headline)

print(f"Scraped data has been saved to {csv_file}")



