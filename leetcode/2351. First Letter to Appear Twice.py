from collections import defaultdict
#easy, counting
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        chrs = defaultdict(int)
        for i in s:
            chrs[i] += 1
            if chrs[i] == 2:
                return i