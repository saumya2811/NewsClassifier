from bs4 import BeautifulSoup
import requests
import html5lib
article=set()
#daily_news=set()

r = requests.get("https://www.thehindu.com/archive")
htmlcontent=r.content
#print(htmlcontent)
soup = BeautifulSoup(htmlcontent, 'lxml')
#print(soup.prettify())
tables=soup.find_all('ul', class_="archiveMonthList")
#print(tables)
all_links=set()
for link in tables:
    for l in link.find_all('a', href=True):
        all_links.add(l.get('href'))

all_links=sorted(all_links, reverse=True)
n1=len(all_links)
for j in range(n1):
    r2=requests.get(all_links[j])
    htmlcon2=r2.content
    soup2=BeautifulSoup(htmlcon2, 'lxml')
    tables2=soup2.find_all('table', class_="archiveTable")
    daily_news = set()
    for child in tables2:
        for link2 in child.find_all('a', href=True):
            daily_news.add(link2.get('href'))
    daily_news=sorted(daily_news, reverse=True)
    #print(daily_news)
    n=len(daily_news)
    #print(n)
    k=1
    for k in range(n):
        r3 = requests.get(daily_news[k])
        htmlcon3 = r3.content
        soup3 = BeautifulSoup(htmlcon3, 'lxml')
        news_articles = soup3.find_all('ul', class_="archive-list")


        for itr in news_articles:
            for link4 in itr.find_all('a', href=True):
                article.add(link4.get('href'))
                if len(article)>5500:
                    break
            if len(article) > 5500:
                break
        if len(article) > 5500:
            break
    if len(article) > 5500:
        break
article=sorted(article)
print(article)


with open('hindu.txt', 'w') as filehandle:
    for listitem in article:
        filehandle.write('%s\n' % listitem)














