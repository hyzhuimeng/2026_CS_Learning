import requests
url="https://jsonplaceholder.typicode.com/todos/14374172"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    print(data)
except:
    requests.exceptions.RequestException
    print("网络请求失败，请检查 URL")