import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, stone * -1)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if y > x:
                heapq.heappush(maxHeap, x - y)

        return abs(maxHeap[0]) if maxHeap else 0




        