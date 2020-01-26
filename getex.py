import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = {
    "sm": "top_hty",
    "fbm": "0",
    "ie": "utf8",
    "query": "스타킹"
}

params = urllib.parse.urlencode(values)
# values 의 query 파라미터의 "스타킹" 단어를 인코딩하여 params 의 변수에 값을 저장.
url = api + "?" + params
# api 변수와 values 변수의 값을 더해서 url 변수에 저장.

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

# https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%8A%A4%ED%83%80%ED%82%B9