from collections import Counter
from typing import List

# medium, counting
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        aggregate_responses = []
        for response_list in responses:
            deduped = list(set(response_list))
            aggregate_responses += deduped
        
        count = Counter(aggregate_responses)
        highest_freq = sorted(count.values())[-1]
        most_common = sorted([w for w, freq in count.items() if freq == highest_freq])[0]
        return most_common