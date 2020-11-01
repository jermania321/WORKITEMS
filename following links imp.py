import urllib.request, urllib.parse,urllib.error
import ssl
from bs4 import BeautifulSoup
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
x= "http://py4e-data.dr-chuck.net/known_by_Melody.html"
pos=0
count=0
c=int(count)
p=int(pos)
while c<7:
    p=0
    fh=urllib.request.urlopen(x,context=ctx).read()
    soup=BeautifulSoup(fh,"html.parser")
    tags=soup("a")
    for tag in tags:
        p=p+1
        if p is 18:
            x=tag.get("href",None)
           
            print(x)
            c=c+1
