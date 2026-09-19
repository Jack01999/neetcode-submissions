import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        #print(res)
        for i in range(len(nums)):
            curr = nums[i]
            clone = copy.deepcopy(res)
            for j in range(len(clone)):
                currClone = clone[j]
                #print("currClone : ", currClone)
                currClone.append(curr)
                res.append(currClone)
            #print("Clone : ", clone)
            #print("res : ", res)

        return res
        