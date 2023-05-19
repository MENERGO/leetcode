class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        count = 0

        def func(num, z):
            nonlocal count
            if z * 2 > num:
                return 0
            count += math.comb(num - z, z)
            func(num, z + 1)
            return int(count)

        return func(n, 0)
