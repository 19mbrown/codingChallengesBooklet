import re

string = input("Enter a string: ")
regex = input("Enter a regex pattern: ")
print(re.search(regex, string))
