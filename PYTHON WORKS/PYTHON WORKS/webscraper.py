import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information by navigating the HTML structure
    title = soup.title.text
    paragraphs = soup.find_all('p')

    # Print or use the extracted information as needed
    print(f'Title: {title}')
    for index, paragraph in enumerate(paragraphs):
        print(f'Paragraph {index + 1}: {paragraph.text}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
