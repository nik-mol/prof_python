import requests
from bs4 import BeautifulSoup 
import re


KEYWORDS_set = {'Дизайн', 'Фото', 'Web', 'Python', 'Биология'}
KEYWORDS_list = ['Дизайн', 'Фото', 'Web', 'Python', 'СДЭК', 'время']
HEADERS = {'User-Agent': 'Chrome'}

url_website = 'https://habr.com'
url_page = 'https://habr.com/ru/all/'
response = requests.get(url_page, headers=HEADERS)
text = response.text

soup = BeautifulSoup(text, features = 'html.parser')

articles = soup.find_all('div', class_ = 'tm-article-snippet')
# print(len(articles))
for article in articles:
 
#------------------------------------TASK2------------------------------------------------ 
    full_info_articles = article.find_all('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')  
    full_info_articles_list = [info_article.find('p').text for info_article in full_info_articles]


    full_info_articles_str = (' ').join(full_info_articles_list).strip()            # -----del punctuation--------------
    new_full_info_articles_str = re.sub(r',.!?', '', full_info_articles_str)        # -----del punctuation--------------
    new_full_info_articles_list = new_full_info_articles_str.split()                # -----del punctuation--------------

    if set(KEYWORDS_list) & set(new_full_info_articles_list):
        article_date = article.find('time')
        article_headers = article.find('h2').find('span')
        article_tag_a = article.find('h2').find('a')
        article_url = url_website + article_tag_a.attrs['href']    
        print(f'Date: {article_date.text} --> Headers: {article_headers.text} --> Url: {article_url}')

        print('============================')

# ------------------------------------TASK1------------------------------------------------------   
    hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')  
    hubs = {hub.find('a').text.strip() for hub in hubs}
    if hubs & KEYWORDS_set:        
        article_date = article.find('time')
        article_headers = article.find('h2').find('span')
        article_tag_a = article.find('h2').find('a')
        article_url = url_website + article_tag_a.attrs['href']    
        print(f'Date: {article_date.text} --> Headers: {article_headers.text} --> Url: {article_url}')