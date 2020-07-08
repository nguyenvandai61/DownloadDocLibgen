from bs4 import BeautifulSoup as bs
import io
import os
import urllib3
import requests
from urllib import parse

class BookLink:
    def __init__(self, nameArr, linkArr, sizeArr):
        self.nameArr = nameArr
        self.linkArr = linkArr
        self.sizeArr = sizeArr

def scrape_and_run(topic, n=3, var="title"):
    # scrape on goodreads.com using desire genre type or key word
    # and save the titles and autors in a csv file
    link = "http://libgen.is/search.php"
    print(var)
    page = requests.get(link, {
        "lg_topic": "libgen",
        "open": 0,
        "view": "simple",
        "phrase": 1,
        "column": "def",
        "sort": var,
        "sortmode": "DESC",
        "req": topic,
        "res": str(n)
    })
    soup = bs(page.content, 'html.parser')

    nameArr = []
    linkArr = []
    sizeArr = []

    # Tim truoc roi download
    for i in range(2, n+2):
        # Add link download
        l = "table.c >tr:nth-child("+str(i)+") > td:nth-child(10) > a"
        a = soup.select(l)
        linkdir = a[0].get("href")
        linkArr.append(linkdir)
        # Add book title
        l = "table.c > tr:nth-child("+str(i)+") > td:nth-child(3) > a"
        a = soup.select(l)
        nameArr.append(a[0].text)
        # Add size of book
        l = "table.c > tr:nth-child("+str(i)+") > td:nth-child(8)"
        a = soup.select(l)
        print(a)
        sizeArr.append(a[0].text)
        
    return BookLink(nameArr, linkArr, sizeArr)
    
    


    


def download(BookLink, topic):
    file_dir = os.getcwd() + "\\download\\" + topic

    # check if the desire genre path exists
    # create a new one if it doesnt
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    names_urls = zip(BookLink.nameArr, BookLink.linkArr)

    

    for name, url in names_urls:
        book_page = requests.get(url)
        soup = bs(book_page.content, 'html.parser')
        linka = soup.select("h2>a")
        linkdown = linka[0].get("href")
        print("co link douww")
        print(linkdown)
        rq = urllib3.PoolManager(num_pools=2)
        r = rq.request('GET', linkdown, preload_content=False)
        # tim ten file
        i = linkdown.rfind('/')
        name = parse.unquote(linkdown[i:])

        with open(file_dir+name, 'wb') as out:
            while True:
                data = r.read()
                if not data:
                    break
                out.write(data)

        r.release_conn()


if __name__ == '__main__':
    topic = 'typescript'
    scrape_and_run(topic, 4, "year")
