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
<title>Cart</title>
</head>
<body>
 <hr>
""")

msgList=sp.finish()

if sp.finish():
    for (total) in msgList:
        print(f"結帳完成，共{total}元")
else:
    print("結帳失敗")
print("<br><a href='cart.py'>回上頁</a>")
print("</body></html>")
