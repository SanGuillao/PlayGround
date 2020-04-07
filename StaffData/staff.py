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
        
    def getAllFormatted(self):
        """ returns all of the information, formatted"""
        if self.salary:
            return(f"{self.id}, {self.firstName}, {self.lastName},"
            f" {self.totalWorkHours}, {self.totalOvertime},"
            f" {self.superFirstName}, {self.superLastName},"
            f" {self.salary}, {self.employDate}")
        else:
            return(f"{self.id} {self.firstName} {self.lastName}"
                f" {self.totalWorkHours} {self.totalOvertime}"
                f" {self.superFirstName} {self.superLastName}"
                f" {self.employDate}")