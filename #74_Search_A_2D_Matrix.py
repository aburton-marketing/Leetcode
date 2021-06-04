class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = rows * columns -1
        
        if len(matrix) == 0: return False
        
        while left <= right:
            mid = int(left + (right-left) / 2)
            mid_element = matrix[int(mid/columns)][int(mid%columns)]
            if mid_element == target:
                return True
            elif target < mid_element:
                right = mid - 1
            elif target > mid_element:
                left = mid + 1
        return False
