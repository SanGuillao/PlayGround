from operator import Operator
from utilities import getUserInputFromMenu


def mainMenu():
    menu = "Enter 1 for Manager Menu \n"
    menu += "Enter 2 for Operator Menu \n"
    menu += "Enter 3 to exit: "
    
    user_input = getUserInputFromMenu(menu)
    
    
    return(user_input)

def managerMenu(new_op):
    menu = "\tWelcome Manager!\n\n"
    menu += "\tEnter 1 to print all operators\n"
    menu += "\tEnter 2 to print only operators with a given role character\n"
    menu += "\tEnter 3 to print only operators with a given employment year\n"
    menu += "\tEnter 4 to print only operators with a given employment month\n"
    menu += "\tEnter 5 to print only operators with a given employment day\n"
    menu += "\tEnter 6 to exit: "
    
    user_input = getUserInputFromMenu(menu)
    
    while True:
        if user_input == 6:
            return
            
        elif user_input == 1:
            new_op.printAllOperators()
            
        elif user_input == 2:
            new_op.printByRole()
            
        elif user_input == 3:
            new_op_.printByYear()
            
        elif user_input == 4:
            new_op.printByMonth()
            
        elif user_input == 5:
            new_op.printByDay()
            
        else:
            print("Please enter an option from the menu")
        
        print("")
        user_input = getUserInputFromMenu(menu)
    

flag = True
user_input = 0
new_op = Operator()
new_op.loadOperators()

if len(new_op.list_of_operators) != 0:
    flag = False
    user_input = mainMenu()

while flag == False:
    if user_input == 3:
        flag = True
        break
        
    elif user_input == 1:
        managerMenu(new_op)
    
    elif user_input == 2:
        new_op.operatorMenu()
        
    else:
        print("Please enter an option from the menu")
    
    print("")
    user_input = mainMenu()
    