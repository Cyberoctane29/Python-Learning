#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# # Creating an instance of Employee directly
# e1 = Employee("Harry", 12000)
# print(e1.name)
# print(e1.salary)
#
# # Creating an instance of Employee from a string
# string1 = "Harry-12000"
# e2 = Employee(string1.split("-")[0], string1.split("-")[1])
# print(e2.name)
# print(e2.salary)

#ok here we can do this for e2 but doing the parsing everytime would be a lot of work also if we change     def __init__(self, name, salary):
 #to accept only parsed string via string1.split("-")[0] and string1.split("-")[1] for input string1 = "Harry-12000" in the constructor
 #    def __init__(self, name, salary) then it will not accept when rather than the input being in this format Harry-12000 is in direct format of
#e1 = Employee("Harry", 12000) hence we need a constructor which will accept the input in any format so we use alternative constructors

#we can make it a class method

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
        def fromStr(cls,string):
        return cls(string1.split("-")[0], int(string1.split("-")[1]))

#we ask it to return this class's instance with these parameters

# Creating an instance of Employee directly
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

# Creating an instance of Employee from a string
string1 = "Harry-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

#when we run it an instance is made with those paramters string1.split("-")[0], string1.split("-")[1]

#chatgpt:
#
# Memory updated
# Yes, the fromStr class method acts as an alternative constructor. It provides a different way to create an instance of the Employee class using a string formatted with a name and salary separated by a hyphen.
#
# Here's your corrected code with proper indentation and variable names:
#
# python
# Copy code
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     @classmethod
#     def fromStr(cls, string):
#         name, salary = string.split("-")
#         return cls(name, int(salary))
#
# # Creating an instance of Employee directly
# e1 = Employee("Harry", 12000)
# print(e1.name)   # Output: Harry
# print(e1.salary) # Output: 12000
#
# # Creating an instance of Employee from a string
# string1 = "Rohan-15000"
# e2 = Employee.fromStr(string1)
# print(e2.name)   # Output: Rohan
# print(e2.salary) # Output: 15000
# Explanation:
# Class Definition and Initializer:
#
# The Employee class has an __init__ method to initialize the name and salary attributes.
# Class Method fromStr:
#
# Decorated with @classmethod, it takes the class (cls) and a string as arguments.
# It splits the string into name and salary, converts salary to an integer, and returns a new instance of Employee.
# Creating Instances:
#
# e1 is created directly using the Employee constructor.
# e2 is created using the fromStr class method, which serves as an alternative constructor.
# Printing Attributes:
#
# The name and salary attributes of both instances are printed to demonstrate that they have been set correctly.
# Using class methods as alternative constructors is a common pattern in Python to provide additional ways to create instances of a class.
