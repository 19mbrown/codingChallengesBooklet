def roman(a):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    romInt = str()
    i = int()
    while (a > 0):
        for _ in range(a // val[i]):
            romInt += syb[i]
            num -= val[i]
        i+=1
    return romInt
