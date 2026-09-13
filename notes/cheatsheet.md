"".join()通过引号中的内容拼接字符串，括号内为需要拼接的内容
with open("data.json","w",encoding="utf-8")as f:
        json.dump(b_dict,f,ensure_ascii=False,indent=4)