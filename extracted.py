import json

# some JSON:
x = """ 


[{ "price": " 40.50 ",    "qty": "   1  ",  "desc": "  Arm Rest  ",  "code": " 234  "      }]


"""

# parse x:
y = json.loads(x)


# the result is a Python dictionary:
print(type(y))

print(y[0])

totalQty = 0
buffer = ''
for oneRecord in y:
    print(oneRecord)
    buffer += str(oneRecord)
    
    totalQty += float(oneRecord['qty'])
    
print("total qty is: " +str(totalQty))