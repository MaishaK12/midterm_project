# The ShiftSupervisor class should keep a data attribute for the annual
# salary and a data attribute for the yearly production bonus that a shift supervisor has earned. 
# Within the same file, demonstrate the class by writing a program that uses a ShiftSupervisor object.

from Employee import Employee


# ShiftSupervisor extends superclass Employee; includes annual salary and yearly production bonus
class ShiftSupervisor(Employee):
    # Constructor
    def __init__(self, name, number, annual_salary, production_bonus):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__production_bonus = production_bonus

    # Accessor and Mutator for annual salary and production bonus
    def get_annual_salary(self):
        return self.__annual_salary

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def get_production_bonus(self):
        return self.__production_bonus

    def set_production_bonus(self, production_bonus):
        self.__production_bonus = production_bonus


# Create Supervisor object
supervisor = ShiftSupervisor("Lucy Mason", "1234", 50000.0, 1000.0)
# Displays Supervisor’s information
print("Name:", supervisor.get_name())
print("Employee Number:", supervisor.get_number())
print("Annual Salary:", supervisor.get_annual_salary())
print("Production Bonus:", supervisor.get_production_bonus())
