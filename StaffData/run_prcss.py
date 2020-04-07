""" this file calls the functions in the prcss_staff_data file """
from staff import Staff
import prcss_staff_data as prcss

list_of_staff = prcss.loadData()

prcss.formatDate(list_of_staff)
prcss.calculateSalary(list_of_staff)

prcss.writeData(list_of_staff)