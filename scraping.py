from bs4 import BeautifulSoup
import requests

baidu=requests.get('https://www.douyin.com').content
soup=BeautifulSoup(baidu, 'html.parser')

links=soup.findAll('a')
print(links)

for link in links:
    print(link.string)