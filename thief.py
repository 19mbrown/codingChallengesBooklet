#!/usr/bin/python3
pinN = list(str(1234))

for i in pinN:
    for k in pinN:
        for j in pinN:
            for l in pinN:
                x = [i,k,j,l]
                if not (x.count(i) > 1 or x.count(k) > 1 or x.count(j) > 1 or x.count(l) > 1):
                    print(i, k, j, l)
