def menu():
    menu = "---Basic Calculator---"
    menu += "\n1. Addition"
    menu += "\n2. Subtraction"
    menu += "\n3. Multiplication"
    menu += "\n4. Division"
    menu += "\n0. Quit"
    
    print(menu)

def prompt_input():
    prompt = "\nWelcome to our basic calculator! Please enter an option: "
    user_input = int(input(prompt))
    return user_input
    
def addition():
    x = int(input("Please enter the first number you wish to add: "))
    y = int(input("Please enter the second number you wish to add: "))
                            
    total = x + y
    print(f"{x} + {y} = {total}")
    
def control():
    quit = False
    
    while quit == False:
        menu_input = prompt_input()
        if(menu_input == 0):
            quit = True
            break
    
        elif(menu_input == 1):
            addition()
        elif(menu_input == 2):
            break
        elif(menu_input == 3):
            break
        elif(menu_input == 4):
            break
        
        print(menu())