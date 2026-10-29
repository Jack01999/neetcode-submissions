class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap = []
        sortedList = []
        for num in nums:
            heapq.heappush(heap, num)

        while heap:
            sortedList.append(heapq.heappop(heap))
        
        if len(sortedList) <= 1:
            return len(sortedList)
        solution = 1
        currMax = 1
        for i in range(1, len(sortedList)):
            if sortedList[i] == sortedList[i-1]:
                continue
            
            if sortedList[i] == sortedList[i-1]+1:
                currMax += 1
            else:
                currMax = 1
            solution = max(solution, currMax)


        return solution