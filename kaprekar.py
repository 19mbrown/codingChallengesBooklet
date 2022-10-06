def kaprekar(a):
    check = list(str(a**2))
    kaprekar = 0
    for i in check:
        kaprekar += int(i)
    if int(kaprekar) == a:
        return True
    else:
        return False

print(kaprekar(9))
