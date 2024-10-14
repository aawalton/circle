import requests
from bs4 import BeautifulSoup
import csv

# Erin would probably say something like:
print("Ooh, magic internet scraping! Let's gather all those chapter thingies!")

# URL of the table of contents
url = "https://wanderinginn.com/table-of-contents/"

# Define headers to make the request look more like a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://wanderinginn.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Send a GET request to the URL with the defined headers
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table of contents div
toc = soup.find('div', id='table-of-contents')

# Debug: Print the entire parsed HTML if toc is None
if toc is None:
    print("Couldn't find the table of contents. Here's the parsed HTML:")
    print(soup.prettify())
else:
    # Prepare a list to store chapter info
    chapter_info = []

    # Extract title and link for each chapter
    for volume in toc.find_all('div', class_='volume-wrapper'):
        volume_title = volume.find('h2').text.strip()
        for chapter in volume.find_all('div', class_='chapter-entry'):
            web_cell = chapter.find('div', class_='body-web')
            if web_cell:
                link = web_cell.find('a')
                if link:
                    title = link.text.strip()
                    href = link['href']
                    chapter_info.append([volume_title, title, href])

    # Erin-style commentary:
    print(f"Wow! We found {len(chapter_info)} chapters! That's a lot of words!")

    # Save the information to a CSV file
    with open('wandering_inn_chapters.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Volume', 'Title', 'Link'])  # Write header
        writer.writerows(chapter_info)

    print("All done! The chapters are now in a magical CSV scroll. Time for cookies!")
