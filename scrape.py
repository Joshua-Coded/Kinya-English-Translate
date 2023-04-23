import requests
from bs4 import BeautifulSoup

url = "http://morganinafrica.blogspot.com/2006/02/rwandan-dictionary-kinyarwanda-english.html"

# Send a GET request to the URL
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the dictionary entries
table = soup.find('table', {'class': 'tr-caption-container'})

# Extract the rows of the table
rows = table.find_all('tr')

# Iterate over the rows and extract the Kinyarwanda-English pairs
for row in rows:
    # Get all the table cells in this row
    cells = row.find_all('td')
    
    # Check if this row has two cells (Kinyarwanda and English)
    if len(cells) == 2:
        kinyarwanda = cells[0].get_text().strip()
        english = cells[1].get_text().strip()
        
        # Do something with the extracted Kinyarwanda-English pair
        print(f'Kinyarwanda: {kinyarwanda}, English: {english}')