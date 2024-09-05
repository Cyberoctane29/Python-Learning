class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

#in the above the tesla will be only set for e1 as rn the changeCompany is an instance method hence as we write e1.changeCompany("Tesla") it basically
#takes e1 and puts it in cls's place and Tesla in place of newCompany.

class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

#  @classmethod with this it gets the first argument cls to the class not the instance unlike in the previous one