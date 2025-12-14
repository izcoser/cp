from collections import Counter
from typing import List

# easy, counting 
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter((s1 + " " + s2).split())
        return [w for w, f in count.items() if f == 1]