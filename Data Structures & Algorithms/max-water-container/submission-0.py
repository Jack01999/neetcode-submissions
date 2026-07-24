class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force, iterate through every i * j
        solution = 0

        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                localMin = min(heights[i], heights[j])
                localArea = (j-i) * localMin
                solution = max(solution, localArea)

        return solution