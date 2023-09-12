# Class Person holds name, address, and telephone number
class Person:
    # Constructor
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    # Accessor and Mutator for name, address, and telephone
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_telephone(self):
        return self.__telephone

    def set_telephone(self, telephone):
        self.__telephone = telephone
