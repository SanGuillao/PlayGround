from utilities import getUserInputFromMenu
import math

class CylindricalTank:
    def __init__(self, radius = 6, height = 400, lqd_height = 0):
        self.radius = radius
        self.height = height
        self.liquid_height = lqd_height
        self.max_volume = math.pi * radius * radius * height
        
    def getCurrentVolume(self):
        return self.liquid_height * math.pi * self.radius * self.radius
    
    def getMaxVolume(self):
        return self.max_volume
    
    def getAmntToFill(self):
        return self.max_volume - self.getCurrentVolume()
        
    def getAmntPartial(self, user_input):
        newVolume = 0.0
        self.getCurrentVolume()
        
        while True:
            try:
                newVolume = int(input("Please enter amount to fill: "))
                break
            except ValueError:
                print("Please enter a numerical value")
        
        newVolume = newVolume * math.pi * self.radius * self.radius
        
        return newVolume - self.liquid_height
    
    def setLiquidHeight(self, amnt_oil):
        self.liquid_height += amnt_oil
        
    def tankMenu(self):
        menu = "\t\tCylindrical Tank\n\n"
        menu += "\t\tEnter 1 to get max possible volume\n"
        menu += "\t\tEnter 2 to get current volume\n"
        menu += "\t\tEnter 3 to supply oil\n"
        menu += "\t\tEnter 4 to get amnt to completly fill tank\n"
        menu += "\t\tEnter 5 to get amnt to partially fill tank\n"
        menu += "\t\tEnter 6 to exit: "
        
        user_input = getUserInputFromMenu(menu)
        
        while True:
            if user_input == 6:
                return
                
            elif user_input == 1:
                print(self.getMaxVolume())
                
            elif user_input == 2:
                print(self.getCurrentVolume())
                
            elif user_input == 3:
                try:
                    amnt = int(input("How much oil: "))
                    self.setLiquidHeight(amnt)
                    print(f"{amnt} ltrs has been added to the tank")
                    print(f"The tank has {self.getCurrentVolume()} units of" 
                        " oil")
                except ValueError:
                    print("Error! A numerical value was expected, but not"
                        " received!")
                
            elif user_input == 4:
                print(self.getAmntToFill())
                
            elif user_input == 5:
                print(self.getAmntPartial())
            
            else:
                print("Please enter an option from the menu..")
            
            user_input = getUserInputFromMenu(menu)