file1 = "example.txt"
with open(file1, "w") as file :
    file.write("Hello, Windows IDLE!\n")
    file.write("This is a file handling example\n")
print(f"{file1} has been created and written.")
