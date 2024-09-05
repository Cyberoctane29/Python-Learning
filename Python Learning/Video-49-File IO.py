# f=open('myFile.txt','r')
# # print(f)
# text=f.read()
# f.close()
#
# print(text)

# f1=open('myFile1.txt','w')
#if file doesnt exist then it would be created
#if we open an existing txt file with content in write mode then the content in it will be removed

#t and b can added with r
#by default r has t with it hence it basically rt by default and we dont have to specify it but for b we have to write rb
#in w mode we have to write f.write and in a mode too we have to write f.write

#alternate way without closing file

#context manager

# with open('myFile.txt', 'r') as f:
#     content = f.read()
#
# print(content)

# with open('myFile1.txt', 'w') as f:
#     f.write('Hey, I am Saswat!')
#
# with open('myFile1.txt','r')as f1:
#     content=f1.read()
#     print(content)


# f1=open('myFile.txt','w')
# f1.write('Saswat is gonna flourish in his life!')

# f=open('myFile.txt','r')
#
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)

# f = open('marks.txt', 'r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#
#     if not line:
#         break
#
#     # Strip newline characters and split by comma
#     line = line.strip()
#     parts = line.split(',')
#
#     if len(parts) < 3:
#         print(f'Error in line {i}: {line}')
#         continue
#
#     m1 = parts[0]
#     m2 = parts[1]
#     m3 = parts[2]
#
#     print(f'Student {i}: {m1}')
#     print(f'Student {i}: {m2}')
#     print(f'Student {i}: {m3}')
#     print(line)
#
# f.close()

f1=open('myFile1.txt','w')
lines=['I am happy!\n','I am amazing!\n','I am nice!\n']
f1.writelines(lines)
f1.close()

f1=open('myFile1.txt','r')
content=f1.read()
print(content)