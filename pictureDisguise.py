import os,urllib.request
import re
import socket
import sys

pictureSrc = "D://pythonProject//new"

def saveFlie(path):
    if not os.path.isdir(pictureSrc):
        os.mkdir(pictureSrc)
    pos = path.rindex('/')
    # print(path)
    t = os.path.join(pictureSrc,path[pos+1:])
    return t

url = 'http://www.pixiv.net/member.php?id=652196'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36'}
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

data = response.read()
# print(data)
for link, t in set(re.findall(r'([a-zA-z]+://[^\s]*(jpg|png|gif))', str(data))):

    print(link)
    try:
        urllib.request.urlretrieve(link, saveFlie(link))
    except:
        print('失败')