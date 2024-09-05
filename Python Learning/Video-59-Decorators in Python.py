# def greet(fx):
#     def mfx():
#        print("hey! Welcome back!")
#        fx()
#        print("bye! Lets meet again!")
#     return mfx

# @greet
# def hello():
#     print("Hello World!")

#or

# greet(hello)

# hello()

#for add(function with arguments)
#so if there are any arguments then

def greet(fx):
    def mfx(*args,**kwargs):
       print("hey! Welcome back!")
       fx(*args,**kwargs)
       print("bye! Lets meet again!")
    return mfx
#*args takes every argument as a tuple and **kwargs is to take arguments in the form of a dictionary, key value pair
# @greet
def add(x,y):
    print(f"The sum of {x} and {y} is: {x+y}")

# add(2,4)

#or

greet(add)(1,2)