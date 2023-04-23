import requests
from io import BytesIO
from pdfminer.high_level import extract_text
import csv

# URL of the PDF file to download
pdf_url = "https://www.rcsdk12.org/cms/lib04/NY01001156/Centricity/Domain/4194/english-kinyarwanda-dictionary.pdf"

# Download the PDF file and save its contents to a BytesIO buffer
response = requests.get(pdf_url)
pdf_buffer = BytesIO(response.content)

# Extract the text from the PDF file using pdfminer
text = extract_text(pdf_buffer)

# Split the text into rows based on newlines
rows = text.split('\n')

# Open a new CSV file for writing
with open('english-kinyarwanda-dictionary.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write each row of the text to the CSV file
    for row in rows:
        writer.writerow([row])