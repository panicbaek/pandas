import requests
from bs4 import BeautifulSoup

url = 'https://m.sports.naver.com/kbaseball/article/109/0005394392'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = soup.select('#comp_news_article > div._article_content')
text = data[0].text
print(text)


