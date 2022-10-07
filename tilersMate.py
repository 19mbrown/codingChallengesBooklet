width = int(input("What's the width? "))
length = int(input("What's the length? "))
ratePerM2 = float(input("What's the rate per m^2? "))
print("£{:.2f}".format((width * length) * ratePerM2))
