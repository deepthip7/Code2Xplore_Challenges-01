name=input("Enter your name:")
email_id=input("Enter your email id:")
number=input("Enter your number:")
age=int(input("Enter your age:"))
valid = True
if name[0] == " " or name[-1] == " ":
    valid = False
elif name.count(" ") <1:
    valid = False
if "@" not in email_id or "." not in email_id:
        valid = False
elif email_id[0] == "@":
        valid = False
if age<18 or age>60:
    valid = False
if len(number) != 10:
    valid = False
elif number[0] == "0":
    valid = False
elif not number.isdigit():
    valid = False
if valid:
    print("User profile is Valid")
else:
    print("User profile is Invalid")
