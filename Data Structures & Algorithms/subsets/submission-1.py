import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for curr in nums:
            n = len(res)  # freeze length before growing
            for j in range(n):
                res.append(res[j] + [curr])  # new list, no shared reference, no deepcopy
        return res
        