import control as c

filename = "students.txt"
data = {}
contents = ""

#filename = input("Please input the name of the file (with extension): ")

data = c.readFromFile(filename)

c.display(data)