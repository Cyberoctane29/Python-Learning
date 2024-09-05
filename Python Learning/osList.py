import os
folders=os.listdir("data")
# print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir((f"data/{folder}")))

print(os.getcwd())

#also

os.chdir("/Users")
print(os.getcwd())

#as dir is changed hence the for loop block wont work


