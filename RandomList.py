import random
lst1 = [0,0,0,0,0]
lst2 = [0,0,0,0,0]
i=0
while i<5:
    a = random.randint(1,100)
    if a%2!=0 :
        lst1[i] = a
        i=i+1
print(lst1,"is a list of random odd numbers between 1 and 100")
j=0
while j<5:
    a = random.randint(1,100)
    if a%2==0 :
        lst2[j] = a
        j=j+1
print(lst2,"is a list of random even numbers between 1 and 100")
