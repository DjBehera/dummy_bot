import requests

url = "http://httpbin.org/json"

## comment added from test_branch
## Added some new comments

r = requests.get(url)
a = 90
c = 90
d = a * c
print("Response code : ",r.status_code)
print("Response headers : \n", r.headers)
print("Response Content : \n",r.text)
