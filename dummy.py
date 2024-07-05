import requests

url = "http://httpbin.org/json"

## comment added from test_branch

r = requests.get(url)
a = 4
print("Response code : ",r.status_code)
print("Response headers : \n", r.headers)
print("Response Content : \n",r.text)