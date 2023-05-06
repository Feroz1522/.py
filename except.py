try:
    print(" enter value for dividing values")
    x = int(input(" >> "))
    y = int(input(" >> "))
    sum = x / y
    print(f" Answer is {sum}")
except ValueError:
    print(" enter numbers ")     
except TypeError:
    print("numbers are accepatable")
except ZeroDivisionError:
    print('zero cannot be divide other input value')