import re

foo = "1×£1 + 2×50p + 2×20p + 1×5p + 1×2p + 3×1p".split(" + ")
out = int()

for i in foo:
    tmp = i.replace("p", "").replace("£", "100*").replace("×", "*")
    out += eval(tmp)

if int(out) == 250: print("Can make £2.50")
else: print("Can't make £2.50")
