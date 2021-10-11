import cx_Oracle
try:
    query="insert into employees values(:eno,:ename,:esal,:eaddr)"
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    records=[(200,'sunny',2000,'Mumbai'),(300,'Bunny',3000,'Goa'),(400,'Munny',4000,'Hyd')]
    cursor.executemany(query,records)
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