# def mult(x):
#     return x*2
#
# multi=lambda x:x*2
#
# print(mult(2))
# print(multi(2))

avg=lambda x,y:(x+y)/2
# print(avg(3,4))

#takes 3 arguments and more

#can pass function to function as parameter

def appl(fx,value):
    return 6 + fx(value)
#
# print(appl(multi,2))

# def appl(fx,value,value1):
#     return 6 + fx(value,value1)
#
# print(appl(avg,2,3))

print(appl(lambda x:x*x,3))