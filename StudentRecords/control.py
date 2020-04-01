def unpack(line):
    """ Unpack the information from the line into seperate variables """
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
    """ Read from filename, return the data """
    
    listOfStudents = []
    
    while True:
        try:
            with open(filename, 'r') as f:
                for line in f:
                    listOfStudents.append(unpack(line))
            
            print(f"Success opening {filename}")
            print(f"Total amount of students: {len(listOfStudents)}")
            return listOfStudents
            
        except FileNotFoundError:
            filename = input(f"The file {filename} could not be found. "
                "Please make sure it is exists within the project folder: ")
    
def display(data):
    """ Print out data in neat format """
    
    for line in data:
        print(f"{line['firstName'].ljust(9, ' ')} {line['lastName'].ljust(15, ' ')} {line['id'].ljust(15, ' ')} {line['dept'].ljust(10, ' ')} {line['gpa']} {line['status'].rjust(7, ' ')} {line['dateOfGrad'].rjust(15, ' ')}")