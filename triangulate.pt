a = int(input("What size is the first side? "))
b = int(input("What size is the second side? "))
c = int(input("What size is the third side? "))


if (a + b > c) and (a + c > b) and (b + c > a):
    print("This is a triagle! ")
    for i in [a,b,c]:
        if [a,b,c].count(i) == 2:
            print("This is an isosceles triagle.")
            break
        if [a,b,c].count(i) == 3:
            print("This is an equilateral triangle.")
    x = sorted([a,b,c])
    if (x[0] ** 2) + (x[1] ** 2) == (x[2] ** 2):
        print("This is a right angled triangle.")
        
else:
    print("This is not a triangle.")
