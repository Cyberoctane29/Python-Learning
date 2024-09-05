#default constructor
# class person:
#     def __init__(self):
#         print("Hey this is person!")
#
#     def intro(self):
#         print(f"I am {self.name} and I am {self.age}")

# ob1=person(

class person:
    def __init__(self,name,o):
        print("Hey this is person!")
        self.name=name
        self.age=o

    def intro(self):
        print(f"I am {self.name} and I am {self.age}")


a=person("Saswat",19)
b=person("Ricky",19)
a.intro()
b.intro()

