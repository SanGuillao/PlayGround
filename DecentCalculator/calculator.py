class Calc:
    """ A class modeling the functions of a calculator """
    
    def __init__(self):
        self.user_input = -1

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
        self.user_input = int(input(prompt))
        #return user_input
        
    def addition(self):
        """ Asks the user for x and y, adds using x + y, prints total """
        x = int(input("Please enter the first number you wish to add: "))
        y = int(input("Please enter the second number you wish to add: "))
                            
        total = x + y
        print(f"{x} + {y} = {total}")

    def subtraction(self):
        """ Asks the user for x and y, subtracts using x - y, prints total """
        x = int(input("Please enter the first number you wish to "
            "subtract: "))
        y = int(input("Please enter the second number you wish to "
            "subtract: "))
                                
        total = x - y
        print(f"{x} - {y} = {total}")

    def multiplication(self):
        """ Asks the user for x and y, multiplies using x * y, prints total """
        x = int(input("Please enter the first number you wish to"
            " multiply: "))
        y = int(input("Please enter the second number you wish to"
            " multiply: "))
                              
        total = x * y
        print(f"{x} * {y} = {total}")
    
    def division(self):
        """ Asks the user for x and y, divides using x / y, prints total """
        x = int(input("Please enter the first number you wish to divide:"
            " "))
        y = int(input("Please enter the second number you wish to divide:"
            " "))
                                
        total = x / y
        print(f"{x} / {y} = {total}")
        
    def control(self):
        """ 
        Controls the entire program, allows user to pick different 
        functions, or to end the program
        """
        quit = False
        
        print(self.menu())
        
        while quit == False:
            self.prompt_input()
            if(self.user_input == 0):
                quit = True
                break
        
            elif(self.user_input == 1):
                self.addition()
            elif(self.user_input == 2):
                self.subtraction()
            elif(self.user_input == 3):
                self.multiplication()
            elif(self.user_input == 4):
                self.division()
            
            print()
            print(self.menu())
        
        print("\nThank you for using the basic calculator!!") 