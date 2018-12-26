import requests
import re
from bs4 import BeautifulSoup
def getHTMLText(url):
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    try:
        r = requests.get(url,headers=send_headers)
        #r=request.get(url)
        r.raise_for_status()
        print(r.status_code)
        r.encoding='utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup,allUniv):
    data = soup.find_all('div',{'class':re.compile('shadow-dark')})
    for div in data:
        singleUniv=[]
        divl = div.find('div',{'style':'margin-left:2.5rem;'})
        rank = divl.get_text().strip()
        singleUniv.append(rank.split(' ')[0])
        h3=div.find("h3")
        singleUniv.append(h3.get_text().strip())
        ldiv=div.find_all('div',{'style':'padding-right:0.5rem;'})
        singleUniv.append(ldiv[0].strong.string)
        singleUniv.append(ldiv[1].strong.string)
        allUniv.append(singleUniv)
def printUnivList(allUniv):
    print(
