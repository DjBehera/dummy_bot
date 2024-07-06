import requests

url = "http://httpbin.org/json"

## comment added from test_branch
## Added some new comments
### Added from feature branch

r = requests.get(url,url,url)
a = 3


c = 90
d = a * c
print("Response code : ",r.status_code)
print("Response headers : \n", r.headers)
print("Response Content : \n",r.text)
