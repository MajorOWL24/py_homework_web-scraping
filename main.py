from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://habr.com/ru/all')


dates = r.html.find('time')
names = r.html.find('h2.tm-article-snippet__title.tm-article-snippet__title_h2 a span')
links = r.html.find('h2.tm-article-snippet__title.tm-article-snippet__title_h2 a')

for i in range(0, len(dates)):
    link = links[i].attrs['href']
    if link.startswith("/"):
        link = 'https://habr.com' + link
    text = dates[i].text
    #text = dates[i].attrs['title']
    print(text, names[i].text, link)
