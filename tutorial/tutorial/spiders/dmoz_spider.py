import os
import urllib

import scrapy,re
pictureSrc = "D://pythonProject//new2"
class DemoSprider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.pixiv.net/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename,"wb") as  f:
        #     f.write(response.body)
        for link, t in set(re.findall(r'([a-zA-z]+://[^\s]*(jpg|png|gif))', str(response.body))):

            print(link)
            try:
                urllib.request.urlretrieve(link, saveFlie(link))
            except:
                print('失败')
        # print("66666"+str(response.body))



def saveFlie(path):
    if not os.path.isdir(pictureSrc):
        os.mkdir(pictureSrc)
    pos = path.rindex('/')
    # print(path)
    t = os.path.join(pictureSrc, path[pos + 1:])
    return t