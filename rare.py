import urllib.request as url
k=url.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
print(k.read())