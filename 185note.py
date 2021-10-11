import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employees"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
#for row in data:
#print('Employee no:',row[0])
#print('Employee name:',row[1])
#print('Employee salary:',row[2])
#print('Employee address:',row[3])
#print()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()