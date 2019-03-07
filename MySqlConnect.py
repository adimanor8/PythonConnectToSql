import  pymysql
conn=pymysql.connect(host='localhost',port= 3306,user='root',password='D@arrow2vfkva,bv2',db='app2', autocommit=True)
Cursor=conn.cursor()
Cursor.execute("insert into dogs2 values('b1','6','b3')")
Cursor.execute("show tables")
Cursor.execute("select namedog from dogs2")
Cursor.execute("DELETE from dogs2 where namedog='b1'")
Cursor.execute("select * from dogs2")
for row in Cursor:
    print(row)
