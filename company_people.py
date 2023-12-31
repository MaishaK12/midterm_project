# Once you have written the classes, write a program that creates an object of the
# ProductionWorker class and prompts the user to enter data for each of the object's data attributes. 
# Store the data in the object, then use its accessor methods to retrieve it and display it on the screen.

from ProductionWorker import ProductionWorker

# Prompt user for ProductionWorker's information
name = input("Enter worker's name: ")
number = input("Enter worker's number: ")
shift = int(input("Enter worker's shift (Press 1 for day, and 2 for night): "))
pay_rate = float(input("Enter worker's hourly pay rate: "))

# ProductionWorker object with user's input
worker = ProductionWorker(name, number, shift, pay_rate)

# Displays worker's information
print("Name:", worker.get_name())
print("Number:", worker.get_number())
print("Shift:", worker.get_shift())
print("Pay rate: $", worker.get_pay_rate(), "per hour")
