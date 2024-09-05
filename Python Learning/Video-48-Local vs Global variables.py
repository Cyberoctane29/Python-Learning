# x=10
#
# def globalVariable():
#     x=5
#     print(x)
#
# print(x)
# globalVariable()

x=10

def globalVariable():
    global x
    x=5
    print(x)

globalVariable()
print(x)
