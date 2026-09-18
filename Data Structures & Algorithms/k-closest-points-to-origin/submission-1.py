import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []

        for i in range(len(points)):
            originX = 0
            originY = 0
            pointX = points[i][0]
            pointY = points[i][1]
            distance = math.sqrt((pointX - originX)**2 + (pointY-originY)**2)
            heapq.heappush(minHeap, (distance, i))

        while len(res) < k:
            closest = heapq.heappop(minHeap)
            res.append(points[closest[1]])

        return res

        

        