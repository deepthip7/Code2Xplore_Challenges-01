student_id=input("Enter student ID: ")
email_id=input("Enter student email id: ")
password=input("Enter password: ")
code=input("Enter Referral code: ")
valid=True
if not (
    len(student_id) == 7 and
    student_id[0:3] == "CSE" and
    student_id[3] == "-" and
    student_id[4].isdigit() and
    student_id[5].isdigit() and
    student_id[6].isdigit()
):
    valid = False
if (
    "@" not in email_id or "." not in email_id and email_id[0] == "@" and email_id[-1] == "@" and email_id[-4:-1] != ".edu"
):
    valid = False
if not len(password)>=8 :
    valid = False
elif not password[0]>='A' and password[0]<='Z':
    valid = False
elif not (password[1].isdigit() or
     password[2].isdigit() or
     password[3].isdigit() or
     password[4].isdigit() or
     password[5].isdigit() or
     password[6].isdigit() or
     password[7].isdigit()
):
    valid = False
if not(
    len(code)==6 and
    code[0:3]=="REF" and code[3].isdigit() or code[4].isdigit() and code[-1]=='@'
):
    valid = False
if valid:
    print("APPROVED")
else:
    print("REJECTED")