class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        p = int(10 ** (len(str(x)) // 2 - 1))
        for i in range(p, x // 2 + 100):
            if i * i == x:
                return i
                break
            if i * i > x:
                return i - 1
