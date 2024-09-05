# class Employee:
#     def __init__(self,name):
#         self.name=name
#
#     def showDetails():
#         print(f"The name of the Employee is: {self.name}")
#
# emp1=Employee("Harry")
# emp1.showDetails()
same as
Employee.showDetails(emp1)

#the thing is when we write emp1.showDetails() it converts to Employee.showDetails(emp1

#thats why if we did this
def showDetails():
    print(f"The name of the Employee is: {self.name}")

#in class and then called
emp1.showDetails()

#then it shows this error as internally emp1.showDetails() was converted to this Employee.showDetails(emp1) and it has an argument, the same
#argument TypeError: Employee.showDetails() takes 0 positional arguments but 1 was given this line is implying

# Traceback (most recent call last):
#   File "C:\Users\saswa\PycharmProjects\pythonProject\Video-66-Instance variables vs class variables.py", line 9, in <module>
#     emp1.showDetails()
# TypeError: Employee.showDetails() takes 0 positional arguments but 1 was given

#instance variable

class Employee:
    def __init__(self, name):
        self.name = name #instance variable
        self.raise_amount = 0.02 #instance variable

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount}")

# Creating instances of Employee
empl = Employee("Harry")
empl.raise_amount = 0.3
empl.showDetails()

emp2 = Employee("Rohan")
emp2.showDetails()

# here raise amount for both Harry and Rohan was set to 0.02 as a default but as it was individually assigned to them hence it can be changed
# for each employee

# Yes, that's correct. In the Employee class, the raise_amount attribute is initialized to a default value of 0.02 for each instance of the class. However, since raise_amount is an instance attribute, it can be individually assigned and changed for each employee.
#
# Here's a detailed explanation:
#
# Explanation
# Default Value:
#
# When a new Employee object is created, the raise_amount is set to 0.02 by default.
# This default value is specified in the __init__ method of the class.
# Changing the Value:
#
# After an Employee object is created, you can change the raise_amount for that particular instance without affecting other instances.
# Each instance of the Employee class maintains its own copy of the raise_amount attribute.

# Summary
# Each instance of the Employee class has its own raise_amount attribute.
# The default value of raise_amount is set to 0.02 for each instance upon creation.
# The raise_amount can be individually modified for each instance after creation, and these changes do not affect other instances.

# Yes, self.name = name is an instance variable as well. In Python, instance variables are variables that are specific to each instance of a class. They are defined within methods (usually within the __init__ method) and are prefixed with self to indicate that they belong to the instance.
#
# Instance Variables
# Instance variables are used to store data that is unique to each instance.
# They are defined by prefixing the variable name with self within a method of the class.

#class variable

class Employee:
    companyName = "Apple"  # Class variable

    def __init__(self, name):
        self.name = name           # Instance variable
        self.raise_amount = 0.02   # Instance variable

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

# Creating instances of Employee
empl = Employee("Harry")
empl.raise_amount = 0.3
empl.showDetails()

emp2 = Employee("Rohan")
emp2.showDetails()

# Class Variables vs Instance Variables
# Class Variable (companyName):
#
# Defined at the class level and shared among all instances of the class.
# It can be accessed using the class name (Employee.companyName) or through an instance (self.companyName).
# Instance Variables (name, raise_amount):
#
# Defined within the __init__ method and are unique to each instance of the class.
# They are accessed using self.

#more info

# Creating instances of Employee
# empl = Employee("Harry")
# emp2 = Employee("Rohan")
#
# # Changing the company name for empl instance only
# empl.companyName = "Google"
# empl.raise_amount = 0.3
# empl.showDetails()
#
# # emp2 will still refer to the class variable
# emp2.showDetails()
#
# # Changing the class variable for all instances
# Employee.companyName = "Microsoft"
# emp2.showDetails()
# empl.showDetails()
#
# # Showing that the instance attribute hides the class variable for empl
# print(empl.companyName)  # Output: Google
# print(emp2.companyName)  # Output: Microsoft
#
# empl.companyName = "Google" creates an instance variable companyName for empl, which hides the class variable for that instance only.
#
# Wait what?
# ChatGPT
# Yes, that('s correct. When you assign a value to empl.companyName, you are creating an instance variable with the same name as the class variable
# 'companyName''. This instance variable will shadow (or hide) the class variable for that particular instance.)

#class variable
class Employee:
    companyName = "Apple"  # Class variable

    def __init__(self, name):
        self.name = name           # Instance variable
        self.raise_amount = 0.02   # Instance variable

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

# Creating instances of Employee
empl = Employee("Harry")
empl.raise_amount = 0.3
empl.companyName=Apple india
empl.showDetails()

emp2 = Employee("Rohan")
emp2.showDetails()

#now we see that empl and emp2 have two different companyName, the thing which happens if instance variable is there for an instance then
#that is used, for example here for Harry Instance variable emp1.companyName exists already hence its used.
#As its checked in the instance first that if the instance variable is available

#Also Employee.companyName=Google can even change the class variable

# When modified through an instance, a new instance variable is created, hiding the class variable for that instance only.
# in class variable
# but in instance variable a new one isnt created right?
#
# answer in brief
#
# 2/2
#
# ChatGPT
# Correct!
#
# Class Variable: When you modify it through an instance, a new instance variable is created that hides the class variable for that specific instance.
# Instance Variable: When you modify it, you're simply changing the existing instance variable for that specific instance; no new variable is created.
# So, instance variables are always unique to each instance, while class variables can be shared or hidden when an instance variable is created.

#also

class Employee:
    companyName = "Apple"  # Class variable for company name
    noOfEmployees = 0       # Class variable for counting employees

    def __init__(self, name):
        self.name = name               # Instance variable for employee name
        self.raise_amount = 0.02       # Instance variable for raise amount
        Employee.noOfEmployees += 1    # Incrementing the class variable for employee count

    def showDetails(self):
        print(f"The name of the Employee is {self.name} "
              f"and the raise amount in {Employee.companyName} "
              f"is {self.raise_amount}. Total employees: {Employee.noOfEmployees}")

# Creating an instance of Employee
empl = Employee("Harry")
empl.raise_amount = 0.3           # Changing the instance variable for Harry
empl.companyName = "Apple India"   # This creates an instance variable, not affecting the class variable
empl.showDetails()                  # Showing details of the employee


#example of how no of employees cant be for each employee but it should be more of a class based variable