# The ProductionWorker class should keep data attributes for the following information:
#     Shift number (an integer, such as 1, 2, or 3)
#     Hourly pay rate
# The workday is divided into two shifts: day and night. The shift attribute will hold an integer value representing the shift that the employee works. 
# The day shift is shift 1 and the night shift is shift 2. 

from Employee import Employee


# ProductionWorker extends superclass Employee; includes shift number and hourly pay rate
class ProductionWorker(Employee):
    # Constructor
    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        self.shift = shift
        self.pay_rate = pay_rate

    # Accessor and Mutator for shift, and pay rate
    def get_shift(self):
        return self.shift

    def set_shift(self, shift):
        if shift == 1 or shift == 2:
            self.shift = shift

    def get_pay_rate(self):
        return self.pay_rate

    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate
