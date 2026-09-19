class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, currList, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(nums):
                return
            subset.append(nums[i])
            dfs(i, currList, total + nums[i])
            subset.pop()
            dfs(i+1, currList, total)

        dfs(0, [], 0)
        return res

        