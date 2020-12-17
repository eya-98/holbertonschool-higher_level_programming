#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or type(roman_string) != str:
        return 0
    else:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(roman_string)):
            if (i != (len(roman_string) - 1) and
                roman[roman_string[i]] < roman[roman_string[i + 1]]):
                num -= roman[roman_string[i]]
            else:
                num += roman[roman_string[i]]
            return num
