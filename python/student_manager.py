import json
import logging
class StudentManager:
    def __init__(self):
        self.students=[]
    def add_student(self,name,score):
        student_dict={"name":name,"score":score}
        self.students.append(student_dict)
    def save_to_file(self):
        try:
            with open("data_student.json","w",encoding="utf-8")as f:
                json.dump(self.students,f,ensure_ascii=False,indent=4)
        except FileNotFoundError:
            print("对不起，好像出问题了")
    def load_from_file(self):
        try:
            with open("data_student,json","r",encoding="utf-8")as f:
                self.students=json.load(f)
        except FileNotFoundError:
            logging.warning("本地暂无数据，初始化为空")
stu=StudentManager()
stu.add_student("李华",88)
stu.add_student("张三",99)
stu.save_to_file()
