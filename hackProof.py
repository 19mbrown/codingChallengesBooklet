import getpass
from pathlib import Path

x = 0
while x < 2:
    print("What's you ", end="")
    password = getpass.getpass()

    print("Re-enter your ", end="")
    passCheck = getpass.getpass()
    if passCheck == password:
        break
    else:
        print("Passwords not matching! ")

while not getpass.getpass() == info.password:
    print("WRONG PASSWORD! \nTry again")
print(open(f"{Path.home()}/example.txt", "r"))
