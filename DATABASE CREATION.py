def Create_Database_Bus():
    import mysql.connector
    mycon = mysql.connector.connect(
        host='localhost', user='root', passwd='')
    cursor = mycon.cursor()
    mycon.autocommit = True
    s1 = "CREATE DATABASE IF NOT EXISTS Bus"
    cursor.execute(s1)


Create_Database_Bus()
