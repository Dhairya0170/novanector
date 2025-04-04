import requests
from bs4 import BeautifulSoup

# Target URL
URL = "www.quora.com"  # Replace with the site you want to scrape

# Send a GET request
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all article titles (modify this based on the website's structure)
    titles = soup.find_all("h2")  # Adjust tag (e.g., "h1", "h3", "p", etc.)

    # Print extracted titles
    for idx, title in enumerate(titles, start=1):
        print(f"{idx}. {title.get_text(strip=True)}")
else:
    print("Failed to retrieve the website")

