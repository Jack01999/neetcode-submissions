class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            leftNum = numbers[left]
            rightNum = numbers[right]
            if leftNum + rightNum == target:
                return [left+1, right+1]
            elif leftNum + rightNum < target:
                left += 1
                continue
            else:
                right -= 1
                continue
        return []