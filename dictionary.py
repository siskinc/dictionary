from bs4 import BeautifulSoup
import urllib3
import re
import os

http = urllib3.PoolManager()

def getYoudao(word):
    if isinstance(word,str):
        url =  'http://dict.youdao.com/w/'+word+'/#keyfrom=dict2.top'
    else:
        raise Exception('Please input a word ,it must a str.')
    body = http.request('GET',url)
    soup = BeautifulSoup(body.data.decode('utf-8'),'html.parser')
    if body.status == 200:
        div = soup.find_all(id = 'phrsListTab')
        if len(div) != 0:
            return re.findall(r'^<li>(.+?)</li>$',str(div[0]),re.M)
        else:
            return None
    else:
        print('网络不通')
        return None


if __name__ == '__main__':
    while True:
        word = input('>>>')
        meanings = getYoudao(word)
        for meaning in meanings:
            meaning = meaning.split('；')
            count = 0
            space = (len(meaning[0].split('.')[0])+2) * ' '
            for m in meaning:
                if count == 0:
                    print(m)
                else:
                    m = space + m
                    print(m)
                count += 1

