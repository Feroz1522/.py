weight=input("enter your weight : ")
c=input("(L)bs or (K)g : ")

if c.upper()=='k':
    print(int(weight)*2.20 )
if c.upper()=='l':
    print( int(weight)*0.45 ) 