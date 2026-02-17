n = int(input("Enter weights: "))
list = []
for i in range(n):
    weight = int(input("Enter weight " + str(i+1) + ": "))
    list.append(weight)
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]
full_name = "Paruchuru Deepthi Sri"
L = 0
for ch in full_name:
    if ch != " ":
        L += 1
PLI = L % 3
valid_weights = 0
affected = 0
for i in list:
    if i < 0:
        invalid_entries.append(i)
    elif i >= 0 and i <= 5:
        very_light.append(i)
        valid_weights += 1
    elif i >= 6 and i <= 25:
        normal_load.append(i)
        valid_weights += 1
    elif i >= 26 and i <= 60:
        heavy_load.append(i)
        valid_weights += 1
    else:
        overload.append(i)
        valid_weights += 1
if PLI == 0:
    for item in overload:
        invalid_entries.append(item)
        affected += 1
    overload = []
elif PLI == 1:
    affected = len(very_light)
    very_light = []
elif PLI == 2:
    affected = len(very_light) + len(overload)
    very_light = []
    overload = []
print("length value :", L)
print("PLI value :", PLI)
print("Very Light Packages :", very_light)
print("Normal Load Packages :", normal_load)
print("Heavy Load Packages :", heavy_load)
print("Overload Packages :", overload)
print("Invalid Entries :", invalid_entries)
print("Total Valid Weights :", valid_weights)
print("Items Affected due to PLI :", affected)
register_num = input("Enter Register Number: ")
last = int(register_num[-1])
if last % 2 == 0:
    reversed_weights = []
    for elt in list:
        reversed_weights.insert(0, elt)
    list = reversed_weights
    print("After Personalization:", list)
else:
    reversed_invalid = []
    for elt in invalid_entries:
        reversed_invalid.insert(0, elt)
    invalid_entries = reversed_invalid
    print("After Personalization:", invalid_entries)