import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employees"
    cursor.execute(query)
    n=int(input('Enter no. of required rows:'))
    data=cursor.fetchmany()
    f=open('dbresults.txt','w')
    f.write(str(data))
    for row in data:
         print('Employee no:',row[0])
         print('Employee name:',row[1])
         print('Employee salary:',row[2])
         print('Employee address:',row[3])
         print()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()