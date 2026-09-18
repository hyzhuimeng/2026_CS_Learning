import requests
import logging
class DataFetcher():
    def __init__(self):
        pass
    def fetch_user_data(self,user_id):
        url=f"https://jsonplaceholder.typicode.com/users/{user_id}"
        try:
            response=requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"请求异常，状态码:{response.status_code}")
                return None
        except:
            logging.error("出错了")
            return None
data=DataFetcher()
print(data.fetch_user_data(999))
            


