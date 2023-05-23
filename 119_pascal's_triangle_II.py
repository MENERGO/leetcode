class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            pre = [1]
            for j in range(1, i):
                pre.append(result[-1][j - 1] + result[-1][j])
            result.append(pre + [1])
        return result[rowIndex]
