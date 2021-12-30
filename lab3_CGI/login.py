#!/usr/bin/env python3
import os
import cgi, cgitb
import secret

from http.cookies import SimpleCookie
from templates import secret_page, after_login_incorrect, login_page

# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = cookie.get("UserID").value if cookie.get("UserID") else None
cookie_password = cookie.get("Password").value if cookie.get("Password") else None

if cookie_username:
    username = cookie_username
if cookie_password:
    password = cookie_password

if (not username and not password):
    print(login_page())
elif(username == secret.username and password == secret.password):
    print(f"Set-Cookie:UserID = {username}")
    print(f"Set-Cookie:Password = {password}")
    print(secret_page(username, password))
else:
    print(after_login_incorrect())

