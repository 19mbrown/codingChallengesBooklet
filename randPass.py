import string
import secrets
from pathlib import Path
import os

choices = string.ascii_letters + string.digits + string.punctuation

x = str()
for _ in range(20):
    x += secrets.choice(choices)
print(x)

userName = input("What's your username? ")

location = f"{Path.home()}/.pass.txt"
print(location)
if not os.path.exists(location):
    os.mknod(location)
    os.chmod(location, 0o200)
with open(location, mode="a") as file:
    file.write("Username: " + userName + "\n")
    file.write("Password: " + str(passwd) + "\n\n")
