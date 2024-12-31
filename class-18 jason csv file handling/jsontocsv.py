#convert json file to csv
#Read employees.csv file,
#and write data into new json file ie emp.json
import csv
import json

fp1 = open ('employees.json', 'r')
fp2 = open ('emp2.csv', 'w', newline= "")
employees= json.load(fp1) #python data
employees_list=[]
 
for emp in employees:
    employees_list.append([emp['eid'],emp['ename'],emp['gender']])
#print(employees_list)

csvwrite=csv.writer(fp2)
csvwrite.writerow(['eid','ename','gender'])
csvwrite.writerows(employees_list)











fp1.close()
fp2.close()