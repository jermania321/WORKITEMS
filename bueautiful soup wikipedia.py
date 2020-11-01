import urllib.request,urllib.parse,urllib.error
import ssl
from bs4 import BeautifulSoup
fh=urllib.request.urlopen("https://en.wikipedia.org/wiki/Illuminati").read()
soup=BeautifulSoup(fh,'html.parser')


#aganist the ssl certificate error
ctx=ssl.create_default_context
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#ssl????????????????????????/


tags=soup('a')
for tag in tags:
    print(tag.get('href',None))