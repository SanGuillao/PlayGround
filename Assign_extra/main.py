"""
Write a program that does the following:
    1. Has a funct that receives a list of input string from the user
    2. Calls another funct which tests whether each input sting is a valid
       email address
    3. Program prints whether each string is valid or invalid
    4. Rules:
        a. It must have username@website.extension format
        b. The username can only include letters, digits, dashes and
           underscores
        c. The website name can only have letters and digits
        d. The extension can only contain letters
        e. Max length of extension is 3
    Hint: Use find(), isalnum(), isalpha()
"""

# ask for user input, return the list of strings
def userInput():
    userList = []
    while True:
        str = input("Please enter email address or q to quit: ")
        if str == 'q':
            break
        else:
            userList.append(str)

    return userList

# check if user string is valid, return True if valid
# use find(), isalnum(), and isalpha()
def isValid(str):
    # find the location of the first split
    loc1 = str.find('@')
    username = str[:loc1]
    # brute force check the username, see if it follows the rules
    for i in username:
        if i.isalnum() == False:
            if i != '-' and i != '_':
                return False

    # find the location of the second split
    loc2 = str.find('.')
    website = str[loc1 + 1 : loc2]
    # check if website follows the rules
    if website.isalnum() == False:
        # print(website)
        return False

    # from the second split to the end, grab extension
    extension = str[loc2 + 1 :]
    # check to see if extension follows rules
    if extension.isalpha() == False:
        return False
    if len(extension) > 3:
        return False

    # if all rules were followed, return valid (True)
    return True

# format the output, return a print
def outPut(str):
    if isValid(str):
        return f"{str} is a valid email address"
    else:
        return f"{str} is not a valid email address"

# main part of the Program
# begin asking for user input
listStr = userInput()
# output if emails entered are valid/invalid
for str in listStr:
    print(outPut(str))
