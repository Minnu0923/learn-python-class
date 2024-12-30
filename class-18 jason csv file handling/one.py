import json
fp=open('employees.json', 'r')
employees=json.load(fp)
print(type(employees))
print(len(employees))
print(employees)
