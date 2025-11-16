class Solution:
    def romanToInt(self, s: str) -> int:
        subtractions = {k: v for k, v in {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}.items() if k in s}
        regulars = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        acc = 0

        for key, val in subtractions.items():
            acc += val
            s = s.replace(key, "")

        for key, val in regulars.items():
            acc += s.count(key) * val
        return acc

        return acc