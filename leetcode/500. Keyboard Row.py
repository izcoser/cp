from typing import List
# hashtable, easy
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        ret = []
        for w in words:
            wset = set(w.lower())
            if wset.issubset(first_row) or wset.issubset(second_row) or wset.issubset(third_row):
                ret.append(w)
        
        return ret