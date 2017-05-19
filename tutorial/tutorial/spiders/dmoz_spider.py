import scrapy
class DemoSprider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://my.oschina.net/xueba/blog/492948"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename,"wb") as  f:
        #     f.write(response.body)
        print("66666"+str(response.body))