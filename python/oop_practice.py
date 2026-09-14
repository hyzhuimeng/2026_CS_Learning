import json
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def save_to_json(self):
        a={"name":self.name,"score":self.score}
        with open("student_info.json","w",encoding="utf-8") as f:
            json.dump(a,f,ensure_ascii=False)
stu=Student("张三","95")
stu.save_to_json()
        