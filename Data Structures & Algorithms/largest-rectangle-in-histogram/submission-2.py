class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        solution = 0
        stack = [] # [index, height]

        # Iterate through heights, building increasing stack
        for i in range(len(heights)):
            height = heights[i]
            start = i
            while len(stack) > 0 and stack[-1][1] > height:
                #numPopped += 1
                idx, poppedHeight = stack.pop()
                solution = max(solution, (i - idx) * poppedHeight)
                start = idx
            stack.append([start, height])

        # Go through remainder of stack to calculate each area
        while len(stack) > 0:
            idx, poppedHeight = stack.pop()
            solution = max(solution, (len(heights) - idx) * poppedHeight)

        return solution
        