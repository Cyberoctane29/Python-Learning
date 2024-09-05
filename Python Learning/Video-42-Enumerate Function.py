fruits=['banana','apple','plum','lichi','pineapple','orange']
# for index,fruit in enumerate(fruits):
#     print(fruit)
#     if(fruit=='pineapple'):
#         print(f"Its my favorite and its in {index}!")
#         break

#writing index,fruit unpacks the tuples

print(list(enumerate(fruits)))
#or
# for v in enumerate(fruits):
#     print(v)

#prints the tuples of (index,fruit) pairs

for index,fruit in enumerate(fruits,start=1):
    print(fruit)
    if index==5:
        print("My favorite fruit!")
    # if(fruit=='pineapple'):
    #     print(f"Its my favorite and its in {index}!")
