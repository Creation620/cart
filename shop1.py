#連線DB
from dbConfig import conn, cur
def listshop():
    #查詢
    sql="SELECT * FROM `商城` WHERE 1 "
    cur.execute(sql)
    records = cur.fetchall()
    return records

def delshop(ID):
    sql="delete from `商城` where ID=%s;"
    cur.execute(sql,(ID,))
    conn.commit()
    return True

def likeMsg(id,vipNumber=0):
    if vipNumber>0:
        sql="update guestbook set likes=likes+100 where id=%s;"
        
    else:
        sql="update guestbook set likes=likes+1 where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def addNew(Name,number,Price):
    sql="insert into `商城` (Name,number,Price) values (%s,%s,%s);"
    cur.execute(sql,(Name,number,Price))
    conn.commit()
    return True

def A(ID,number):
    sql="update `商城` SET number=number+%s where ID=%s;"
    cur.execute(sql,(number,ID))
    conn.commit()
    return True

#client

def listcart():
    #查詢
    sql="SELECT * FROM `cart` WHERE 1 "
    cur.execute(sql)
    records = cur.fetchall()
    return records
 
def buy(ID,number):
    sql="INSERT INTO `cart`(`ID`, `Name`, `price`) select `ID`, `Name`, `Price` from `商城` where ID = %s;"
    cur.execute(sql,(ID,))
    conn.commit()
    
    sql="UPDATE `cart` SET `buy`=buy+%s WHERE `ID`=%s"
    cur.execute(sql,(number,ID))
    conn.commit()
    
    sql="UPDATE `商城` SET `number`=number-%s WHERE `ID`=%s"
    cur.execute(sql,(number,ID))
    conn.commit()
    return True
    
def returnS(ID,number):
    sql="UPDATE `商城` SET `number`=number+%s WHERE `ID`=%s;"
    cur.execute(sql,(number,ID))
    conn.commit()
    
    sql="UPDATE `cart` SET `buy`=buy-%s WHERE `ID`=%s;"
    cur.execute(sql,(number,ID))
    conn.commit()
    
    sql="delete from cart where buy <= 0;"
    cur.execute(sql)
    conn.commit()
    return True

def finish():
    sql="select sum(buy*price) as total from cart where buy>0;"
    cur.execute(sql)
    records = cur.fetchone()
    
    sql="Truncate Table cart;"
    cur.execute(sql)
    conn.commit()
    return records
    