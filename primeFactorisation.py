n = input("Enter a number: ")
primfac = []
d = 2
while d*d <= n:
    while (n % d) == 0:
        primfac.append(d)
        n //= d
    d += 1
if n > 1:
    primfac.append(n)
print(primfac)
