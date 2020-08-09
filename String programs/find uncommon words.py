def uncommmon(a, b):
    a = A.split()
    b = B.split()

    uc = ''
    for i in a:
        if i not in b:
            uc = uc + " " + i
    for j in b:
        if j not in a:
            uc = uc + ' ' + j

    return uc


A = "apple banana mango"
B = "banana fruits mango"
print(uncommmon(A, B))
