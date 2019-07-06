#!/usr/bin/env python3
import cgi

print("Content-Type: text/plain")
print("")

form = cgi.FieldStorage()
stringval = form.getvalue('a', None)
listval = form.getlist('b')

print("a: {}, b: {}".format(str(stringval), str(listval)))

# http://localhost:8000/cgi-bin/field_storage.py?a=45&b=45&b=56
