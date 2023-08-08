class Solution:
    def reverseBits(self, n: int) -> int:
        ln = len(bin(n)[2:])
        return int((bin(n)[2:][::-1] + '0' * (32 - ln)), 2)
