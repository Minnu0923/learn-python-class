#example-writerow
import csv
fp = open('emp.csv','w', newline ="")
csvwriter=csv.writer(fp);
emp_list=[[1, 'Rahul', 5000],[2, 'Sonia',10000]]
csvwriter.writerow(['eid','ename','salary'])
csvwriter.writerow(emp_list)

fp.close()