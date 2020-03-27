def menu():
    """ Will output Calculator Menu """
    menu = "---Basic Calculator---"
    menu += "\n1. Addition"
    menu += "\n2. Subtraction"
    menu += "\n3. Multiplication"
    menu += "\n4. Division"
    menu += "\n0. Quit"
    
    print(menu)

def prompt_input():
    """ Will allow the user to input a choice based off the menu """
    prompt = "\nWelcome to our basic calculator! Please enter an option: "
    user_input = int(input(prompt))
    return user_input
    
def addition():
    """ Asks the user for x and y, adds using x + y, prints total """
    x = int(input("Please enter the first number you wish to add: "))
    y = int(input("Please enter the second number you wish to add: "))
                            
    total = x + y
    print(f"{x} + {y} = {total}")
    
def subtraction():
    """ Asks the user for x and y, subtracts using x - y, prints total """
    x = int(input("Please enter the first number you wish to subtract: "))
    y = int(input("Please enter the second number you wish to subtract: "))
                            
    total = x - y
    print(f"{x} - {y} = {total}")
    
def multiplication():
    """ Asks the user for x and y, multiplies using x * y, prints total """
    x = int(input("Please enter the first number you wish to multiply: "))
    y = int(input("Please enter the second number you wish to multiply: "))
                            
    total = x * y
    print(f"{x} * {y} = {total}")
    
def division():
    """ Asks the user for x and y, divides using x / y, prints total """
    x = int(input("Please enter the first number you wish to divide: "))
    y = int(input("Please enter the second number you wish to divide: "))
                            
    total = x / y
    print(f"{x} / {y} = {total}")
    
def control():
    """ 
    Controls the entire program, allows user to pick different 
    functions, or to end the program
    """
    quit = False
    
    while quit == False:
        menu_input = prompt_input()
        if(menu_input == 0):
            quit = True
            break
    
        elif(menu_input == 1):
            addition()
        elif(menu_input == 2):
            subtraction()
        elif(menu_input == 3):
            multiplication()
        elif(menu_input == 4):
            division()
        
        print(menu())