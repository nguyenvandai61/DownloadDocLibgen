from bs4 import BeautifulSoup as bs
import io
import os
import urllib3
import requests
from urllib import parse



def scrape_and_run(topic, n):
    # scrape on goodreads.com using desire genre type or key word
    # and save the titles and autors in a csv file
    link = "http://libgen.is/search.php?lg_topic=libgen&open=0&view=simple&phrase=1&column=def&sort=year&sortmode=DESC"+"&req="+topic+"&res="+str(n)
    page = requests.get(link)
    soup = bs(page.content, 'html.parser')

    nameArr = []
    linkArr = []

    # Tim truoc roi download
    for i in range(2, n+2):
            
        l = "table.c >tr:nth-child("+str(i)+") > td:nth-child(10) > a"
        print(l)
        a = soup.select(l)
        print(a)
        linkdir = a[0].get("href")
        linkArr.append(linkdir)
        nameArr.append(i)
    
    download(nameArr, linkArr, topic)
    
    


    


def download(nameArr, linkArr, topic):
    file_dir = os.getcwd() + "\\download\\" + topic

    # check if the desire genre path exists
    # create a new one if it doesnt
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    names_urls = zip(nameArr, linkArr)

    

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


# if __name__ == '__main__':
#     topic = 'typescript'
#     scrape_and_run(topic)
