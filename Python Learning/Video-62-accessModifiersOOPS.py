# class Employee:
#     def __init__(self):
#         self.name="Harry!"
#
# a=Employee()
# print(a.name)
#it could be accessed as its public
#now in python there is no strict private but we can still do it by puttin two underscored in front of the variable

# class Employee:
#     def __init__(self):
#         self.__name="Harry!"
#
# a=Employee()
# print(a.name)

#so it gave an error
#indirect acessing - name mangling
#in this the private attributes name is changed in a way
# print(a._Employee__name)

#also
# print(a.__dir__())

#protected

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())

# # class Employee:
# #     def __init__(self):
# #         self.__name="Harry!"
# # a=Employee()
# # print(a.__dir__())
#
# the above is for private
#
# class Student:
#     def __init__(self):
#         self._name = "Harry"
#
# obj = Student()
# print(dir(obj))
#
# this is protected
#
# I saw that there is a difference in dir line
# also
# in private:
# #indirect acessing - name mangling
# #in this the private attributes name is changed in a way
# # print(a._Employee__name)
#
# but in protected nothing like this is required
# print(obj._name)
# in protected
# ChatGPT
# You've touched on some important concepts related to encapsulation and access control in Python: public, protected, and private attributes.
#
# Public, Protected, and Private Attributes in Python
# Public Attributes:
#
# Can be accessed from anywhere.
# No special syntax needed.
# Example:
# python
# Copy code
# class PublicExample:
#     def __init__(self):
#         self.name = "Harry"
#
# obj = PublicExample()
# print(obj.name)  # Direct access
# Protected Attributes:
#
# Indicated by a single underscore (_).
# Suggests that the attribute is intended for internal use and should not be accessed directly from outside the class, but this is only a convention and not enforced by Python.
# Example:
# python
# Copy code
# class ProtectedExample:
#     def __init__(self):
#         self._name = "Harry"
#
# obj = ProtectedExample()
# print(obj._name)  # Direct access (not recommended, but allowed)
# Private Attributes:
#
# Indicated by double underscores (__).
# Triggers name mangling, where the attribute name is modified internally to include the class name. This makes it harder (but not impossible) to access the attribute directly from outside the class.
# Example:
# python
# Copy code
# class PrivateExample:
#     def __init__(self):
#         self.__name = "Harry"
#
# obj = PrivateExample()
# # print(obj.__name)  # This would raise an AttributeError
# print(obj._PrivateExample__name)  # Name mangling allows indirect access
# Differences in dir() Output
# When using dir() to inspect an object, the output will include all attributes and methods associated with the object. The way protected and private attributes appear in the dir() output differs due to name mangling.
#
# Protected Attributes: Appears with a single underscore and the attribute name.
# Private Attributes: Appears with the class name prefixed to the attribute name.
# Example Code
# Here's a comprehensive example to illustrate the differences:
#
# python
# Copy code
# class Employee:
#     def __init__(self):
#         self.__name = "Harry"  # Private attribute
#
# class Student:
#     def __init__(self):
#         self._name = "Harry"  # Protected attribute
#
# # Creating instances
# a = Employee()
# b = Student()
#
# # Using dir() to inspect attributes
# print(dir(a))
# print(dir(b))
#
# # Accessing attributes
# # Private attribute (name mangling)
# print(a._Employee__name)  # Works due to name mangling
# # print(a.__name)  # Raises AttributeError
#
# # Protected attribute (convention)
# print(b._name)  # Works but not recommended
# # Key Points
# Private Attribute Access: Private attributes are accessed using name mangling (_ClassName__attributeName), which is a mechanism to prevent direct access but still allows it if necessary.
# Protected Attribute Access: Protected attributes follow a convention indicating that they should not be accessed directly, but they are still accessible without any special syntax.
# Encapsulation: Both mechanisms are meant to enforce encapsulation and prevent unintended use or modification of class internals, but private attributes offer stronger (though not absolute) protection.
# In summary, while Python does not enforce strict access control, these conventions help in writing cleaner and more maintainable code by indicating the intended level of access for class attributes.
#
# print(dir(a))
#
# if the above is possible then what is this
#
# print(dir(a))
#
# ChatGPT
# Using dir() on an instance of a class, such as a in your example, returns a list of the attributes and methods available for that instance. This includes:
#
# Attributes defined in the instance's class.
# Attributes inherited from base classes.
# Methods defined in the class and its base classes.
# Internally generated attributes like those created by name mangling for private attributes.
# Example
# Let's revisit the Employee and Student classes and use dir() on their instances:
#
# python
# Copy code
# class Employee:
#     def __init__(self):
#         self.__name = "Harry"  # Private attribute
#
# class Student:
#     def __init__(self):
#         self._name = "Harry"  # Protected attribute
#
# # Creating instances
# a = Employee()
# b = Student()
#
# # Using dir() to inspect attributes and methods
# print(dir(a))
# print(dir(b))
# Output Explanation
# Private Attribute (__name):
#
# In the Employee class, self.__name is a private attribute.
# dir(a) will include _Employee__name due to name mangling.
# Protected Attribute (_name):
#
# In the Student class, self._name is a protected attribute.
# dir(b) will include _name directly.
# Expected Output
# python
# Copy code
# print(dir(a))
# # Output: ['_Employee__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
#
# print(dir(b))
# # Output: ['_name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
# Breakdown of dir() Output
# Common Attributes: Both outputs include common attributes and methods such as __class__, __dict__, __init__, and others that are part of all Python objects.
#
# Private Attribute (__name):
#
# Appears as _Employee__name in the dir(a) output due to name mangling.
# Protected Attribute (_name):
#
# Appears as _name directly in the dir(b) output.
# Accessing Attributes
# Using dir() helps you discover the attributes and methods available for an object, including those that are intended to be private or protected:
#
# Private Attribute Access:
#
# python
# Copy code
# print(a._Employee__name)  # Correct way to access private attribute due to name mangling
# Protected Attribute Access:
#
# python
# Copy code
# print(b._name)  # Direct access to protected attribute (not recommended but allowed)
# Conclusion
# The dir() function is a useful introspection tool that lists all the attributes and methods available for an object. This includes private attributes (with name mangling) and protected attributes. It provides a way to explore the structure and capabilities of objects, especially for debugging and understanding the internal workings of a class.