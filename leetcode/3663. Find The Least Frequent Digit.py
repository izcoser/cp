from collections import Counter
# easy, counting
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        count = Counter(str(n))
        lowest_freq = sorted(count.values())[0]
        return int(sorted([d for d, freq in count.items() if freq == lowest_freq])[0])