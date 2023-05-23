class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            pre = [1]
            for j in range(1, i):
                pre.append(result[-1][j - 1] + result[-1][j])
            result.append(pre + [1])
        return result
