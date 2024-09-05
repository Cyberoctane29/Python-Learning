# dict={1:"Saswat",3:"Rick",2:"Ricky"}
# print(dict[1]) #throws error if key doesnt exist
# print(dict.get(1)) #doesnt throw error if key doesnt exist
# print(dict)
# print(dict.keys())
#
# for key in dict.keys():
#     print(key)
#     print(dict[key])
#
#     #as ordered hence they are in the same order in the output too
#
#     print(dict.values())
#
#     for key in dict.keys():
#         print(f"The value corresponding to {key} is {dict[key]}.")
#
#
# print(dict.items())
# for key,value in dict.items():
#     print(f"The value corresponding to {key} is {value}.")

dict2={1:"Saswat",3:"Rick",2:"Ricky"}
dict3={4:"Seth",5:"Singer"}
#
# dict2.update(dict3)
# print(dict2)
#
# #empty dictionary
# empt={}
# print(type(empt))
#
# dict2.pop(3)
# print(dict2)
#
# dict2[3]="Ricky"
# print(dict2)
#
# dict2.popitem()
# print((dict2))

# del dict3
# print(dict3)

dict2[3]="Ricky"
dict2[4]="Singer"
dict2[5]="Rick"
print(dict2)
del dict2[5]
print(dict2)

