x = open("file.txt","r")
print(x.read())
print(x.readline())
print(x.readlines())
print(x.readlines()[2])
x.close()