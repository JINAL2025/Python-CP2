import random
lst1= [0,0,0,0,0]
i=0
while i<5:
    a = random.randint(1,1000)
    if a%2!=0 :
        lst1[i] = a
        i=i+1
print(lst1)
