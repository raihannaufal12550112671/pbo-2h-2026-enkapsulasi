from datetime import datetime

class Book:
    def __init__(self, idx, title, author):
        self.__id = idx
        self.__title = title
        self.__author = author
        self.last_updated = datetime.now()
        
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def set_title(self, new_title):
        self.__title = new_title
        self.last_updated = datetime.now()

    def get_author(self):
        return self.__author

    def set_author(self, new_author):
        self.__author = new_author
        self.last_updated = datetime.now()
