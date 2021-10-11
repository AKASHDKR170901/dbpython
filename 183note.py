import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    cotoff=float(input('Enter cutoff salary:'))
    query="delete from employees where esal>%f"
    cursor.execute(query%cutoff)
    con.commit()
    print('Deleted successfully')
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()