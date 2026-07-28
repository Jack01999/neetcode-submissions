class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        solution = 1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)
                    solution = max(solution, dp[j])
        return solution