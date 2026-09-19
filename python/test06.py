import requests
url="https://httpbin.org/get"
params={"search":"python","page":1}
headers={"User-Agent":"My-Python-App/1.0"}
response=requests.get(url,params=params,headers=headers)
print(response.json())