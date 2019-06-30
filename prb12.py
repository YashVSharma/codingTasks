from googlesearch import search
import os
import pyqrcode

a=input("Enter search")

li=[]
li1=[]
for i in search(a, tld='com', lang ='en', num=5, start=0, stop=2, pause=2.0):
  li.append(i)
print(li)

for i in range(len(li)):
  url=pyqrcode.create(li[i])
  url.svg("rty%d"%i,scale=8)
  #os.system("cp qwerty%d"%i+" /var/www/html")
  print(url.terminal())
