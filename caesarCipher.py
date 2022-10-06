import string

key = int(input("What's the key? "))
input = input("Enter a string: ").lower()


def rotate(l, n):
    return l[n:] + l[:n]

letters = string.ascii_lowercase
lettersShift = rotate(letters, int(key))

newList = list()

for i in list(input):
    newList.append(lettersShift[letters.index(i)])
print("".join(newList))
