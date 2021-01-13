#!/usr/bin/python3
from sys import argv
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
elif argv[1].isdigit() is False:
    print("N must be a number")
    exit(1)
elif int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
else:
    num = 2
    for j in range(int(argv[1]) - 2):
        L = []
        k = j + 1
        m = 0
        for i in range(int(argv[1])):
            if m != 0:
                k = k + num
            if k < int(argv[1]):
                L.append([i, k])
            elif k == int(argv[1]):
                L.append([i, 0])
            elif k >= int(argv[1]):
                k = k - 1 - int(argv[1])
                L.append([i, k])
            m += 1
        num += 1
        print(L)

            
