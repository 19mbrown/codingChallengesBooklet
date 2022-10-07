string1 = "Hello"
string2 = "New"
asciiString1 = [ord(c) for c in string1]
asciiString2 = [ord(c) for c in string2]
for i in range(max([len(asciiString1), len(asciiString2)])):
    try:
        j = asciiString1[i]
        k = asciiString2[i]
        print(j - k)
    except IndexError:
        break
