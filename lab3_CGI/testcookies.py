#!/usr/bin/env python3
import os

def test_cookies():
    print("Set-Cookie:UserID = XYZ;\r\n")
    print("Set-Cookie:Password = XYZ123;\r\n")
    print("Set-Cookie:Expires = Friday, 10-Dec-2021 23:59:59 GMT;\r\n")
    print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>COOKIES SET - First CGI Program</title>")
    print("</head>")
    print("<body>")
    print("<h2>All Done!<h2>")
    print("</body>")
    print("</html>")
    param = "HTTP_COOKIE"
    print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

test_cookies()
param = "HTTP_COOKIE"
print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

