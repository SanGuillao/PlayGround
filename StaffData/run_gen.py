""" this file calls the functions in the gen_staff_data file """
from staff import Staff
import gen_staff_data as gen

list_of_staff = []

# generate 1000 lines of staff data
for i in range(1, 1001):
    list_of_staff.append(gen.generateStaffData())

# output the list of staff to an output file
gen.outputStaffData(list_of_staff)