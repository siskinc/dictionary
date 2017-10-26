from bs4 import BeautifulSoup
import urllib3
from re import match,findall,M

def a():
    http = urllib3.PoolManager()

    ret = http.request('GET','http://dict.youdao.com/w/%E5%BC%80%E5%BF%83/#keyfrom=dict2.top')  
    print(ret.status)
    soup = BeautifulSoup(ret.data.decode('utf-8'),'html.parser')
# a = soup.find_all('a',attrs={'class':'search-js'})
# print(a)
# print(a[0].parent.previous_sibling)
# a = soup.find_all('span')
# print(a)
# print(a[0].parent.previous_sibling)
# for aa in a:
#     print(aa.span.string+aa.a.string)

    p = soup.find_all('p',attrs={'class':'wordGroup'})
    for pp in p:
        a = findall(r'<span style="font-weight: bold; color: #959595; margin-right: .5em; width : 36px; display: inline-block;">(.*?)</span>',str(pp),M)
        b = findall(r'<a class="search-js" .*>(.*?)</a>',str(pp),M)
        if len(a) != 0 and len(b) != 0:
            yield [str(a[0])]+[str(c) for c in b]


c = a()
for cc in c:
    cc[0] = cc[0]+'  '+cc[1]
    del cc[1]
    print(cc)