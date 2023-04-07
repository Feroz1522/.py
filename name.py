name=input("Enter Your Name")
if len(name)<=3:
    print(" Name must need to be atleast 3 Character")
elif len(name)>=50:
    print('Name can be maximum of  50 character')
else:
    print('Good Name ')