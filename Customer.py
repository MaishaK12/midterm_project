# Write a class named Person with data attributes for a person's name, address, and telephone number

from Person import Person


# Class Customer extends superclass Person; includes customer number and mailing list
class Customer(Person):
    # Constructor
    def __init__(self, name, address, telephone, cx_number, mailing_list):
        super().__init__(name, address, telephone)
        # cx is short for customer
        self.__cx_number = cx_number
        self.__mailing_list = mailing_list

    # Accessor and Mutator for customer number and mailing list
    def get_customer_number(self):
        return self.__cx_number

    def set_customer_number(self, cx_number):
        self.__cx_number = cx_number

    def get_mailing_list(self):
        return self.__mailing_list

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list


# Create Customer object
customer = Customer("Ivan Reilly", "123 Random St", "555-555-5555", "A12345", True)
# Display Customer’s information
print("Name:", customer.get_name())
print("Address:", customer.get_address())
print("Telephone:", customer.get_telephone())
print("Customer Number:", customer.get_customer_number())
print("Mailing List:", customer.get_mailing_list())
