from model.order_model import Order_Model
import datetime

class Order_controler:
    id_count = 1

    def __init__(self):
        self.order_list = []

    def add_new_order(self, date: datetime, client_id: int, book_id: int, status: int):
        new_order = Order_Model(self.id_count, date, client_id, book_id, status)

        self.order_list.append(new_order)
        self.id_count+=1
