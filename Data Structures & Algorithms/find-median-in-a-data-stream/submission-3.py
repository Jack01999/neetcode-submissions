import heapq

class MedianFinder:

    def __init__(self):
        # Large heap, O(1) to get min element
        self.minHeap = []
        # Small heap, O(1) to get max element
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            # Take smallest on large side, and give it to small side
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        elif len(self.maxHeap) > len(self.minHeap):
            return float(self.maxHeap[0] * -1)
        else:
            return (self.minHeap[0] + self.maxHeap[0] * -1) / 2.0
        
        