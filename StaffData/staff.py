class Staff:
    def __init__(self, id, fn, ln, twh, tot, sfn, sln, edate, salary=None):
        self.id = id
        self.firstName = fn
        self.lastName = ln
        self.totalWorkHours = twh
        self.totalOvertime = tot
        self.superFirstName = sfn
        self.superLastName = sln
        self.employDate = edate
        self.salary = salary
        
    def setSalary(self, salary):
        """ sets the salary variable = to the parameter passed in """
        self.salary = salary
        
    def setEmployDate(self, date):
        """ set employ date value = to the parameter passed in """
        self.employDate = date
        
    def getEmployDate(self):
        """ returns employ date as a string """
        return self.employDate
    
    def getTotalWorkHours(self):
        """ returns the total hours worked as an int """
        return int(self.totalWorkHours)
        
    def getTotalOvertime(self):
        """ returns the total overtime hours as in int """
        return int(self.totalOvertime)
        
    def getAllFormatted(self):
        """ returns all of the information, formatted"""
        if self.salary:
            return(f"{self.id}, {self.firstName}, {self.lastName},"
            f" {self.totalWorkHours}, {self.totalOvertime},"
            f" {self.superFirstName}, {self.superLastName},"
            " ${:.2f},"
            f" {self.employDate}".format(self.salary))
        else:
            return(f"{self.id} {self.firstName} {self.lastName}"
                f" {self.totalWorkHours} {self.totalOvertime}"
                f" {self.superFirstName} {self.superLastName}"
                f" {self.employDate}")