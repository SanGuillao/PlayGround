import control as c

filename = "students.txt"
data = {}
user = None

#filename = input("Please input the name of the file (with extension): ")

data = c.readFromFile(filename)

user = c.menu()

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

#c.display(data)

#c.parseInfo(data)