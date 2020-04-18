from operator import Operator

def mainMenu():
    menu = "Enter 1 for Manager Menu \n"
    menu += "Enter 2 for Operator Menu \n"
    menu += "Enter 3 to exit: "
    
    try:
        user_input = int(input(menu))
    except ValueError:
        while True:
            try:
                user_input = int(input("Please enter an option from the"
                    " menu: "))
                break
            except ValueError:
                pass
    
    
    return(user_input)

def managerMenu():
    menu = "\tWelcome Manager!\n\n"
    menu += "\tEnter 1 to print all operators\n"
    menu += "\tEnter 2 to print only operators with a given role character\n"
    menu += "\tEnter 3 to print only operators with a given employment year\n"
    menu += "\tEnter 4 to print only operators with a given employment month\n"
    menu += "\tEnter 5 to print only operators with a given employment day\n"
    menu += "\tEnter 6 to exit: "
    
    try:
        user_input = int(input(menu))
    except ValueError:
        while True:
            try:
                user_input = int(input("Please enter an option from the"
                    " menu: "))
                break
            except ValueError:
                pass
    
    while True:
        if user_input == 6:
            return
    

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
        managerMenu()
    
    elif user_input == 2:
        new_op.operatorMenu()
    
    print("")
    user_input = mainMenu()
    
#new1 = Operator()

#new1.loadOperators()
#new2 = CuboidalTank()

#print(f"The tank needs {new2.getAmntPartial()} units")

#new1.printAllOperators()
#new1.printByRole()
    
"""while True:
    try:
        user_input = int(input(Menu()))
        break
    except ValueError:
        print("Please enter a choice from the menu")

from cuboidalTank import CuboidalTank
from hexagonalPrismTank import HexagonalPrismTank
from cylindricalTank import CylindricalTank

new1 = CuboidalTank()
new2 = HexagonalPrismTank()
new3 = CylindricalTank()

print(new1.getCurrentVolume())
print(new2.getCurrentVolume())
print(new3.getCurrentVolume())"""