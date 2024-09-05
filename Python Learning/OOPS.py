# class info:
#     name="Saswat"
#     age=20
#     happy="yes"
#
# rick=info()
# rick.name="rick"
# print(rick.name)

#method

# class info:
#     name="Saswat"
#     age=20
#     happy="yes"
#     def infor(self):
#         print(f"I am {info.name}, I am {info.age}.Am I happy? {info.happy}")
#
# rick=info()
# rick.name="rick"
# rick.age=19
# rick.happy="yes"
# print(rick.name)
# rick.infor()

class info:
    name="Saswat"
    age=20
    happy="yes"
    def infor(self):
        print(f"I am {self.name}, I am {self.age}.Am I happy? {self.happy}")

rick=info()
rick.name="rick"
rick.age=19
rick.happy="yes"
print(rick.name)
rick.infor()


