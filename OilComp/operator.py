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
        return ("TO DO")

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
        