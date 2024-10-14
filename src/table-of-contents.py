import requests
from bs4 import BeautifulSoup
import csv

# Erin would probably say something like:
print("Ooh, magic internet scraping! Let's gather all those chapter thingies!")

# URL of the table of contents
url = "https://wanderinginn.com/table-of-contents/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the chapter links
chapters = soup.find_all('a', class_='chapter-link')

# Prepare a list to store chapter info
chapter_info = []

# Extract title and link for each chapter
for chapter in chapters:
    title = chapter.text.strip()
    link = chapter['href']
    chapter_info.append([title, link])

# Erin-style commentary:
print(f"Wow! We found {len(chapter_info)} chapters! That's a lot of words!")

# Save the information to a CSV file
with open('wandering_inn_chapters.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])  # Write header
    writer.writerows(chapter_info)

print("All done! The chapters are now in a magical CSV scroll. Time for cookies!")

