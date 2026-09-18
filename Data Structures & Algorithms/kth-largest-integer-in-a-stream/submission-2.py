import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myHeap = nums[:k]
        self.k = k
        heapq.heapify(self.myHeap)

        for num in nums[k:]:
            if num > self.myHeap[0]:
                heapq.heappushpop(self.myHeap, num)

        print(self.myHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.myHeap, val)
        if len(self.myHeap) > self.k:
            heapq.heappop(self.myHeap)
        return self.myHeap[0]
        # if len(self.myHeap) == 0:
        #     heapq.heappush(self.myHeap, val)
        # if val > self.myHeap[0]:
        #     heapq.heappushpop(self.myHeap, val)
        # return self.myHeap[0]
        
