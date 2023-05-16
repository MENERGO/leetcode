class Solution:
    def myPow(self, x: float, n: int) -> float:
        import math
        if n == 0:
            return 1
        power = 1
        init = x
        while power < n:
            x = x * x
            power = power * 2
        if power == n:
            return x
        z = self.myPow(init, power - n)
        if math.isnan(z):
            return 0
        return x / z


print(Solution().myPow(2.00000, 7))
