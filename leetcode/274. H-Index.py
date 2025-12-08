from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        h = 0
        for i, c in enumerate(citations, start=1):
            # Does the i-th most cited paper have at least i citations?
            if c >= i:
                h = i
            else:
                break
        return h