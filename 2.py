l = []

for n in range(1, 1000):
    bn = bin(n).replace('0b', '')
    bn = bn[::-1]
    bn = bn + bn[-1]
    r = int(bn, 2)
    if r > 99:
        l.append(n)

print(min(l))