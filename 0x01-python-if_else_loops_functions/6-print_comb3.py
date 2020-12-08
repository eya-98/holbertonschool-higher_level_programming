#!/usr/bin/python3
for c in range (0, 10):
    for d in range(c + 1, 10):
        if c < 8 and d < 9:
            print("{:d}{:d},".format(c, d), end=" ")
        elif c == 8 and d == 9:
            print("{:d}{:d}".format(c, d))
