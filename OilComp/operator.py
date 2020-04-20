from cuboidalTank import CuboidalTank
from hexagonalPrismTank import HexagonalPrismTank
from cylindricalTank import CylindricalTank
from utilities import getUserInputFromMenu

class OperatorDetails:
    def __init__(self, id, first_name, last_name, employDate, role):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        (self.month, self.day, self.year) = employDate.split(':')
        self.role = role
    
    def getRole(self):
        return self.role
        
    def getYear(self):
        return self.year
        
    def getMonth(self):
        return self.month
        
    def getDay(self):
        return self.day
    
    def printDetails(self):
        return (f"{self.id} {self.first_name} {self.last_name}"
            f" {self.month}:{self.day}:{self.year} {self.role}")

class Operator:
    def __init__(self):
        self.list_of_operators = []
        
    def unpack(self, line):
        (id, first_name, last_name, employDate, role) = line.split()
            
        return OperatorDetails(id, first_name, last_name, employDate, role)
    
    def loadOperators(self):
        try:
            with open("operators.txt", 'r') as f:
                for line in f:
                    self.list_of_operators.append(self.unpack(line))
        except FileNotFoundError:
            print("operators.txt not found! Please make sure file is with "
                "project")
        
    def printAllOperators(self):
        for line in self.list_of_operators:
            print(line.printDetails())
            
    def printByRole(self):
        user_input = input("Please enter role: ")
        
        for line in self.list_of_operators:
            if line.getRole() == user_input:
                print(line.printDetails())
                
    def printByYear(self):
        user_input = input("Please enter year: ")
        
        for line in self.list_of_operators:
            if line.getYear() == user_input:
                print(line.printDetails())
                
    def printByMonth(self):
        user_input = input("Please enter month: ")
        
        for line in self.list_of_operators:
            if line.getMonth() == user_input:
                print(line.printDetails())
                
    def printByDay(self):
        user_input = input("Please enter day: ")
        
        for line in self.list_of_operators:
            if line.getDay() == user_input:
                print(line.printDetails())
                
    def operatorMenu(self):
        cuboidal = CuboidalTank()
        hexa = HexagonalPrismTank()
        cylin = CylindricalTank()
        user_input = 0
        
        menu = "\tWelcome Operator!\n\n"
        menu += "\tEnter 1 to select Cuboidal Tank\n"
        menu += "\tEnter 2 to select Cylindrical Tank\n"
        menu += "\tEnter 3 to select Regular Right Hexagonal Prism Tank\n"
        menu += "\tEnter 4 to exit: "
        
        user_input = getUserInputFromMenu(menu)
        
        while True:
            if user_input == 4:
                return
            elif user_input == 1:
                cuboidal.tankMenu()
            elif user_input == 2:
                cylin.tankMenu()
            elif user_input == 3:
                hexa.tankMenu()
            else:
                print("Please enter an option from the menu..")
                
            user_input = getUserInputFromMenu(menu)
                