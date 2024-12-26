from bs4 import BeautifulSoup
import requests, json

url = "https://www.lemonde.fr/signataires/manon-romain/"
selection = "div.thread"

req = requests.get(url)
html = BeautifulSoup(req.content)

articles = html.select(selection)

articles_data = []

for article in articles:
    articles_data.append({
        "name": article.select_one("h3.teaser__title").text, 
        "authors": [author.text for author in article.select(".article__author-link")],
        "url": article.select_one("a.teaser__link").get("href"), 
    })
    
with open("articles.json", "wt") as f:
    f.write(json.dumps(articles_data)) 