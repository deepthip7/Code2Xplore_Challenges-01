n=int(input(("Enter number of students: ")))
students_marks=[]
for i in range(n):
   students_marks.append(int(input("Enter student "+str(i+1)+" marks : " )))
valid_students=0
failed_students=0
for mark in students_marks:
    if mark<0 or mark>100:
        print(f"{mark}->Invalid")
    else:
        valid_students+=1
        if mark>=90 and mark<=100:
            print(f"{mark} -> Excellent")
        elif mark>=75 and mark<90:
            print(f"{mark} -> Very Good")
        elif mark>=60 and mark<=74:
            print(f"{mark} -> Good")
        elif mark>=40 and mark<60:
            print(f"{mark} -> Average")
        else:
            print(f"{mark} -> Fail")
            failed_students+=1
print("Total Valid students: ",valid_students)
print("Total failed students: ",failed_students)