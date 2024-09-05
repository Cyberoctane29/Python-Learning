# def cube(x):
#     return x*x*x
l=[1,2,3,4,5]

# res=[]
# for i in l:
#     res.append(cube(i))
#
# print(res)

#or using map

# l=map(cube,l)
# print(l) #returns map object

#convert to list
# l=list(map(cube,l))
# print(l)

#can be lambda function too

# l1=list(map(lambda x:x*x*x,l))
# print(l1)

#filter

# def filter_func(x):
#     return x>4

# filterList=list(filter(filter_func,l))
# print(filterList)

#with lambda
# filterList=list(filter(lambda x:x>4,l))
# print(filterList)

#reduce
#reduce needs to be imported

from functools import reduce
# # def sum(x,y):
# #       return x+y
# #
# # listNre=reduce(sum,l)
# # print((listNre))

listNre=reduce(lambda x,y:x+y,l)
print(listNre)