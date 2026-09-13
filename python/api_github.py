import requests
import logging
url="https://api.github.com/users/torvalds"
logging.basicConfig(
    filename="log.log",
    encoding='UTF-8',
    level=logging.INFO
)
try: 
    response = requests.get(url)
    if response.status_code == 200:
        a_dict=response.json()
        b_dict={
            "姓名":a_dict["name"],
            "任职公司":a_dict["company"],
            "公开仓库数量":a_dict["public_repos"]
        }
        logging.info(f"获取用户信息:{b_dict}")
except requests.exceptions.RequestException:
    logging.error("网络请求失败，请检查 URL")