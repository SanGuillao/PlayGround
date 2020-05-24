import random

class CWIS:
    """ a class to simulate a CWIS defense turret """
    def __init__(self):
        """ nothing to initialize """
    
    def menu(self):
        """ present the user with the control interface """
        listOfTargets = []
        user_input = ''
        while user_input != 'N' and user_input != 'n':
            self.genTargets(listOfTargets)
            self.display(listOfTargets)
            user_input = input("Do you wish to run again? [Y/N] ")
            listOfTargets.clear()
            
    def genTargets(self, listOfTargets):
        """ generate a random amount of targets and assign them random threat levels """
        randTargets = int(random.uniform(4, 11))
        randThreat = random.normalvariate(100, 15)
        
        for i in range(randTargets):
            listOfTargets.append(randThreat)
            randThreat = random.normalvariate(100, 15)
        
        listOfTargets.sort()
        listOfTargets.reverse()
        
    def display(self, listOfTargets):
        """ display the list of targets in neat format """
        targetNum = 1
        burst = 0
        
        for obj in listOfTargets:
            burst = self.destroy()
            print("Target #{} \tThreat: {:.2f} \tBurst: {}".format(targetNum, obj, burst))
            targetNum += 1
            
    def destroy(self):
        """ calculate how many burst of fire before object is destroyed """
        burst = 0
        temp = int(random.uniform(0, 4))
        # print(temp)
        check = False
        while check == False:
            if temp == 0:
                burst += 1
                return burst
            
            burst += 1
            temp = int(random.uniform(0, 4))
            
        return burst

if __name__ == '__main__':
    new1 = CWIS()
    new1.menu()