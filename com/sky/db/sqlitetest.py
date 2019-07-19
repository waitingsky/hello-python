import sqlite3

# 建表
def createTable(conn):
    c = conn.cursor()
    
    c.execute('drop table if exists COMPANY');
    c.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    print ("Table created successfully");
    c.close()

# 插入
def insertDatas(conn):
    c = conn.cursor()
    
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    print("Records created successfully");
    c.close()

# 查询
def selectDatas(conn):
    c = conn.cursor()

    cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print( "ID = ", row[0])
        print( "NAME = ", row[1])
        print( "ADDRESS = ", row[2])
        print( "SALARY = ", row[3], "\n")

    print("Operation done successfully");
    c.close()

# 更新
def updateDatas(conn):
    c = conn.cursor()

    c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)

    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print ("ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ADDRESS = ", row[2])
        print ("SALARY = ", row[3], "\n")

        print ("Operation done successfully");
    c.close()

# 删除
def deleteDatas(conn):
    c = conn.cursor()
   
    c.execute("DELETE from COMPANY where ID=2;")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    
    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    
    print("Operation done successfully");
    c.close()


# 执行
conn = sqlite3.connect('helloworld.db')
print("Opened database successfully");

createTable(conn)

insertDatas(conn)

selectDatas(conn)

updateDatas(conn)

deleteDatas(conn)

conn.commit()
conn.close()



