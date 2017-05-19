import json
import urllib.request


url = "https://jipiao.jd.com/search/queryFlight.action?" \
      "depCity=%E5%8C%97%E4%BA%AC&arrCity=%E5%B9%BF%E5%B7%9E&depDate=2017-05-15" \
      "&arrDate=2017-05-15&queryModule=1&lineType=OW" \
      "&queryType=listquery&queryuuid=&uniqueKey=&sourceId=&arrTime=";

urlCity = "https://jipiao.jd.com/search/getQueryFlightHistory.action"
requestC = urllib.request.Request(urlCity)
responseC = urllib.request.urlopen(requestC)
dataC = responseC.read()
# print(dataC)

url = "https://dx.3.cn/desc/2461934?cdn=2&callback=showdesc"
request = urllib.request.Request(url);
response = urllib.request.urlopen(request);
data = response.read()
a = json.loads(data)
print  (a['data'])



