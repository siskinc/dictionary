from bs4 import BeautifulSoup
import urllib3
import re
import os

http = urllib3.PoolManager()

def getYoudao(word):
    if isinstance(word,str):
        url =  'http://dict.youdao.com/w/'+word+'/#keyfrom=dict2.top'
    else:
        raise Exception('Please input a word ,it must  a str.')
    body = http.request('GET',url)
    soup = BeautifulSoup(body,'html.parser')
    print(body.status)
    print(str(soup))
    div = soup.find_all(id = 'phrsListTab')
    print(div)
    if len(div) != 0:
        return re.findall(r'^<li>(.+?)</li>$',str(div[0]),re.M)
    else:
        return None



if __name__ == '__main__':
    while True:
        word = input('>>>')
        print(getYoudao(word))