i = input("Enter a string:\n")

print(i[::-1])
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z", "W", "Y"]

countVowels = int()
for x in vowels:
    countVowels += i.lower().count(x)

countConsonants = int()
for x in consonants:
    countConsonants += i.upper().count(x)
print("Vowels: ", countVowels)
print("Consonants: ", countConsonants)
