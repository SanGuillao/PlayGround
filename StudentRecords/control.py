def unpack(line):
    """ 
    Unpack the information from the line into seperate variables 
    returns a dict called student
    """
    student = {
            'firstName' : '',
            'lastName' : '',
            'id' : '',
            'dept' : '',
            'gpa' : 0.0,
            'status' : '',
            'dateOfGrad' : ''
        }
        
    try:
        (firstName, lastName, id, dept, gpa, status, dateOfGrad) = line.split()
        student['firstName'] = firstName
        student['lastName'] = lastName
        student['id'] = id
        student['dept'] = dept
        student['gpa'] = float(gpa)
        student['status'] = status
        student['dateOfGrad'] = dateOfGrad
    
    except ValueError:
        (firstName, lastName, id, dept, gpa, status) = line.split()
        student['firstName'] = firstName
        student['lastName'] = lastName
        student['id'] = id
        student['dept'] = dept
        student['gpa'] = float(gpa)
        student['status'] = status
    
    return student
    
def readFromFile(filename):
    """ Read from filename, return the data as a dict """
    
    listOfStudents = []
    
    while True:
        try:
            with open(filename, 'r') as f:
                for line in f:
                    listOfStudents.append(unpack(line))
            
            print(f"Success opening {filename}")
            print(f"Total amount of students: {len(listOfStudents)}")
            print("")
            return listOfStudents
            
        except FileNotFoundError:
            filename = input(f"The file {filename} could not be found. "
                "Please make sure it is exists within the project folder: ")

def menu():
    """ Allow user to pick an option, return user choice as int """
    user = None
    temp = "Press 0 to print all students\n"
    temp += "Press 1 to print only students who have graduated\n"
    temp += "Press 2 to print only students who have a GPA >= a given amount\n"
    temp += "Press 3 to print only students of a given major\n"
    temp += "Press 4 to exit: "
    
    user = input(temp)
    
    while True:
        try:
            user = int(user)
            return user
        except ValueError:
            pass
        user = input("Invalid entry, please input a value from the menu: ")
    
def displayFormat(line):
    """ format the information passed in, return it as a string """
    
    return(f"{line['firstName'].ljust(9, ' ')} "
            f"{line['lastName'].ljust(15, ' ')} {line['id'].ljust(15, ' ')} "
            f"{line['dept'].ljust(10, ' ')} "
            "{:.2f}"
            f"{line['status'].rjust(7, ' ')} "
            f"{line['dateOfGrad'].rjust(15, ' ')}".format(line['gpa']))

def displayAll(data):
    """ Prints out all students in data in neat format """
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    
    for line in data:
        print(displayFormat(line))
        
            
def displayGrads(data):
    """ Print out only students who have graduated """
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    
    for line in data:
        if line['status'] == 'Y':
            print(displayFormat(line))
                
def displayGPA(data):
    """ Print out students who's GPA is a certain amnt """
    
    user_amnt = input("Please input the GPA amount: ")
    
    while True:
        try:
            user_amnt = float(user_amnt)
            break
        except ValueError:
            pass
            
        user_amnt = input("Invalid entry, please enter a number: ")
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    
    for line in data:
        if line['gpa'] >= user_amnt:
            print(displayFormat(line))
                
def displayDept(data):
    """ Print out students who belong to a certain Major """
    
    flag = False
    user_in = input("Please enter major filter: ")
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    
    for line in data:
        if user_in.lower() == line['dept'].lower():
            print(displayFormat(line))
            flag = True
    
    if flag == False:
        print(f"Sorry, we could not find any Major matching {user_in} "
            "Please make sure input is correct.")
        
            