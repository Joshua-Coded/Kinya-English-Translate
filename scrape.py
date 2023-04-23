import requests
from io import BytesIO
from pdfminer.high_level import extract_text

# URL of the PDF file to download
pdf_url = "https://www.rcsdk12.org/cms/lib04/NY01001156/Centricity/Domain/4194/english-kinyarwanda-dictionary.pdf"

# Download the PDF file and save its contents to a BytesIO buffer
response = requests.get(pdf_url)
pdf_buffer = BytesIO(response.content)

# Extract the text from the PDF file using pdfminer
text = extract_text(pdf_buffer)

# Print the extracted text to the console
print(text)