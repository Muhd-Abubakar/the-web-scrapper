import requests
from bs4 import BeautifulSoup

# Print a message indicating the start of the web scraping process
print("Starting web scraping...")

# URL of the website to scrape
url = "https://example.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
   
    # Find all anchor tags on the page
    links = soup.find_all("a")
    print(f"Found {len(links)} links on {url}")
    
    # Iterate over the links and print their titles and href attributes
    for index, link in enumerate(links, start=1):
        href = link.get("href")
        # Check if the href attribute starts with "http://" or "https://"
        if href.startswith("http://") or href.startswith("https://"):
            title = link.text.strip()
            # Print the link title and href if the title is not empty
            if title:
                print(f"{index}. {title} - {href}")
            else:
                print(f"{index}. No title found - {href}")

else:
    # Print an error message if the request was not successful
    print(f"Failed to connect to {url}, {response.status_code}")

# Print a message indicating the completion of the web scraping process
print("Web scraping completed!")
