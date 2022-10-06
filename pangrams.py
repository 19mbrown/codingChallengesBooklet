import string

def pangrams(a):
    a = a.lower()
    for i in string.ascii_lowercase:
        if i in a:
            x = True
        else:
            x = False
            break
    return x

print(pangrams("The quick brown fox jumps over the lazy dog"))
