# #dir
# #list
# x=[1,2,3,]
# print(dir(x))
# print(x.__add__)
#
# #tuple
# y=(1,2,3,)
# print(dir(y))
# print(y.__add__)
# #if add isnt present in it, it would give name error

# #dict
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("John", 30)
print(p.__dict__)

#if we print this then we get the output then whatever we set as attribute for the
#object with 'self.' we will be displayed as a dictionary

#help
# print(help(str))
print(help(Person))