#This program counts the number of lines, words and characters in a file
import os, sys
flrname = input("Enter a file name to count the number of lines, words and characters : ")
if os.path.isfile(flrname) :
    fr = open(flrname, "r")
else :
    print(flrname, "does not exist.")
    sys.exit()

