import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    query="select * from employees"
    cursor.execute(query)
    row=cursor.fetchone()
    while row is not None:
        print(row)
        row=cursor.fetchone()
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()