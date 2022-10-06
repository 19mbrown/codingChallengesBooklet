new = {0: 0, 1: 1}
for i in range(2, int(input("How many places do you want? "))):
    new[i] = new[i - 1] + new[i-2]
    print(new[i])
