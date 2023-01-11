import datetime

class Order_Model:

    def __init__(self, id: int, date:datetime, client_id:int, book_id:int, status: int):
        self.id = id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status

