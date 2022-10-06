def checkLuhn(x):
    nDigits = len(x)
    sum = 0
    parity = (nDigits-2) % 2 
    
    for i in range(0, nDigits -1):
        digit = integer(x[i])
        if i % 2 == parity:
            digit = digit * 2 
        if digit > 9:
            digit = digit - 9 
        sum += digit 
    return 10 - (sum % 10) == x % 10 
