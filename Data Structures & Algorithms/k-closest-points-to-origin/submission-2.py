import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        maxHeap = []

        for i in range(len(points)):
            originX = 0
            originY = 0
            pointX = points[i][0]
            pointY = points[i][1]
            distance = -(math.sqrt((pointX - originX)**2 + (pointY-originY)**2))
            heapq.heappush(maxHeap, (distance, i))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        while len(res) < k:
            closest = heapq.heappop(maxHeap)
            res.append(points[closest[1]])

        return res

        

        