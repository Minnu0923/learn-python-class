#Insert
import mysql.connector
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='jandb',
                                  auth_plugin='mysql_native_password'
                                )
    cursor=dbcon.cursor()
    sql_st='''
                select * from employee;
'''
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    for emp in employees:
        print("employee ID", emp [0], "employee name", emp[1])
    print(employees)
    
    print('Fetched successfully')
except mysql.connector.Error as err:
    print(err)
