def readFromFile(filename):
    data = []
    while True:
        try:
            with open(filename) as inFile:
                for line in inFile:
                    data.append(line)
            return data
            
        except FileNotFoundError:
            filename = input(f"The file {filename} could not be found. "
                "Please make sure it is exists within the project folder: ")
            
def display(contents):
    #print(contents.strip())
    print(contents)