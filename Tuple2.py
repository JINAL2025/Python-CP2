list1 = [(136,'Jinal',17), (165,'Mahi',17), (175,'Jahnavi',18), (178,'Pal',18), (185,'Krisha',18)]
l = len(list1)
roll = [0]*l
name = [0]*l
age = [0]*l
for i in range(0, l) :
    roll[i] = list1[i][0]
    name[i] = list1[i][1]
    age[i] = list1[i][2]
print("Roll numbers : ", roll)
print("Names : ", name)
print("Ages : ", age)
