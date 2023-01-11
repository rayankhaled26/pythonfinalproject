class Personal_information:
    def __init__(self, id: int, fullname: str, age: int, id_no: int):
        self.__id = id
        self.__fullname = fullname
        self.__age = age
        self.__id_no = id_no

    def set_id (self, id):
        self.__id = id

    def get_id(self):
        return self.__id


    def set_fullname(self, fullname):
        self.__fullname = fullname

    def get_fullname(self):
        return self.__fullname


    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


    def set_id_no(self, id_no):
        self.__id_no = id_no

    def get_id_no(self):
        return self.__id_no