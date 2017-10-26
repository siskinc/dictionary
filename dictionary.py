from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib3
import re

http = urllib3.PoolManager()

def check_contain_chinese(check_str):
    return all('\u4e00' <= char <= '\u9fff' for char in check_str)

def getListOfEnglish(p):
    for pp in p:
        a = re.findall(r'<span style="font-weight: bold; color: #959595; margin-right: .5em; width : 36px; display: inline-block;">(.*?)</span>',str(pp),re.M)
        b = re.findall(r'<a class="search-js" .*>(.*?)</a>',str(pp),re.M)
        if len(a) != 0 and len(b) != 0:
            yield [str(a[0])]+[str(c) for c in b]

def chinese_option(soup):
    p = soup.find_all('p',attrs={'class':'wordGroup'})
    rets = getListOfEnglish(p)
    for ret in rets:
        ret[0] = ret[0]+'  '+ret[1]
        del ret[1]
        yield ret


def getYoudao(word):
    if isinstance(word,str):
        url =  'http://dict.youdao.com/w/'+quote(word)+'/#keyfrom=dict2.top'
    else:
        raise Exception('Please input a word ,it must a str.')
    body = http.request('GET',url)
    soup = BeautifulSoup(body.data.decode('utf-8'),'html.parser')
    if body.status == 200:
        if check_contain_chinese(word):
            return chinese_option(soup)
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
        word = word.replace(' ','%20')
        meanings = getYoudao(word)
        if not check_contain_chinese(word):
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
        else:
            count = 0
            for meaning in meanings:
                space = (len(meaning[0].split('.')[0])+2) * ' '
                for m in meaning:
                    if count == 0:
                        print(m)
                    else:
                        m = space + m
                        print(m)
                    count += 1

