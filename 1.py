n = 116

bn = bin(n).replace('0b', '')
l = len(bn)
center = l // 2

if len(bn) % 2 == 0:
    r = bn[:center - 1] + bn[center + 1:]
else:
    r = bn[:center] + bn[center + 1:]

res = int(r, 2)
print(res)