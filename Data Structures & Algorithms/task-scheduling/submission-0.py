import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        # Process most frequent tasks first
        freqMap = {}
        for task in tasks:
            freqMap[task] = freqMap.get(task, 0) + 1

        maxHeap = []
        for key, val in freqMap.items():
            heapq.heappush(maxHeap, -val)
        
        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        

        