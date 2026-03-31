#This program reads the contents of a file
import os, sys
flname = input("Enter a file name to read its contents : ")
if os.path.isfile(flname) :
    f = open(flname, "r")
else :
    print(flname, "does not exist.")
    sys.exit()
ch = f.read(1)
while ch :
    print(ch, end = "")
    ch = f.read(1)
f.close()
