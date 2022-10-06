for i in range(0, 2012):
    i = list(str(i))
    for j in i:
        if i.count(j) > 1:
            print("".join(i))
            break
