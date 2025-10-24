class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ls = []
        n = len(matrix)
        m = len(matrix[0])
        up, down = 0, n - 1
        left, right = 0, m - 1
        while left <= right and up <= down:
            for j in range(left, right + 1):
                ls.append(matrix[up][j])
            up += 1
            for i in range(up, down + 1):
                ls.append(matrix[i][right])
            right -= 1
            if up <= down:
                for j in range(right, left - 1, -1):
                    ls.append(matrix[down][j])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    ls.append(matrix[i][left])
                left += 1
        return ls
