from functions.soup import create_soup
from decorators.decor_logger import decor_logger_parametres
from decorators.decor_logging import decor_logging_parametres

# @decor_logger_parametres(path='log/app_logger.log')
@decor_logging_parametres(path='log/app_logging.log')
def get_articles(URL, url_website, KEYWORDS):

  url_website = url_website
  KEYWORDS_set = KEYWORDS
  soup = create_soup(URL)
  
  articles = soup.find_all('div', class_ = 'tm-article-snippet') 
  result = {}
  for article in articles: 
      hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')  
      hubs = {hub.find('a').text.strip() for hub in hubs}
      if hubs & KEYWORDS_set:        
        article_date = article.find('time')
        article_headers = article.find('h2').find('span')
        article_tag_a = article.find('h2').find('a')
        article_url = url_website + article_tag_a.attrs['href']
        
        result = {'Date': article_date.text, 'Headers': article_headers.text, 'Url': article_url}     
  return result