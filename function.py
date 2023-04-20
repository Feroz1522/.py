#getting data from User                 

#Method_1
print("Method 1 :")

def get_data1():
    print("enter your name " )
    x = input(">")
    print("enter your age "  )
    y = input(">")
    print(f"your name is {x} and your age is {y}")
    print("thank you for sharing your data")
get_data1()

#Method_2
print("Method 2 :")
def get_data(name,age):
    print("enter Your name " + name)
    print("your age is " + str(age))
    print(f"your name is {name} and age is {age} .thank you for sharing your data")
get_data("Feroz","19")