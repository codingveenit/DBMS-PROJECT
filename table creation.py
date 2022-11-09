def table_creation_Bus():
    import mysql.connector
    mycon = mysql.connector.connect(
        host='localhost', user='root', passwd='', database='Bus')

    cursor = mycon.cursor()
    mycon.autocommit = True

    s1 = "create table Bus(name varchar(100),phno varchar(15)  primary key,age int(4),gender varchar(50),from_f varchar(100),to_t varchar(100),date_d varchar(20))"
    cursor.execute(s1)


table_creation_Bus()


def table_creation_user_accounts():
    import mysql.connector
    mycon = mysql.connector.connect(
        host='localhost', user='root', passwd='', database='Bus')

    cursor = mycon.cursor()
    mycon.autocommit = True

    s1 = "create table user_accounts(fname varchar(100),lname varchar(100),user_name varchar(100) ,password varchar(100) primary key, phno varchar(15),gender varchar(50),dob varchar(50),age varchar(4))"
    cursor.execute(s1)


table_creation_user_accounts()
