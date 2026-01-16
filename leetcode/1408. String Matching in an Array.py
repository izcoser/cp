from typing import List
# string matching, easy
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = set()
        for w in words:
            for j in words:
                if w == j or w in ret:
                    continue
                if w in j:
                    ret.add(w)
        return list(ret)