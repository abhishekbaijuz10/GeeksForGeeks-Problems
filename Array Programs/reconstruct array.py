def construct(n, m, a):
    ind = 0

    for i in range(n):
        if a[i] == -1:
            a[i] = a[i]=(a[i + 1]-1 + m)% m


n, m = 6, 7
a =[5, -1, -1, 1, 2, 3]
print(construct(n, m, a))
print(*a)