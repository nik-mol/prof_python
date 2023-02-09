from functions.articles import get_articles

KEYWORDS_set = {'Дизайн', 'Фото', 'Web', 'Python', 'Биология','Браузеры', 'Биология', 'Видеотехника'}

with open('url.text', 'r') as file:
    url_website = file.readline().strip()
    url_page = file.readline().strip()  
    

if __name__ == '__main__':
  get_articles(url_page, url_website, KEYWORDS_set)