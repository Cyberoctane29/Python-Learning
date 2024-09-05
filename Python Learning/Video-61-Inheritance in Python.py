class Employee:
    def __init__(self,name,id):
        self.name=name;
        self.id=id;

    def showDetails(self):
        print(f"The name of the employee with id {self.id} is {self.name}.");

#inheritance
#what if we wanted to change the name of the class from Employee to programmer, in this case the places where employee would be used would given
#an error

class programmer(Employee):
    def showLang(self):
        print("The default language is Python!")

# e=Employee("Brad",24)
# e.showDetails()

e1=programmer("Bradlin",25)
e1.showLang()
e1.showDetails()