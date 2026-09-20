import json
class jsonData:
    def load_data(self,data):
        try:
            with open("git.json","w",encoding="utf-8") as f:
                json.dump(data,f,ensure_ascii=False,indent=4)
                print("文件保存成功")
        except Exception as e:
            print("不好意思，出错了")