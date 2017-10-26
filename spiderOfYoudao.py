from bs4 import BeautifulSoup
import urllib3
from re import match,findall,M

http = urllib3.PoolManager()

ret = http.request('GET','http://dict.youdao.com/w/moon/#keyfrom=dict2.top')
print(ret.status)
soup = BeautifulSoup(ret.data.decode('utf-8'),'html.parser')
a = soup.find_all(id='phrsListTab')
a2 = str(a[0])
print(findall(r'^<li>(.+?)</li>$',a2,M))