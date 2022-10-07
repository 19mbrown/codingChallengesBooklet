x = list(input("Enter a string:\n"))

z = str()

for i in x:
    y = ord(i)
    y += 25
    y = chr(y)
    z += y
print(z)
