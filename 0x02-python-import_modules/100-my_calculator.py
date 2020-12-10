#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    j = 0
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    str = {"+", "-", "*", "/"}
    for i in str:
        if argv[2] == i:
            j = j + 1
    if j == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == "+":
        print("{} + {} ".format(argv[1], argv[3]), end="")
        print("= {}".format(add(int(argv[1]), int(argv[3]))))
    elif argv[2] == "-":
        print("{} - {} ".format(argv[1], argv[3]), end="")
        print("= {}".format(sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == "*":
        print("{} + {} ".format(argv[1], argv[3]), end="")
        print("= {}".format(mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == "/":
        print("{} + {} ".format(argv[1], argv[3]), end="")
        print("= {}".format(div(int(argv[1]), int(argv[3]))))
