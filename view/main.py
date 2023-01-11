from controller.book_control import Book_Control
from controller.client_control import Client_Control
from controller.librarian_control import librarian_Control
from controller.order_control import Order_controler
import datetime

book = Book_Control()
order = Order_controler()
print("Welcome! Join as a client or a Librarian?")
print('''
if you are a client Enter "1"
if you are a Librarian Enter "2"
''')


client = Client_Control()

def get_client_inputs():
    fullname = input("Enter your fullname: ")
    age = input("Enter your age:")
    id_no = input("Enter your id number: ")
    phonenumber = input("Enter your phone number: ")


    client.register_new_client(fullname= fullname, age= age, id_no= id_no, phonenumber= phonenumber)

librarian = librarian_Control()

def get_librarian_inputs():
    fullname = input("Enter your fullname: ")
    age = input("Enter your age:")
    id_no = input("Enter your id number: ")
    emplyment_type = input("Enter your emplyment_type, 1 = 'full'/ '2' = part: ")


    librarian.register_new_librarian(fullname = fullname, age = age, id_no = id_no,emplyment_type = emplyment_type)


user_input = input("Enter Just number '1' or '2': ")
if user_input is '1':
    get_client_inputs()
    print("                                 ")
    print("Choose any book you want:-")




    book.add_new_book(title = "The idiot brain",description= "medical book",auther="Dean Burnet",status="Available")
    book.add_new_book("Nacked Economics", "Economie", "Charles Wheelan", "UnAvailable")
    book.add_new_book("The rule of law", "law book", "Tom Bingham", "UnAvailable")
    book.add_new_book("The Guns of August", "First World War", "Barbra W.Tuchman", "Available")


    for i in range(len(book.book_list)):
        print("///////////////////")
        print("book", book.book_list[i].id)
        print("Title is: ", book.book_list[i].title)
        print("Description is: ", book.book_list[i].description)
        print("Auther is: ", book.book_list[i].auther)
        print("Status is: ", book.book_list[i].status)
    print("                                    ")
    book_num = int(input("Enter the available book number: "))
    chosen_book = book.book_list[0]
    for num in range(len(book.book_list)):
        if book_num == book.book_list[num].id:
            chosen_book = book.book_list[num]

    if chosen_book.status == "Available":
        order.add_new_order(datetime.datetime.now(), client.id_count, chosen_book.id, 1)

    else:
        print("This book '", chosen_book.title, "' is not available")

    print(order.order_list[0].date)
    print(order.order_list[0].book_id)
    print(order.order_list[0].client_id)
    print(order.order_list[0].status)


elif user_input is '2':
    get_librarian_inputs()
    print('''
    please choose what you want:-
    1- get client number.
    2- search for an order.
    3- view all books.
    4- view borrowing order.
    ''')
    number = int(input("add a number: "))
    if number == 1:
        print("client number is: ", client.get_client_count())
    elif number == 2:
        order_Search = int(input("add order id:"))
        for i in range(len(order.order_list)):
            if i == order_Search:
                print("date is ", order.order_list[i].date)
                print("client id is ",order.order_list[i].clint_id)
                print("book id is ",order.order_list[i].book_id)
                print("status number is ",order.order_list[i].status)

    elif number == 3:
        book.add_new_book(title="The idiot brain", description="medical book", auther="Dean Burnet", status="Available")
        book.add_new_book("Nacked Economics", "Economie", "Charles Wheelan", "UnAvailable")
        book.add_new_book("The rule of law", "law book", "Tom Bingham", "UnAvailable")
        book.add_new_book("The Guns of August", "First World War", "Barbra W.Tuchman", "Available")

        for i in range(len(book.book_list)):
            print("///////////////////")
            print("book", book.book_list[i].id)
            print("Title is: ", book.book_list[i].title)
            print("Description is: ", book.book_list[i].description)
            print("Auther is: ", book.book_list[i].auther)
            print("Status is: ", book.book_list[i].status)
    elif number == 4:
        for i in range(len(order.order_list)):
                print("order", order.order_list[i].id)
                print("date is ", order.order_list[i].date)
                print("client id is ", order.order_list[i].clint_id)
                print("book id is ", order.order_list[i].book_id)
                print("status number is ", order.order_list[i].status)
