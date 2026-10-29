class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        l, r = 0, n*m-1
        while r >= l:
            mid = (r+l)//2
            val = matrix[mid // m][mid % m]
            if target == val:
                return True
            if val > target:
                r = mid - 1
            else:
                l = mid + 1
        return False