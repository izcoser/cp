from typing import List
digits_to_chars = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(digits_to_chars[(int)(digits[0])])
        if len(digits) == 2:
            s1 = digits_to_chars[(int)(digits[0])]
            s2 = digits_to_chars[(int)(digits[1])]
            return combine_two(s1, s2)
        if len(digits) == 3:
            s1 = digits_to_chars[(int)(digits[0])]
            s2 = digits_to_chars[(int)(digits[1])]
            s3 = digits_to_chars[(int)(digits[2])]
            return combine_three(s1, s2, s3)
        if len(digits) == 4:
            s1 = digits_to_chars[(int)(digits[0])]
            s2 = digits_to_chars[(int)(digits[1])]
            s3 = digits_to_chars[(int)(digits[2])]
            s4 = digits_to_chars[(int)(digits[3])]
            return combine_four(s1, s2, s3, s4)


def combine_two(s1: str, s2: str) -> List[str]:
    combs = []
    for i in s1:
        for j in s2:
            combs.append(i + j)

    return combs

def combine_three(s1: str, s2: str, s3: str) -> List[str]:
    combs = []
    for i in s1:
        for j in s2:
            for k in s3:
                combs.append(i + j + k)
    return combs


def combine_four(s1: str, s2: str, s3: str, s4: str) -> List[str]:
    combs = []
    for i in s1:
        for j in s2:
            for k in s3:
                for w in s4:
                    combs.append(i + j + k + w)
    return combs
