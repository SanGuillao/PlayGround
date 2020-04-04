def unpack(line):
    """ 
    Unpack the information from the line into seperate variables 
    returns a dict called student
    """
    student = {
            'firstName' : '',
            'lastName' : '',
            'id' : '',
            'dept' : '',
            'gpa' : 0.0,
            'status' : '',
            'dateOfGrad' : ''
        }
        
    try:
        (firstName, lastName, id, dept, gpa, status, dateOfGrad) = line.split()
        student['firstName'] = firstName
        student['lastName'] = lastName
        student['id'] = id
        student['dept'] = dept
        student['gpa'] = float(gpa)
        student['status'] = status
        student['dateOfGrad'] = dateOfGrad
    
    except ValueError:
        (firstName, lastName, id, dept, gpa, status) = line.split()
        student['firstName'] = firstName
        student['lastName'] = lastName
        student['id'] = id
        student['dept'] = dept
        student['gpa'] = float(gpa)
        student['status'] = status
    
    return student
    
def readFromFile(filename):
    """ Read from filename, return the data as a dict """
    
    listOfStudents = []
    
    while True:
        try:
            with open(filename, 'r') as f:
                for line in f:
                    listOfStudents.append(unpack(line))
            
            print(f"Success opening {filename}")
            print(f"Total amount of students: {len(listOfStudents)}")
            print("")
            return listOfStudents
            
        except FileNotFoundError:
            filename = input(f"The file {filename} could not be found. "
                "Please make sure it is exists within the project folder: ")
                