# import tensorflow
# import hashlib
# print("Saswat\nis going to achieve everything he dreamt of" )
# #yes it will happen
# print("Saswat",7,"Seth",sep="-",end='009');


# a=input();
# print("His name is:",a);

# for i in range(2):
#   a=input("Enter your name: ")
# print("His name is:",a)

# name="Saswat"
# for i in name:
#     print(i)
#
# print(name[0])

# name1="Saswat Seth"
# print(name1[0:8])

# name="Harry"
# print(name[-4:-2])

# name2='hey!!!! Saswat!!!!8'
# print(len(name2))
# print(name2)
# print(name2.lower())
# print(name2.upper())
# print(name2.rstrip('!'))
# print(name2.rstrip('t!'))
# print(name2.replace("!","~"))
# print(name2.split("Saswat"))
# print(name2.capitalize())

# name2list=name2.split(" ")
# name2list[0]=name2list[0].capitalize();
# result=" ".join(name2list)
# print(result)
#
# print(name2.center(50))
# print(name2.count("8"))

# print(name2.endswith("8"))
# print(name2.endswith("!!!!",2,7))
#
# print(name2.find("Saswat"))
# print(name2.find("Seth"))
#
# print(name2.index("Saswat"))
# print(name2.index("Seth"))

# print(name2.isalnum())
# name3="Ricky29"
# print(name3.isalnum())
# print(name3.isalpha())
#
# print(name3.islower())

# isprintable
# isspace
# istitle
# startswith
# swapcase
# title

# a=int(input("Enter your age: "))
# print(a)
# if(a>=18):
#     print("You may vote.")
# else:
#     print("You cant vote.")

# a=9
# b=8
# def isGreater(a,b):
#     pass

# def average(*number):
#     print(type(number))
#     sum=0
#     for i in number:
#         sum+=i
#     print("Average is: ",float(sum/len(number)))
#
# average(1,2,3,4,5)
#or
# def average(*number):
#     print(type(number))
#     sum=0
#     for i in number:
#         sum+=i
#     return sum/len(number)
#
# c=average(1,2,3,4,5)
# print(c)

#or

# def average(*number):
#     print(type(number))
#     sum=0
#     for i in number:
#         sum+=i
#     return
# c=average(1,2,3,4,5)
# print(c)
# print(type(c))
#
# def name(**name):
#     print(type(name))
#     print("Hello, ",name["fname"], name["mname"], " and", name["sname"])
#
# name(fname="Saswat",mname="Seth", sname="Rick") #key value pairs

# l=[1,2,3,4,5]
# print(l[-2])
# print(l[3])
#
# if 4 in l:
#     print("yes")
# else:
#     print("No")

# for i in range(0,len(l),2):
#   print(l[i])
#
# a=[]
# for i in range(0,len(l),2):
#    a.append(l[i])

# print(a)
# #or

#jump index
# print(l[0:5:2])
#
# print(l[1:3])
#
# print(l[0:5:-2])
#
# print(l[0:])
# print(l[:len(l)])

#list comprehension
# lst=[i for i in range(4)]
# print(lst)
#
# lst1=[i*i for i in range(4)]
# print(lst1)
#
# lst2=[i*i for i in range(10) if i%2==0]
# print(lst2)

# l1=[1,5,3,2,0]
# l1.sort()
# print(l1)

# l2=[1,5,3,2,0]
# l2.sort(reverse=True)
# print(l2)
#
# l2.reverse()
# l2.index(1)
# l2.count(1)

#not recommended
# m=l2
# m[0]=67
# print(l2)
#
# #recommended
# m=l2.copy()
# m[0]=23
# print(l2)
# print(m)
#
# l2.insert(1,889)
# print(l2)
#
# l2.extend(m)
# print(l2)
#
# k=l2+m
# print(k)

# tup = (1)
# print(type(tup))  #returns int
#
# tup=(1,)
# print(type(tup))  #returns tuple
#
# tup1=(1,4,2,3,5)
# if 1 in tup1:
#     print("yes")
# else:
#     print("No")
#
# tup2=tup1[1:4:2]
# print(tup2)

#tuples can be concatenated as a new tuple is being made

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")       #add item
# temp.pop(3)                 #remove item
# temp[2] = "Finland"         #change item
# countries = tuple(temp)
# print(countries)

# tuple1=(0,1,2,3,3,4,5)
# res=tuple1.count(3)
# res1=tuple1.index(3)
# res2=tuple1.index(3,2,5)
# #checks 3's occurence in 2-5 index
# res3=len(tuple1)

# sentence='Hey {} I am {}!'
# name1="X"
# name2="Y"
#
# print(sentence.format(name1,name2))
#
# #or
#
# sentence='Hey {1} I am {0}!'
# name1="X"
# name2="Y"
#
# print(sentence.format(name2,name1))
#
# #or
# #f-strings
# print(f"Hey {name1} I am {name2}!")
#
#
# txt = "Hey the price is {price:.2f}!"
# print(txt.format(price=4902.00043))
#
# price = 4902.00043
#
# #without
# txt = "Hey the price is {:.2f}!"
# print(txt.format(price))
#
# #f-strings
# print(f"Hey the price is {price:.2f}!")
#
# #print just a string
# print(f"{2*30}")
#
# #ignoring it
# print(f"Hey {{name1}} I am {{name2}}!")

#docstring

# def squar(a):
#
#     '''It returns the square of a number passed to it as a parameter.'''
#     return (a**2)
#
# print(squar.__doc__)
# print(squar(2))

for i in range(5):
    print(i)

else:
    print("no more i.")

#can be used with while loop too
#but

for i in range(5):
    print(i)
    if i==3:
        break;

else:
    print("no more i.")

#the else wont execute as loop broke but didnt go till end

for i in range(5):
    print("The number is {}".format(i+1))
else:
    print("no more i")