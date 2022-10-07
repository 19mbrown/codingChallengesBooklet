week1 = ["carrots", "milk", "meat"]
week2 = ["milk", "crisps"]

for i in week1:
    if not (i in week2):
        print(i)
for i in week2:
    if not (i in week1):
        print(i)
