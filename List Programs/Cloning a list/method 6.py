def cloning(ls):
    lc = []
    for item in ls: lc.append(item)
    return lc


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)

print(li1)
print(li2)
