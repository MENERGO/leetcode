class Solution:
    def countBits(self, n: int) -> list[int]:
        lst = [0] * (n + 1)
        for i in range(n + 1):
            lst[i] = bin(i)[2:].count('1')
        return lst
