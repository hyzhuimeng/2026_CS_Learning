import logging
import requests

url="https://jsonplaceholder.typicode.com/todos/14374172"
logging.basicConfig(
    filename="logging.log",
    encoding='UTF-8',
    level=logging.INFO
)
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.info("程序正常启动")
        print(data)
    else:
        logging.warning(f"响应码非200，code={response.status_code}")
except requests.exceptions.RequestException:
    logging.error("网络请求失败，请检查 URL")