from model.client_model import Client_model

class Client_Control:

    def __init__(self):
        self.client_list = []
    id_count = 0
    def register_new_client(self,fullname: str, age: str, id_no: str, phonenumber: str):
        new_client = Client_model(self.id_count, fullname, int(age), int(id_no), int(phonenumber))

        self.client_list.append(new_client)
        self.id_count+=1

        if fullname.isspace():
            return "invalid fullname"
        elif age.isspace() or not age.isdigit():
            return "invalid age"
        elif id_no.isspace()or not id_no.isdigit():
            return "invalid id_no"
        elif phonenumber.isspace()or not phonenumber.isdigit():
            return "invalid phonenumber"



    def get_client_count(self):
        return len(self.client_list)
