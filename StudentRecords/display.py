def menu():
    """ Allow user to pick an option, return user choice as int """
    user = None
    temp = "Press 0 to print all students\n"
    temp += "Press 1 to print only students who have graduated\n"
    temp += "Press 2 to print only students who have a GPA >= a given amount\n"
    temp += "Press 3 to print only students of a given major\n"
    temp += "\nPress 4 to sort students based on graduation date\n"
    temp += "Press 5 to sort students based on GPA\n"
    temp += "Press 6 to exit: "
    
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
        
 
def sortOnGradDate(data):
    """ Sorts and prints students based on Graduation Date"""
    
    tempList = data[:]
    
    for line in tempList:
        try:
            (month, day, year) = line['dateOfGrad'].split(":")
            line['month'] = int(month)
            line['day'] = int(day)
            line['year'] = int(year)
        except ValueError:
            line['year'] = 0
    
    tempList = sorted(tempList, key = lambda k: k['year'], reverse = True)
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    
    for line in tempList:
        print(displayFormat(line))

def sortOnGPA(data):
    """ Sorts and prints students based on GPA """
    
    sortedList = sorted(data, key = lambda k: k['gpa'], reverse = True)
    
    print("".center(80, '*'))
    print("".center(80, '*'))
    
    for line in sortedList:
        print(displayFormat(line))