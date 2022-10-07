x = sorted([1,2,3,4,5,6,7,8,9,10])
print(x)
new = []
for i in x:
    if i % 2 == 0:
        x.remove(i)
        new.append(i)
for i in sorted(new):
    x.append(i)
print(x)
