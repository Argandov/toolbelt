#!/usr/bin/env python3

from newspaper import Article
import sys

url = sys.argv[1]

def parse_article(url):
    article = Article(url)
    article.download()
    article.parse()
    
    date = article.publish_date
    authors = article.authors
    raw_article = article.text
    title = article.title

    text = article.text
    
    return date, raw_article, title, authors, text

date, raw_article, title, authors, text = parse_article(url)

print(authors)
print(text)
