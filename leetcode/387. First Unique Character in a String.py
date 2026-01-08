from collections import Counter
# easy, hash table
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for index, i in enumerate(s):
            if counter[i] == 1:
                return index
        return -1