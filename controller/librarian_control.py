from model.librarian_modle import Librarian_model


class librarian_Control:

    def __init__(self):
        self.librarian_list = []

    id_count = 0

    def register_new_librarian(self, fullname: str, age: str, id_no: str, emplyment_type: str):
        new_client = Librarian_model(self.id_count, fullname, int(age), int(id_no), int(emplyment_type))

        self.librarian_list.append(new_client)
        self.id_count += 1


        if fullname.isspace():
            return "invalid fullname"
        elif age.isspace() or not age.isdigit():
            return "invalid age"
        elif id_no.isspace()or not id_no.isdigit():
            return "invalid id_no"
        elif emplyment_type.isspace()or not emplyment_type.isdigit():
            return "invalid emplyment_type"



    def get_librarian_count(self):
        return len(self.librarian_list)
