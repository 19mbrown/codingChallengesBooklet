x = int(input("Enter an integer: "))
fizz = int(input("Fizz: "))
buzz = int(input("Buzz: "))

def isprime(num):
    for n in range(2,int(num**0.5)+1): 
        if num%n==0: return False
    return True

for i in range(1, x):
    x = False
    if i % fizz == 0 and not i % buzz == 0:
        print("Fizz")
        x = True
    if i % fizz == 0 and not i % buzz == 0:
        print("Buzz")
        x = True
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz")
        x = True
    if isprime(i):
        print("OOPS")
        x = True
    if not x:
        print(i)

