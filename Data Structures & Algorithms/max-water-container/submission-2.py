class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute force, iterate through every i * j
        # solution = 0

        # for i in range(len(heights)-1):
        #     for j in range(i+1, len(heights)):
        #         localMin = min(heights[i], heights[j])
        #         localArea = (j-i) * localMin
        #         solution = max(solution, localArea)

        # return solution

        # Optimal, two pointer
        solution = 0
        left, right = 0, len(heights)-1
        while left < right:
            localMin = min(heights[left], heights[right])
            localArea = (right - left) * localMin
            solution = max(solution, localArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return solution