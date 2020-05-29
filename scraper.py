import requests
from bs4 import BeautifulSoup
import sys

#result = requests.get("https://www.kijiji.ca/b-bikes/ottawa/bike/k0c644l1700185?ll=45.421530%2C-75.697193&address=Ottawa%2C+ON&radius=104.0&gpTopAds=y")
#URL2 = "https://www.kijiji.ca/b-bikes/ottawa/bike/page-2/k0c644l1700185?radius=104.0&gpTopAds=y&address=Ottawa%2C+ON&ll=45.421530,-75.697193"

# Base URL to perform Kijiji webscraping on - provide the URL from the first page (not any of the numbered pages)
URL = "https://www.kijiji.ca/b-bikes/ottawa/bike/k0c644l1700185?radius=104.0&gpTopAds=y&address=Ottawa%2C+ON&ll=45.421530,-75.697193"
# List of bike companies to do a keyword search for - case doesn't matter.
BIKE_LIST = [
    "specialized",
    "giant", 
    "cervelo"
]
OLD_LISTINGS = dict() # Store of all the listings that we have already be notified about

# Helper functions

def site_content(url):
    """
    param: url <str> : Kijiji website URL from the first page
    return:
    """

    # Check that the URL is from the first page 
    if "page-" in url:
        print("Please provide a URL from the first page of your Kijiji search query.")
        sys.exit(1)

    # Fetch URL content using requests module. The return will be an HTML Status code as described here: 
    # https://www.restapitutorial.com/httpstatuscodes.html
    result = requests.get(url)
    print("Status: ", result.status_code)

    if result.status_code == 200: # Successfully fetched contents
        return result.content
    else:
        print("Failed to load content from the following URL: {}".format(url))
        sys.exit(1)


'''
for link in links:

    if "Kuota Kryon Road Bike For Sale!" in link.getText():
        print(counter)
    else:
        counter += 1
    

print("Final result: ", links[49])
print('URL: ', links[49]['href'])


print('REST OF THE CONTENT: \n')

print(links)

soup = BeautifulSoup(result.content, 'lxml')
links = soup.find_all("a")
counter = 0
'''