import requests
from bs4 import BeautifulSoup



HEADERS =  {'User-Agent': 'Chrome'}

def create_soup(URL):
    """Create soup
  """
    response = requests.get(URL, headers=HEADERS)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    return soup