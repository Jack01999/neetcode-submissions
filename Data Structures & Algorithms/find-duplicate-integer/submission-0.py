class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]

        nums.sort()
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return nums[left]
            left += 1
            right += 1

        return 0
        
        
        