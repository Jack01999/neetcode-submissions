class Solution:
    def trap(self, height: List[int]) -> int:
        solution = 0
        prefixMaxArr = [0] * len(height)
        suffixMaxArr = [0] * len(height)
        prefixMax = 0
        suffixMax = 0
        for i in range(len(height)):
            prefixMax = max(prefixMax, height[i])
            prefixMaxArr[i] = prefixMax
        for i in range(len(height)-1, -1, -1):
            suffixMax = max(suffixMax, height[i])
            suffixMaxArr[i] = suffixMax

        print(prefixMaxArr)
        print(suffixMaxArr)

        for i in range(len(height)):
            solution += min(prefixMaxArr[i], suffixMaxArr[i]) - height[i]


        return solution