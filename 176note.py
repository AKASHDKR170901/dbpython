import cx_Oracle
try:
    query="Create table employees(eno number,ename varchar 2(10),esal number(10.2),eaddr varchar 2(10))"
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    print('Table created successfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
