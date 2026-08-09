from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = []

        while maxHeap or queue:
            time += 1

            if maxHeap:
                freq = -heapq.heappop(maxHeap)
                freq -= 1

                if freq > 0:
                    queue.append((freq, time + n))

            if queue and queue[0][1] == time:
                freq, _ = queue.pop(0)
                heapq.heappush(maxHeap, -freq)

        return time


