dict1 = {"Uppercase_Count" : 0, "Lowercase_Count" : 0}

def count_lower_upper(str):
    
    u = 0
    l = 0
    for ch in str :
        if ch.islower() :
            l+=1
        else :
            u+=1
    dict1["Uppercase_Count"] = u
    dict1["Lowercase_Count"] = l
    print(dict1)

string1 = input("Enter a word : ")
count_lower_upper(string1)
