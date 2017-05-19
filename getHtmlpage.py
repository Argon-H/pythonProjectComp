import urllib.request
url = "http://www.douban.com/"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

data = response.read()
data = data.decode('utf-8')

print(data)

print(type(response))
print("url: "+response.geturl())
print(response.info())
print(response.getcode())