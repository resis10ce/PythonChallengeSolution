import urllib.request
import pickle

req=urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
res=req.read().decode("utf-8")


import pickle              # import module first

f = open('banner.p', 'r')   # 'r' for reading; can be omitted
mydict = pickle.load(f)         # load file content as mydict
f.close()                       

print(mydict)

f = open('banner.p', 'br')
mydict = pickle.load(f)  

for line in y:
  for t in line:
    print(t[0]*t[1], end = '')
  print("")