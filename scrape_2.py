import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

file=open('hindu.txt', 'r')
content=file.readlines()
Content_table=[[]]
n=len(content)
j=0
for line in content:
#trim1=set()
    r=requests.get(line)
    page=r.content
    soup=BeautifulSoup(page, 'lxml')
    articles=soup.find('div', class_="article")
    article_title=""
    tag=""
    body=""
    li = []

    if (soup.find('div',{'class':'article'})):
        articles = soup.find('div', class_="article")
        #if (articles.find('div', {'class':'paywall'}) and articles.find('h1', {'class': 'title'}) and articles.find('a',{'class': 'section-name'}) ):
        try:
            article_title=articles.find('h1', class_="title").text
            #print(article_title)
        except:
            article_title="None"

        try:
            tag=articles.find('a', class_="section-name").text
            #print(tag)
        except:
            tag="None"

        try:
            body = articles.find('div', class_="paywall").text
            #print(body)
        except:
            body="None"

    li.append(article_title)
    li.append(tag)
    li.append(body)
    #print(li[1])
    Content_table.append(li)
    print(j)
    j=j+1


df = pd.DataFrame(Content_table)
df.to_csv('hindu.csv', index=True, header=["Title", "Tag", "Body"])

