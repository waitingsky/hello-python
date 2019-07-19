import mysql.connector
 
# 查询版本 
def selectVersion(mydb):
    mycursor = mydb.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    mycursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取单条数据.
    data = mycursor.fetchone()

    print ("Database version : %s " % data)
    
    mycursor.close()

# 建表
def createTable(mydb):
    mycursor = mydb.cursor()
     
    sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
    mycursor.execute(sql)
    mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
    
    mycursor.close()

# 插入
def insertDatas(mydb): 
    mycursor = mydb.cursor()
     
    print("插入单行数据")
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = ("RUNOOB", "https://www.runoob.com")
    mycursor.execute(sql, val)
     
    mydb.commit()    # 数据表内容有更新，必须使用到该语句
     
    print(mycursor.rowcount, "记录插入成功。")

    print("插入多行数据")
    sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val = [
      ('Google', 'https://www.google.com'),
      ('Github', 'https://www.github.com'),
      ('Taobao', 'https://www.taobao.com'),
      ('stackoverflow', 'https://www.stackoverflow.com/')
    ]
    mycursor.executemany(sql, val)
     
    mydb.commit()    # 数据表内容有更新，必须使用到该语句
     
    print(mycursor.rowcount, "记录插入成功。")
    
# 查询
def selectDatas(mydb): 
    mycursor = mydb.cursor()
     
    print("查询全部数据")
    mycursor.execute("SELECT * FROM sites")
     
    myresult = mycursor.fetchall()     # fetchall() 获取所有记录
     
    for x in myresult:
        print(x)
        
    print("过滤查询 RUNOOB")
     
    sql = "SELECT * FROM sites WHERE name ='RUNOOB'"
 
    mycursor.execute(sql)
 
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print("%s 占位符来转义查询的条件");
    sql = "SELECT * FROM sites WHERE name = %s"
    na = ("RUNOOB", )
     
    mycursor.execute(sql, na)
     
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
  
  
# 查询 分页
def selectDatasByPage(mydb):

    # 读取前 3 条记录：
    mycursor = mydb.cursor()
 
    print("读取前 3 条记录")
    mycursor.execute("SELECT * FROM sites LIMIT 3")
 
    myresult = mycursor.fetchall()
 
    for x in myresult:
        print(x)

    # 从第二条开始读取前 3 条记录：
    print("从第二条开始读取前 3 条记录")
    mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推
 
    myresult = mycursor.fetchall()
 
    for x in myresult:
        print(x)

# 更新
def updateDatas(mydb):
    mycursor = mydb.cursor()
 
    print("占位符插入")
    sql = "UPDATE sites SET name = %s WHERE name = %s"
    val = ("Zhihu", "ZH")
     
    mycursor.execute(sql, val)
    mydb.commit()
     
    print(mycursor.rowcount, " 条记录被修改")
     
    print("sql拼接插入")

    sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"
    mycursor.execute(sql)
    mydb.commit()
     
    print(mycursor.rowcount, " 条记录被修改")

# 删除
def deleteDatas(mydb):     
    mycursor = mydb.cursor()
 
    print("占位符删除") 
    sql = "DELETE FROM sites WHERE name = %s"
    na = ("stackoverflow", )
     
    mycursor.execute(sql, na)
     
    mydb.commit()
     
    print(mycursor.rowcount, " 条记录删除")

    print("sql拼接删除")
    sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
     
    mycursor.execute(sql)
    mydb.commit()
     
    print(mycursor.rowcount, " 条记录删除")
    
# 执行
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="testsdic"
)

selectVersion(mydb)

createTable(mydb)

insertDatas(mydb)

selectDatas(mydb)

selectDatasByPage(mydb)

updateDatas(mydb)

deleteDatas(mydb)

mydb.close()    
