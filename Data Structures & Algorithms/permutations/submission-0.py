class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        pick = [False] * len(nums)

        def dfs(permList, pick):
            if len(permList) >= len(nums):
                res.append(permList.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    permList.append(nums[i])
                    pick[i] = True
                    dfs(permList, pick)
                    permList.pop()
                    pick[i] = False

        dfs([], pick)

        return res

        
        