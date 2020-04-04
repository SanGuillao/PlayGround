import body as b
import display as d

filename = "students.txt"
data = {}
user = None

try:
    filename = input("Please input the name of the file (with extension): ")
except NameError:
    print(f"{filename} was not found, please make sure the name is correct")
    
data = b.readFromFile(filename)

user = d.menu()

while user != 6:

    if user == 0:
        d.displayAll(data)
    elif user == 1:
        d.displayGrads(data)
    elif user == 2:
        d.displayGPA(data)
    elif user == 3:
        d.displayDept(data)
    elif user == 4:
        d.sortOnGradDate(data)
    elif user == 5:
        d.sortOnGPA(data)
    else:
        print("\nPlease make sure you are inputting an option from the menu..")
        
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    user = d.menu()

print("\nExiting program now... \n")
#c.display(data)

#c.parseInfo(data)