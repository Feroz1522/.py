engine = False
cmd = ""
print(' Game has been Started ')
while True:
    
    in_put=input('>').lower()

    if in_put=="start":     
        if engine: # engine =True
            print(' Bike has been already Started ')
        else :
            engine = True
            print(' Bike has been Started ')

    elif in_put == "stop":
        if not engine: # if!=True
            print('Car has been already Stopped')
        else:
            engine = False
            print('Car has been stoped')
    elif in_put == "quit":
        print("game has been quitted")
        break