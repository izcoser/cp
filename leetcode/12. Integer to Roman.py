# https://leetcode.com/problems/integer-to-roman/

def symbol_of_maximal_value_to_subtract(n: int) -> str:
    if n >= 1000:
        return "M", n - 1000
    if n >= 500:
        return "D", n - 500
    if n >= 100:
        return "C", n - 100
    if n >= 50:
        return "L", n - 50
    if n >= 10:
        return "X", n - 10
    if n >= 5:
        return "V", n - 5
    if n >= 1:
        return "I", n - 1

def decimal_place_to_roman(n: int) -> str:
    # eg: receives 3000, returns MMM
    first_digit = int(str(n)[0])
    res = ''
    if first_digit not in (4, 9):
        s, remainder = symbol_of_maximal_value_to_subtract(n)
        res += s
        while remainder > 0:
            s, remainder = symbol_of_maximal_value_to_subtract(remainder)
            res += s
        return res
    else:
        if n == 4:
            return "IV"
        if n == 9:
            return "IX"
        if n == 40:
            return "XL"
        if n == 90:
            return "XC"
        if n == 400:
            return "CD"
        if n == 900:
            return "CM"

class Solution:
    def intToRoman(self, num: int) -> str:
        num_as_str = str(num)
        len_digits = len(num_as_str)
        res = ''

        for idx, x in enumerate(num_as_str):
            n = int(x) * (10 ** (len_digits - idx - 1))
            if n == 0:
                continue
            res += decimal_place_to_roman(n)

        return res
        