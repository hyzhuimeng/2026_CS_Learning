import requests
class head:
    def get_data(self):
        url="https://httpbin.org/get"
        params={"search":"python","page":1}
        headers={"User-Agent":"My-Python-App/1.0"}
        response=requests.get(url,params=params,headers=headers)
        data=response.json()
        print("信息获取成功")
        return data