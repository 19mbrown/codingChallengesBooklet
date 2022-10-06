def VAT():
    price = float(input("What's the price? "))
    rate = 1 + (float(input("What percent vat? ")) / 100)
    return price * rate

def timesTables():
    x = int(input("Enter a number: "))
    a = int(input("What do you want to times it by? "))
    return x * a

def TAX():
    money = int(input("How much do you make a year? £"))
    if money <= 12570:
        return money
    elif money <= 50270:
        return money * 1.2
    elif money <= 150000:
        return money * 1.4
    elif money > 150000:
        return money * 1.45
    else:
        print("ERROR")

match input("What calculator do you want? (Tax/Times Tables/VAT) ").lower():
    case "vat":
        print(VAT())
    case "times tables":
        print(timesTables())
    case "tax":
        print(TAX())
