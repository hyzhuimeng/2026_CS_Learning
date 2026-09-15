import json
import logging
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def save_to_json(self):
        a={"name":self.name,"score":self.score}
        with open("student_info.json","w",encoding="utf-8") as f:
            json.dump(a,f,ensure_ascii=False)
    def load_from_json(self):
        try:
            with open("student_ino.json","r",encoding="utf-8") as f:
                students =json.load(f)
        except:
            logging.error("文件名不存在")
            print("未找到该学生档案")
stu=Student("张三","95")
stu.save_to_json()
stu.load_from_json()
        