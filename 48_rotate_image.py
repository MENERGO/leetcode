class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                    matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]
        return matrix


print(Solution().rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
