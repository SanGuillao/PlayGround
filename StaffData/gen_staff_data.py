from staff import Staff
from random import randint
from random import choice
from string import ascii_uppercase

def generateStaffData():
    """ Will randomly generate staff data to be stored in new1 """
    id = randint(10000, 99999)
    firstName = ''.join(choice(ascii_uppercase) for i in range(randint(6, 20)))
    lastName = ''.join(choice(ascii_uppercase) for i in range(randint(7, 25)))
    totalWorkHours = randint(1, 200000)
    totalOvertime = randint(1, 20000)
    month = randint(1, 12)
    day = randint(1, 28)
    year = randint(1990, 2020)
    employDate = f"{month}:{day}:{year}"
    
    if id % 2 == 0:
        superFirstName = "Alexandre"
        superLastName = "Desplat"
    else:
        superFirstName = "Bruno"
        superLastName = "Coulais"
    
    new1 = Staff(id, firstName, lastName, totalWorkHours, totalOvertime, 
        superFirstName, superLastName, employDate)
    
    return new1
    

def outputStaffData(list_of_staff):
    """ Will ouput staff data to output file staffData.txt """
    
    with open('staffData.txt', 'w') as f:
        for line in list_of_staff:
            f.write(line.getAllFormatted())
            f.write('\n')
    