import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url = "https://example.com"

# Send a request to the webpage and get the HTML response
response = requests.get(url)

# Use BeautifulSoup to parse the HTML response
soup = BeautifulSoup(response.content, "html.parser")

# Find the first link in the webpage
first_link = soup.find("a")["href"]

# Print the first link
print(first_link)