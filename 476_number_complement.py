class Solution:
    def findComplement(self, num: int) -> int:
        return int('0b' + str(bin(num)).lstrip('0b').replace("0", "x").replace("1", "0").replace("x", "1"), 2)
