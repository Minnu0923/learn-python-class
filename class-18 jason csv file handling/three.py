#read employees.csv file and print only bangalore employees

import csv
fp1=open('task2.csv', 'r')
csv_data = csv.reader(fp1)
employees= (list(csv_data))

for emp_list in employees:
    if emp_list[3] == "Bangalore":
        print(emp_list [1])

fp1.close()