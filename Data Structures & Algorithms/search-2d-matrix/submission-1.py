class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find what row it is in first
        top, bot = 0, len(matrix)-1
        while top <= bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        
        left, right = 0, len(matrix[mid]) - 1
        while left <= right:
            col = left + (right - left) // 2
            print(col)
            if matrix[mid][col] == target:
                return True
            elif target < matrix[mid][col]:
                right = col - 1
            else:
                left = col + 1
        return False


        