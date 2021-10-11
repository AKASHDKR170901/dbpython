import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    increment=float(input('Enter increment salary:'))
    salrange=float(input('Enter salary range:'))
    query="update employees set esal=esal+%f where esal<%f"
    cursor.execute(query%(increment,salrange))
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