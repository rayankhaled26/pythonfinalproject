class Book_model:
    def __init__(self, id: int, title: str, description: str, auther:str, status: str):
        self.id = id
        self.title = title
        self.description = description
        self.auther = auther
        self.status = status


    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_auther(self):
        return self.auther

    def get_status(self):
        return self.status