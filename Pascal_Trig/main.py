"""
Assignment:
    Prompt the user for a positive integer, n.  n > 0. Check for user errors
    (e.g, entering a character instead of a number)
    The user should, however, be allowed to enter "q" and bypass the program.
    Write a recursive program which returns the nth row of Pascal's triangle.
    Examples:
    n = 1, return 1
    n = 2, return [1, 1]
    n = 5, return [1, 4, 6, 4, 1]
"""

# prompt the user for the generation, validate their input
def UserInput():

    while True:
        usr = input("Please enter a positive number: ")
        try:
            usr = int(usr)
            if usr > 0:
                return usr
        except ValueError:
            if usr == 'q':
                return usr

# generate Pascal triangle, will need the iteration, the user defined limit('n')
# and the current line (which is a list)
def Generate(itr, n, line):
    #print(f"iteration {itr}, line length: {len(line)}")
    #print(line)
    # assign the first value of line to the new line
    new_line = [line[0]]
    # while the iteration is less than the user defined limit ('n')
    while itr < n:
        # go through the entire rest of the line
        for i in range(len(line)):
            # i is at the end of the line, assign the value
            if i == len(line) - 1:
                new_line.append(line[i])
            # middle values need to be calculated
            else:
                new_line.append(line[i] + line[i+1])

        # increase the iteration by 1
        itr += 1
        # if the iteration has reached the user defined limit, then return
        # the new_line we generated
        if itr == n:
            return new_line
        else:
            # call Generate to get the next line
            # catch the return line when exiting the recursion
            new_line = Generate(itr, n, new_line)
            # break out of the loop
            break

    # after breaking out of the loop, return the line that was caught
    return new_line

# start at the 1st iteration
itr = 1
n = UserInput()
if n != 'q':
    line = [1]
    end = Generate(itr, n, line)
    print(end)
else:
    print("Exiting program...")
