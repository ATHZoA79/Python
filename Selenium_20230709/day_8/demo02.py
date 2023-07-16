import requests
from bs4 import BeautifulSoup

# Step 1: Send a search query
search_query = "web scraping"
url = f"https://www.google.com/search?q={search_query}"
# url = "https://getbootstrap.com/"
response = requests.get(url)

# Step 2: Retrieve the search results page
search_results_page = response.text

# Step 3: Parse the HTML
soup = BeautifulSoup(search_results_page, 'html.parser')

# Step 4: Extract the desired information
search_results = soup.find_all('div', class_='g')

for result in search_results:
    # Extract the title and URL of each search result
    title = result.find('h3').text
    url = result.find('a')['href']
    
    # Print the extracted information
    print("Title:", title)
    print("URL:", url)
    print()

# Step 5: Process the extracted data (not shown in this example)
