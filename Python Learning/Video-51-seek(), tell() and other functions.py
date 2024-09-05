# with open('myFile.txt','r') as f:
#    print(type(f))
#    f.seek(10)
#    # print(f.read(6))
#    print(f.tell())
#    #it should be written here
#    data=f.read(6)
#    print(data)
#
#    #goes from 0 to 10, 10 included



with open('myFile.txt', 'w') as f:
    f.write('If you happy and you know then clap your hands yo!')
    f.truncate(5)
f.close()
with open('myFile.txt','r') as f1:
   print(f1.read())
