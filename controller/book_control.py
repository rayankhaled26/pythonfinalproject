from model.book_model import Book_model

class Book_Control:

    id_count = 1
    def __init__(self):
        self.book_list = []


    def add_new_book(self, title: str, description: str, auther:str, status:str):
        new_book = Book_model(self.id_count, title, description, auther, status)

        self.book_list.append(new_book)
        self.id_count+=1



    def get_book_count(self):
        return len(self.book_list)





