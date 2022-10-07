bet = int(input("Pick a number (1-30) "))
money = float(input("How much money do you want to put on this? "))

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

if bet % 2 == 0:
    money *= 2
if money % 10 == 0:
    money *= 3
if isprime(money):
    money *= 5
if money < 5:
    money *= 2

print("£{:0.2f}".format(money))
