#!/usr/bin/env python3
import os, json
print("Content-type:text/html\r\n\r\n")

print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

# Q1
json_object = json.dumps(dict(os.environ), indent = 4)
print(json_object)

# Q2
param = "QUERY_STRING"
print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

# Q3
param = "HTTP_USER_AGENT"
print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))