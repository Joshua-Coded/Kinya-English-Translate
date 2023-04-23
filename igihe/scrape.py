import requests
from bs4 import BeautifulSoup
import csv

# Make a request to the webpage
url = 'https://www.scribd.com/book/391694700/Kinyarwanda-English-English-Kinyarwanda-Dictionary-Phrasebook'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the dictionary entries
entries = soup.find_all('div', class_='outer-text')

# Extract the Kinyarwanda and English words and phrases, and save to a CSV file
with open('kinyarwanda_english_dictionary.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Kinyarwanda', 'English'])
    
    for entry in entries:
        kinyarwanda = entry.find('div', class_='src').get_text().strip()
        english = entry.find('div', class_='trg').get_text().strip()
        writer.writerow([kinyarwanda, english])
