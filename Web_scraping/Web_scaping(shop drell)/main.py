from functions.catalog_instrument import get_catalog_instrument
from functions.drill import get_drill

with open('file/url.text', 'r') as file:
    url_web = file.readline().strip()
    url_page_drill = file.readline().strip()

if __name__ == '__main__':
    print(get_catalog_instrument(url_web))
    print(get_drill(url_page_drill))