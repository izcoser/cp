from heapq import heapify, heappush, heappop
from collections import Counter
from typing import List

# medium, heap, queue

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0

        h = [-val for _, val in count.items()]
        heapify(h)
        queue = []
        time = 0
        while h or queue:
            time += 1
            if h:
                val = heappop(h)
                val += 1 # we executed the task
                if val < 0:
                    queue.append((val, time + n))

            if queue and queue[0][1] <= time:
                val = queue[0][0]
                heappush(h, val)
                queue = queue[1:]

        return time