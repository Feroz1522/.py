#Method 1 using "and"
code = True
skill = True
if code and skill :
    print(" Your are a coder and skillfull Programer ")
else :
    print(" you are not skillfull yet ")
# Output will be Your are a coder and skillfull Programmer because both values are true
    # if anyone value is false it doesn't show output

#Method 2 using "OR"
code = True
skill = False
if code or skill:
    print(" Your are a coder and skillfull Programer ")
else :
    print(" you are not skillfull yet ")
# Output will be Your are a coder and skillfull Programmer because any one values is true it's enough
    # if both value is false it will show if part

#Method using "not"

code = False
skill = False
if code and not (skill):
    print(" you are only a programer")
elif skill and not (code):
    print(" you are only a skillfull person")
elif code and skill :
    print(" Your are a coder and skillfull Programer ")
else :
    print("sorry you need to develop your skill")