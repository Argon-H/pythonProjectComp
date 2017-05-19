from urllib import request, parse
import os


pathSrc = "D://123//new"
def saveFlie(path):
    if not os.path.isdir(pathSrc):
        os.mkdir(pathSrc)
    pos = path.rindex('/')
    # print(path)
    t = os.path.join(pathSrc,path[pos+1:])
    return t


url = "https://item.jd.com/1371193.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36'}

requestP = request.Request(url=url,headers=headers)

data = {"callback": "call52925",
        "p": "504000",
        "pin": "齐采测试01",
        "uuid": "1491991750553540124274",
        "lid": "19",
        "lim": "10",
        "skus": "",
        "ck": "ipLoction",
        "ec": "utf - 8",
        "c1": "652",
        "c2": "654",
        "c3": "832",
        "hi": "brand:, price:, page: 1",
        "_": "1494840188237"}

data = parse.urlencode(data)

url2 = url + '?' + data
# 跟post不同的只有这一句，使用?把url和data的内容连接起来，结果是https://api.douban.com/v2/book/user/ahbei/collections?status=read&rating=3&tag=%E5%B0%8F%E8%AF%B4
url2="https://www.baidu.com"
response = request.urlopen(url2)

apicontent = response.read()

print("text:"+str(apicontent))
