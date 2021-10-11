import cx_Oracle
try:
    query="insert into employees values(100,'durga',1000,'hyd')"
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print('Recorded successfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
