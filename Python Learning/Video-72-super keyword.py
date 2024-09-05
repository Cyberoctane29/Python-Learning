class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()  # Calls the parent class method

    def child_method(self):
        print("This is the child method.")
        super().parent_method()  # Calls the parent class method

# Creating an instance of ChildClass
child_object = ChildClass()

# Calling methods
child_object.child_method()  # Output: This is the child method. \n This is the parent method.
child_object.parent_method() # Output: Harry \n This is the parent method.

#######################################################################
#and if

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    # def parent_method(self):
    #     print("Harry")
    #     super().parent_method()  # Calls the parent class method

    def child_method(self):
        print("This is the child method.")
        super().parent_method()

#no parent method in child class but if we call
#child_object.parent_method() here it will use the parent_method of the
#parent as it doesnt have its own.

########################################################################
#constructor scenario

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        self.lang = lang
        self.name=name
        self.id=id
#violates DRY principle

# Creating instances
rohan = Employee("Rohan Das", 420)
harry = Programmer("Harry", "2345", "Python")

# Printing the name attribute of rohan
print(rohan.name)

#as the above violates DRY principle hence

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)

#here in the child class's constructor the parent class's constructor
#is called
