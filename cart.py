#!C:\python\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import shop1 as sp

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Guestbook: ListMsg</title>
</head>
<body>
管理端 <a href='listshop.py'> 管理端 </a><hr>
 <a href='listcart.py'> 購物車 </a><hr>

<br>
<form method="post" action="buy.py">
輸入要購買的商品: <input type='text' name='i'>輸入數量<input type='text' name='j'><input type='submit'>
</form>
<form method="post" action="returnS.py">
輸入要退貨的商品: <input type='text' name='i'>輸入數量<input type='text' name='j'><input type='submit'>
</form>
<a href='finish.py'>結帳</a>
 <hr>
""")

msgList=sp.listshop()

for (ID,Name,number,Price) in msgList:
	print(f"<p>編號{ID}: 商品名:{Name} 庫存:{number} 價格:{Price}</p>")

print("</body></html>")

