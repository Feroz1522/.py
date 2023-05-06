#User entering data
try :
    x = input("enter user name ")
    y = input("enter password ")
    user_id = x
    password = y

except :
    print('invalid data')
#server checking the users user id and password
def getdata():
    server_id = 'feroz'
    server_key = '5678'
    if server_id == user_id:
         if server_key == password:
            print(" logined successfully")
         else :
            print(" password invalid")
    else :
        print(" account has  not registered")
getdata()
