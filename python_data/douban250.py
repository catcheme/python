# 时间：2021/5/23 10:38
import urllib.request

url = "http://movie.douban.com/top250"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)"
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/78.0.3904.108 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(req)
html = response.read().decode("UTF-8")
print(type(html))
print(html)
