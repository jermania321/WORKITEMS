#A fun prg try if u want :)
import urllib.request,urllib.parse,urllib.error
fh=urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
count= dict()

for line in fh:
    nel=line.decode().strip()
    for word in nel:
        count[word]=count.get(word,0) + 1
print(count)       

