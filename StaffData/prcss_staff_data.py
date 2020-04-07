from staff import Staff

def unpack(line):
    """ takes in a line of Staff Data, and unpacks the values,
        returns a new object of Staff data
    """
    
    (id, firstName, lastName, twh, tot,  
        superFirst, superLast, employDate) = line.split()
    
    new1 = Staff(id, firstName, lastName, twh, tot, superFirst, superLast, 
        employDate)
    
    return new1
    
def loadData():
    """ Will load data from staffData.txt, return a list of staff """
    list_of_staff = []
    
    try:
        with open('staffData.txt', 'r') as f:
            for line in f:
                list_of_staff.append(unpack(line))
                    
        print("Success opening staffData.txt!")
        print(f"Total amount of staff personel: {len(list_of_staff)}")
        return list_of_staff
        
    except FileNotFoundError:
        print("staffData.txt not found! Please make sure file is with "
            "project")
   
def writeData(list_of_staff):
    """ will write the list of staff data to an output file called 
        results.txt
    """
    
    with open("results.txt", 'w') as f:
        for line in list_of_staff:
            f.write(line.getAllFormatted())
            f.write('\n')
        
        print("Successfully wrote data to results.txt!")

def formatDate(list_of_staff):
    """ formats the date information to show the actual Month"""
    
    list_of_months = ["Janauary", "February", "March", "April", "May",
        "June", "July", "August", "September", "October", "November",
        "December"]
    
    for line in list_of_staff:
        (month, day, year) = line.getEmployDate().split(':')
        month = list_of_months[int(month)-1]
        date = f"{month} {day}, {year}"
        line.setEmployDate(date)

def calculateSalary(list_of_staff):
    """ will take in a list_of_staff and calculate each employee salary 
        based on total works and total overtime
    """
    salary = 0
    
    for line in list_of_staff:
        salary = ((line.getTotalWorkHours() * 15) 
            + (line.getTotalOvertime() * 20))
        line.setSalary(salary)