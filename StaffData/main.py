from staff import Staff
import gen_staff_data as gen
import prcss_staff_data as prcss

list_of_staff = []

for i in range(1, 1001):
    list_of_staff.append(gen.generateStaffData())

#print(list_of_staff[0].getAllFormatted())

gen.outputStaffData(list_of_staff)