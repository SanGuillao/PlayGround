import control as c

filename = "students.txt"
data = {}
user = None

try:
    filename = input("Please input the name of the file (with extension): ")
except NameError:
    print(f"{filename} was not found, please make sure the name is correct")
    
data = c.readFromFile(filename)

user = c.menu()

while user != 4:

    if user == 0:
        c.displayAll(data)
    elif user == 1:
        c.displayGrads(data)
    elif user == 2:
        c.displayGPA(data)
    elif user == 3:
        c.displayDept(data)
    elif user == 4:
        print("\nExiting program now... \n")
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    user = c.menu()


#c.display(data)

#c.parseInfo(data)