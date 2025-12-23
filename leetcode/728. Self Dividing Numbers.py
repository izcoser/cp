from typing import List
# math, easy

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left, right + 1) if is_self_dividing(i) ]
def is_self_dividing(n: int) -> bool:
    for i in str(n):
        if i == '0' or n % int(i) != 0:
            return False
    return True