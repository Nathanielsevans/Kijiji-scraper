import requests
from bs4 import BeautifulSoup
import sys
import json


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
    return: requests.content <request obj> : These are the HTML contents of the requests module
    """

    # Check that the URL is from the first page 
    if "page-" in url:
        print("Please provide a URL from the first page of your Kijiji search query.")
        sys.exit(1)

    # Fetch URL content using requests module. The return will be an HTML Status code as described here: 
    # https://www.restapitutorial.com/httpstatuscodes.html
    result = requests.get(url)

    if result.status_code == 200: # Successfully fetched contents
        return result.content
    else:
        print("Failed to load content from the following URL: {}".format(url))
        sys.exit(1)

def listing_IO(content=False):
    """
    param: content <bool> : Default is set to false so that we don't overwrite our OLD_LISTINGS information
        True means that we have OLD_LISTINGS to write to the backup listings.json file. This will overwrite the file. 
    return: None
    """

    global OLD_LISTINGS # I know it's bad form, but we want to refer to the global OLD_LISTINGS variable.

    # If there is content to write, overwrite the contents of the listings.json backup file.
    if content:
        with open('listings.json', 'w') as f:
            json.dump(OLD_LISTINGS, f)
        f.close()
    else:
        with open('listings.json') as f:
            OLD_LISTINGS = json.load(f)
        f.close()

    return

def parse_site(site_content):
    """
    param: site_content <request.content obj>
    return:
        index <int> : This is the index that contains the first Kijiji listing from the a-href site content list.
        links <list> : List of all the a-href HTML tags from the site.
    """
    
    soup = BeautifulSoup(site_content, 'lxml') # Parse contents of the site using BeautifulSoup
    links = soup.find_all("a") # Find all the ahref tags

    index = 0 # Store the index of the ahref search as we find the first listing

    for link in links:
        if "Sign Up" in link.getText():
            index += 1
            return index, links
        else:
            index += 1

    
def main():
    """
    Main program execution.
    """

    # Init for the Kijiji scrapping process
    listing_IO(False) # Initialize the OLD_LISTINGS global store
    data = site_content(URL) # Load the data from our Kijiji listing URL

    # Parse contents of the site
    start_ind, content = parse_site(data)

    #NOTE: Left off here after finding the first index with a listing on kijiji.

main()





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

counter = 0

#URL2 = "https://www.kijiji.ca/b-bikes/ottawa/bike/page-2/k0c644l1700185?radius=104.0&gpTopAds=y&address=Ottawa%2C+ON&ll=45.421530,-75.697193"
'''