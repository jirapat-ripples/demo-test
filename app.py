#Web Scraping using BeautifulSoup and Requests
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    url = input("Enter the URL of the website to scrape: ")
    soup = scrape_website(url)
    
    if soup:
        print(f"Successfully scraped {url}")
        # Example: Print the title of the page
        title = soup.title.string if soup.title else "No title found"
        print(f"Title of the page: {title}")
        
        # Example: Print all links on the page
        links = soup.find_all('a')
        print("Links found on the page:")
        for link in links:
            href = link.get('href')
            if href:
                print(href)

if __name__ == "__main__":
    main()
# Run the script

