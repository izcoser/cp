from heapq import heappop, heappush
from typing import List
from collections import defaultdict

# min heap, medium

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict(int)
        for w in words:
            count[w] += 1

        # Also possible to do the above with `collections.Counter(words)`

        h = []
        for key in count:
            heappush(h, (-count[key], key))
            
        # this works because min heap items are already compared lexicographically after priority.
        return [heappop(h)[1] for _ in range(k)]

class SolutionUninformed:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict(int)
        for w in words:
            count[w] += 1

        h = []
        for key in count:
            heappush(h, (-count[key], key))

        # PSA: I was unaware the min heap already compared strings lexicographically after priority.
        # we will have one list for each number of occurrences of elements
        sublists = [[]]
        current_freq = 0
        current_index = 0
        for _ in range(k):
            freq, val = heappop(h)
            if freq == current_freq:
                sublists[current_index].append(val)
            else:
                sublists.append([val])
                current_index += 1
                current_freq = freq

        sorted_sublists = [sorted(sublist) for sublist in sublists]
        flattened = [item for sublist in sorted_sublists for item in sublist]
        return flattened