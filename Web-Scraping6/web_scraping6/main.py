import requests
from bs4 import BeautifulSoup


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

url="https://finans.mynet.com/kripto-para/"
sayfa=requests.get(url,headers=headers)
icerik=BeautifulSoup(sayfa.content,"html.parser")

adi=icerik.find_all("div",{"class":"flex align-items-center kripto-first-td-m"})


for i in adi:
    i=i.text.strip()
    print(i)
