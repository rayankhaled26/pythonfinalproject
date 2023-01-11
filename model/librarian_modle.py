from model.personal_information import Personal_information


class Librarian_model(Personal_information):
    def __init__(self, id: int, fullname: str, age: int, id_no: int, emplyment_type: int):
       super(Librarian_model, self).__init__(id, fullname, age, id_no)
       self.__emplyment_type = emplyment_type

