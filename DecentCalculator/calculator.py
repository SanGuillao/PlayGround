class Calc:
    """ A class modeling the functions of a calculator """
    
    #def __init__(self):

    def menu(self):
        """ Will output Calculator Menu """
        menu = "---Basic Calculator---"
        menu += "\n1. Addition"
        menu += "\n2. Subtraction"
        menu += "\n3. Multiplication"
        menu += "\n4. Division"
        menu += "\n0. Quit"
        
        return(menu)
    
    def prompt_input(self):
        """ Will allow the user to input a choice based off the menu """
        prompt = "\nWelcome to our basic calculator! Please enter an option: "
        user_input = input(prompt)
        return user_input
        
    def addition(self):
        """ Asks the user for x and y, adds using x + y, prints total """
        while True:
            try:
                x = int(input("Please enter the first number you wish to add:" 
                    " "))
                y = int(input("Please enter the second number you wish to" 
                    "add: "))
                
                total = x + y
                print(f"{x} + {y} = {total}")
                return None
                    
            except ValueError:
                print("Please make sure to enter numerical values...")
                
    def subtraction(self):
        """ Asks the user for x and y, subtracts using x - y, prints total """
        while True:
            try:
                x = int(input("Please enter the first number you wish to "
                    "subtract: "))
                y = int(input("Please enter the second number you wish to "
                    "subtract: "))
                    
                total = x - y
                print(f"{x} - {y} = {total}")
                return None
                    
            except ValueError:
                print("Please make sure to enter numerical values...")

    def multiplication(self):
        """ Asks the user for x and y, multiplies using x * y, prints total """
        while True:
            try:
                x = int(input("Please enter the first number you wish to"
                    " multiply: "))
                y = int(input("Please enter the second number you wish to"
                    " multiply: "))
                    
                total = x * y
                print(f"{x} * {y} = {total}")
                return None
                    
            except ValueError:
                print("Please make sure to enter numerical values...")

    def division(self):
        """ Asks the user for x and y, divides using x / y, prints total """
        while True:
            try:
                x = int(input("Please enter the first number you wish to "
                    "divide: "))
                y = int(input("Please enter the second number you wish to "
                    "divide: "))
                    
                total = x / y
                print(f"{x} / {y} = {total}")
                return None
                    
            except ValueError:
                print("Please make sure to enter numerical values...")
              
            except ZeroDivisionError:
                print("You can't divide by 0!")
                
            
        
    def control(self):
        """ 
        Controls the entire program, allows user to pick different 
        functions, or to end the program
        """
        quit = False
        user_input = -1
        
        print(self.menu())
        
        while quit == False:
            try:
                user_input = int(self.prompt_input())
                if(user_input == 0):
                    quit = True
                    break
            
                elif(user_input == 1):
                    self.addition()
                elif(user_input == 2):
                    self.subtraction()
                elif(user_input == 3):
                    self.multiplication()
                elif(user_input == 4):
                    self.division()
                
                print()
                print(self.menu())
            except ValueError:
                print("Please choose an option on the menu...")
        
        print("\nThank you for using the basic calculator!!") 