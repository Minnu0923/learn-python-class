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
                CREATE TABLE employee(
                eid int,
                ename VARCHAR(32),
                esal  float);
'''
    cursor.execute(sql_st)
    dbcon.commit()
    print('table created successfully')
except mysql.connector.Error as err:
    print(err)
