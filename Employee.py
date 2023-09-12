# Write an Employee class that keeps data attributes for the following pieces of information:
#     Employee name
#     Employee number

# Class Employee holds employee name, and number
class Employee:
    # Constructor
    def __init__(self, name, number):
        self.name = name
        self.number = number

    # Accessor for name, and number
    def get_name(self):
        return self.name

    def get_number(self):
        return self.number
