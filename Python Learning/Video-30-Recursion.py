# def facto(a):
#     if a==1 or a==0:
#         return 1
#     return a*facto(a-1)
#
# print(facto(4))

def fibo(a):
    if a==0:
        return 0
    elif a==1:
        return 1

    return fibo(a-1)+fibo(a-2)

n=int(input("Enter the n term to be found: "))
for i in range(n):
    print(fibo(i))
