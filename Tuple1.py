list = ['Jinal', 'Jahnavi', ('Harsh',)]
boys = 0
for i in range(0,len(list)) :
    if isinstance(list[i],tuple) != 0 :
        boys+=1
print("The number of boys is ", boys)
print("The number of girls is ", len(list) - boys)
