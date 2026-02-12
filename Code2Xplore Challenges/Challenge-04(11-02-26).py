num=int(input("Enter number of elements to be in list:"))
list_com=[]
for i in range(num):
    list_com.append(input("Enter element"+str(i+1)+": "))
print(list_com)
num_list=[]
str_list=[]
for elt in list_com:
    if elt.isdigit():
        num_list.append(int(elt))
    elif elt.isalnum() and elt!="":
        str_list.append(elt)
print(num_list)
print(str_list)
print("Total numbers: ",len(num_list))
print("Total strings: ",len(str_list))
register_num = input("Enter Register Number: ")
last = int(register_num[-1])
if last % 2 == 0:
    reversed_num = []
    for elt in num_list:
        reversed_num.insert(0, elt)
    num_list = reversed_num
    print("After Personalization:", num_list)
else:
    reversed_str = []
    for elt in str_list:
        reversed_str.insert(0, elt)
    str_list = reversed_str
    print("After Personalization:", str_list)