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
