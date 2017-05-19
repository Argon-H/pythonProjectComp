import urllib.request


def saveFile(data):
    path = 'D://pythonProject//douban.out'
    f = open(path,'wb')
    print(data)
    f.write(data)
    # f.closed()



url = 'http://www.douban.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36'}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

data = response.read()
saveFile(data)

data = data.decode('utf-8')

print(data)

print(type(response))
print("url: "+response.geturl())
print(response.info())
print(response.getcode())