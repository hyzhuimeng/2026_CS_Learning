class book:
    all_books=[]
    def __init__(self,name,money):
        self.name=name
        self.money=money
        book.all_books.append({"name":self.name,"money":self.money})
    def print_info(self):
        print(f"书名：{self.name}，价格：{self.money}")
        print(book.all_books)
bo=book("i","87")
bo.print_info()