x = list()
for i in range(3):
    x.append(int(input("Enter a number: ")))

if input("Do you want to reverse the list? (y/n)") == "y":
    print((sorted(x)[::-1]))
else:
    print(sorted(x))
