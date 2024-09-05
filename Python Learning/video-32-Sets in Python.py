# s={2,4,2,6}
# print(s)
#
# #no order
# for i in s:
#     print(i)
#
# s3={False,2,"yay",(1,2),[1,2]}
# #list cant be stored in a set but a tuple can be
# for i in s3:
#     print(i)
# #empty dict
# s1={}
# print(type(s1))
#
# s2=set()
# print(type(s2))

# s4={1,2,3}
# s5={5,6}
# print(s4.union(s5))
# s4.update(s5)
# print(s4)

s6={1,2,3,7}
s7={3,2,5,6}
# # print(s6.intersection(s7))
# # s6.intersection_update(s7)
# # print(s6)
# #
# # s8=s6.symmetric_difference(s7)
# # print(s8)
#
# s9 = s6.difference(s7)
# print(s9)
#
# print(s6.isdisjoint(s7))
# print(s6.issubset(s7))
# print(s7.issuperset(s6))
#
# s6.add(9)
# print(s6)
#
# #update()
# #remove()/discard()
# #discard doesnt give errors even if we use an element is not present in the set and we are trying to remove it
# #pop()

item=s6.pop()
print(s6)
print(item)

#del()
#clear()

