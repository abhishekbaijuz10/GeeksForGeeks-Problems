start = int(input("Enter the starting point"))
stop = int(input("Enter the stopping point"))
for i in range(start, stop + 1):
    if i % 2 == 0:
        print(i)