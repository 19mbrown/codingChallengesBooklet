number = input("Enter a symbol and number: ")
number = number.split(" ")


print(number[0], "|", end="")
for i in range(int(number[1]) + 1):
    print(str(i).ljust(6), end="")

for i in range(int(number[1]) + 1):
    if number[0] == "/" and i == 0:
        i
    else: 
        print(i, "|", end="")
        for j in range(int(number[1]) + 1):
            match number[0]:
                case "+":
                    print(str(i + j).ljust(6), end="")
                case "-":
                    print(str(i - j).ljust(6), end="")
                case "*":
                    print(str(i * j).ljust(6), end="")
                case "/":
                    if i == 0 or j == 0:
                        i
                    else:
                        if str(i / j).isdigit():
                            print(str(i / j, 3).lstrip("0").ljust(6), end="")
                        else:
                            print(str(round(i / j, 3)).ljust(6), end="")
    print("\n", end="")
