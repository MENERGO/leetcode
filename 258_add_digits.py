class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        while len(n) > 1:
            n = str(sum(list(map(int, (list(n))))))
        return n
