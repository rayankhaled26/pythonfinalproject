from model.personal_information import Personal_information


class Client_model(Personal_information):
    def __init__(self, id: int, fullname: str, age: int, id_no: int, phonenumber: int):
     super(Client_model, self).__init__(id, fullname, age, id_no)
     self.__phonenumber = phonenumber


