with open("new.txt","w") as file:
   file.write("Name:John\n")
   file.write("Age:20\n")
with open("new.txt","r") as file:
    print(file.read())