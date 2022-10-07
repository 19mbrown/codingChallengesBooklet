x = int(input("Enter an integer: "))

for i in range(1, x):
    x = False
    if i % 3 == 0 and not i % 5 == 0:
        print("Fizz")
        x = True
    if i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
        x = True
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        x = True
    if not x:
        print(i)
