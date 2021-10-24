class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        curr_row = 0
        max_col = len(matrix[0]) - 1
        
        while curr_row < len(matrix) and max_col >= 0:
            if matrix[curr_row][max_col] > target:
                print("%d > %d, remove last col" %(matrix[curr_row][max_col], target))
                
                max_col -= 1

            elif matrix[curr_row][max_col] < target:
                print("%d < %d, move to next row" %(matrix[curr_row][max_col], target))
                curr_row += 1
            if not curr_row < len(matrix) and max_col >= 0:
                return False
            if matrix[curr_row][max_col] == target:
                return True
        return False