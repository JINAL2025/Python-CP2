#This progarm copies the contents of a file into another file

import os, sys
flrname = input("Enter a file name to read the content : ")
if os.path.isfile(flrname) :
    fr = open(flrname, "r")
else :
    print(flrname, "does not exist")
    sys.exit()
flwname = input("Enter a file name to write the content : ")
fw = open(flwname, "a+")
ch= fr.read(1)
while ch!= "" :
    #fw.write(ch)
    #print(ch, end = "", file = fw, flush = True)
    print(ch, end = "", file = fw)
    #print(ch, end = "")
    ch = fr.read(1)
fr.close()
fw.close()
print(flrname, "is copied to", flwname, "successfully.")
