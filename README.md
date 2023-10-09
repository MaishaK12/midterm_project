# midterm_project

1) (File Name: triangle.py)
Design a class named Triangle that extends the GeometricShape class (See the sample codes for this class). The Triangle class contains:
  • Three float data fields named side1, side2, and side3 denote the triangle's three sides.
  • A constructor creates a triangle with the specified side1, side2, and side3 with default values 3.0, 4.0, and 5.0, respectively.
  • The accessor methods for all three data fields.
  • The mutator methods for all three data fields.
  • A method named get_perimeter() that returns the perimeter of this triangle.
    o Perimeter: 𝑝 = 𝑠𝑖𝑑𝑒1 + 𝑠𝑖𝑑𝑒2 + 𝑠𝑖𝑑𝑒3
  • A method named get_area() returns the area of this triangle.
    o Area: 𝑎 = √(𝑝2) (𝑝2 − 𝑠𝑖𝑑𝑒1) (𝑝2 − 𝑠𝑖𝑑𝑒2) (𝑝2 − 𝑠𝑖𝑑𝑒3)
  • A method named __str__() that returns a string description for the triangle.
    o For example, if we have a triangle with the following sides (3.0, 4.0,5.0), the __str__() method must return: Triangle: side1 = 3.0, side2 = 4.0, and side3 = 5.0

Within the same file, write a test program that prompts the user to enter the triangle's three sides, a colour, and 1 or 0 to indicate whether the triangle is filled or not, respectively. 
The program should create a Triangle object with these sides and set the colour and filled properties using the input. 
The program should display the triangle's area, perimeter, colour, and True or False to indicate whether the triangle is filled or not.

2) (File Name: company_people.py)
Write an Employee class that keeps data attributes for the following pieces of information:
  • Employee name
  • Employee number

Next, write a class named ProductionWorker that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes for the following information:
  • Shift number (an integer, such as 1, 2, or 3)
  • Hourly pay rate

The workday is divided into two shifts: day and night. 
The shift attribute will hold an integer value representing the shift that the employee works. 
The day shift is shift 1 and the night shift is shift 2. Write the appropriate accessor and mutator methods for each class.

Once you have written the classes, write a program that creates an object of the ProductionWorker class and prompts the user to enter data for each of the object's data attributes. 
Store the data in the object, then use its accessor methods to retrieve it and display it on the screen.

In a particular factory, a shift supervisor is a salaried employee who supervises a shift. 
In addition to a salary, the shift supervisor earns a yearly bonus when their shift meets production goals. 
Write a ShiftSupervisor class that is a subclass of the Employee class. 
The ShiftSupervisor class should keep a data attribute for the annual salary and a data attribute for the yearly production bonus that a shift supervisor hasearned. 
Within the same file, demonstrate the class by writing a program that uses a ShiftSupervisor object.
Write a class named Person with data attributes for a person's name, address, and telephone number. 

Next, write a class called Customer that is a subclass of the Person class. 
The Customer class should have a data attribute for a customer number and a Boolean data attribute indicating whether the Customer wishes to be on a mailing list. 
Finally, within the same file, demonstrate an instance of the Customer
class in a simple program.

3) (File Name: atm_machine.py)
Use the Account class created in Lab 05 to simulate an ATM machine.
Create ten accounts in a list with the ids 0, 1, ..., 9, and an initial balance of $100.
The system prompts the user to enter an id. If the id is entered incorrectly, ask the user to enter the correct id.
Once an id is accepted, the main menu is displayed, as shown in the sample run.
You can enter a choice of 1 for viewing the current balance, 2 for withdrawing money, 3 for depositing money, and 4 for exiting the main menu.
Once you exit, the system will prompt for an id again. So, once the system starts, it won't stop.
