import cx_Oracle
try:
    con=cx_Oracle.connect('scott/tiger@localhost')
    cursor=con.cursor()
    while True:
        eno=int(input('Enter employee no:'))
        ename = input('Enter employee name:')
        esal = float(input('Enter employee salary:'))
        eaddr = input('Enter employee address:')
        query="inser into employees values(%d,'%s',%f,'%s')"
        cursor.execute(query%(eno,ename,esal,eaddr))
        con.commit()
        print('Recorded successfully')
        option=input('Do you want to insert 1 more record[Yes|No]:')
        if option=='No':
            break
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print('There is a problem:',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()