import newspaper
from newspaper import Article
import nltk


url='https://www.bbc.com/news/world-asia-india-68015106'
article = Article(url)
article.download()
article.parse()
print (article.title)
print(article.text)

