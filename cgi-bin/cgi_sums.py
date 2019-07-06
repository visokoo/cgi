#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()
operands = form.getlist('operand')

print("Content-Type: text/plain")
print("")

if operands:
    sum = 0
    for operand in operands:
        sum += int(operand)
    print(sum)
else:
    print("No total calculated as no operands are provided.")
