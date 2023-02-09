import requests
from bs4 import BeautifulSoup

HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control':
    'max-age=0',
    'Connection':
    'keep-alive',
    'Cookie':
    'BITRIX_SM_GUEST_ID=22830; BITRIX_SM_LAST_VISIT=03.08.2022%2013%3A22%3A58; BITRIX_SM_limit=12; BITRIX_SM_SALE_UID=1df354d2c154e52ca5c1718b9b08ec52; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A2%2C%22EXPIRE%22%3A1659560340%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_uid=1659522179418078142; _ym_d=1659522179; _ym_isad=2; _ym_visorc=w; BX_USER_ID=81abfa8ea3899850dc951bdd9535a01b; PHPSESSID=c9GjWIcW6nlrdZQl1OXPC1ymB8zyr7O8',
    'Host':
    'elektrokomplekt67.ru',
    'sec-ch-ua':
    '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'Sec-Fetch-Dest':
    'document',
    'Sec-Fetch-Mode':
    'navigate',
    'Sec-Fetch-Site':
    'cross-site',
    'Sec-Fetch-User':
    '?1',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}


def create_soup(URL):
    """Create soup
  """
    res = requests.get(URL, headers=HEADERS)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')
    return soup