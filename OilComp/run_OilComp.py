def Menu():
    menu = "Enter 1 for Manager Menu \n"
    menu += "Enter 2 for Operator Menu \n"
    menu += "Enter 3 to exit: "
    
    return(menu)
    
while True:
    try:
        user_input = int(input(Menu()))
        break
    except ValueError:
        print("Please enter a choice from the menu")

"""from cuboidalTank import CuboidalTank
from hexagonalPrismTank import HexagonalPrismTank
from cylindricalTank import CylindricalTank

new1 = CuboidalTank()
new2 = HexagonalPrismTank()
new3 = CylindricalTank()

print(new1.getCurrentVolume())
print(new2.getCurrentVolume())
print(new3.getCurrentVolume())"""