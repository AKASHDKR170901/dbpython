import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
if con!=None:
    print('Connection established successfully')
    print('Version:',con.version)
else:
    print('Connection not established')
con.close()
