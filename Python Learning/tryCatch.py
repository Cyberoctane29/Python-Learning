# a = input("Enter the number whose multiplication table is to be printed: ")
# print(f"The multiplication table of {a}:")
# try:
#     for i in range(10):
#         print(f"{int(a)} x {i + 1} = {a * (i + 1)}")
# except Exception as e:
#     print(e)
#
# print("Some lines of code.")
# print("End of program!")

#or

# a = input("Enter the number whose multiplication table is to be printed: ")
# print(f"The multiplication table of {a}:")
# try:
#     for i in range(10):
#         print(f"{int(a)} x {i + 1} = {a * (i + 1)}")
# except:
#     print("Wrong input format!")
#
# print("Some lines of code.")
# print("End of program!")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
#
# except IndexError:
#     print("Index Error")

#finally

# def func1():
#     try:
#         l=[1,2,3,4]
#         i=input("Enter the index: ")
#         print(l[i])
#         return 1
#     except:
#         print("Error ocurred!")
#         return 0;
#     finally:
#         print("I am always executed.")
#
# x=func1()
# print(x)

#why finally is required cant we just write it

def func1():
    try:
        l=[1,2,3,4]
        i=input("Enter the index: ")
        print(l[i])
        return 1
    except:
        print("Error ocurred!")
        return 0

    print("I am always executed.")

x=func1()
print(x)

#notice how without the finally the     print("I am always executed.") is not executed

#even if function returns from try or except even then finally works so even if function returns
