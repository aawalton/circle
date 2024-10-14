# The Wandering Inn Table of Contents Scraper

This project scrapes the table of contents from The Wandering Inn web novel and saves it to a CSV file.

## Setup and Running

To set up and run the scraper, follow these steps:

1. Create a virtual environment:
   ```
   python3 -m venv wandering_inn_env
   ```

2. Activate the virtual environment:
   ```
   source wandering_inn_env/bin/activate
   ```

3. Install the required packages:
   ```
   pip install requests beautifulsoup4
   ```

4. Run the scraper:
   ```
   python src/table-of-contents.py
   ```

This will create a CSV file named `wandering_inn_chapters.csv` with the scraped chapter information.

