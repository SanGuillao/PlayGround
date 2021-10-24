"""
Create a program that does the following:
Receives an odd-numbered integer, n,  input from the user
    (process to receive and validate the user input: 10 points)
Creates a numpy nxn array (10 pts)
Initiates the value of the numpy array to zero (10 points)
Initiate the middle position of the array to 1 (5 points)
The program has a base case (15 points)
Than creates a clockwise spiral from the center of the array (50 points):
The space immediately to the right of the middle position (if n > 1) should be 2
The space underneath 2 should be 3, etc.
Examples:
Example: 3x3
7    8    9
6    1    2
5    4    3
Example: 5x5
21	22	23	24	25
20	7	8	9	10
19	6	1	2	11
18	5	4	3	12
17	16	15	14	13
"""

# import numpy
import numpy as np

# define a func that will ask for user input and verify that is odd
def UserInput():
    while True:
        try:
            usr = int(input("Please enter an odd number: "))
            if usr % 2 != 0:
                break
        except ValueError:
            print("Error, input must be a number")

    return usr

# define a func that will create clockwise spiral from the center of array
def Spiral(arr, size):
    # start the index at right of middle
    row = int(size / 2)
    col = row
    hop_y = 1
    hop_x = 1
    # start the value at 2
    value = 2
    #arr[row][col] = value

    while True:
        try:
            # hop right
            for i in range(hop_y):
                col += 1
                arr[row][col] = value
                value += 1

            # hop down
            for i in range(hop_x):
                row += 1
                arr[row][col] = value
                value += 1

            # increment hop values
            hop_y += 1
            hop_x += 1

            # hop left
            for i in range(hop_y):
                col -= 1
                arr[row][col] = value
                value += 1

            # hop up
            for i in range(hop_x):
                row -= 1
                arr[row][col] = value
                value += 1

            # increment hop values
            hop_y += 1
            hop_x += 1
            
        except IndexError:
            break
# get user input
n = UserInput()

# create array using user input as size
# zeros((r,c)) will return an array with 0s, the size of r and c
arr = np.zeros((n,n), dtype = np.int64)
mid = int(n / 2)
arr[mid][mid] = 1
Spiral(arr, n)
print(arr)
