class Solution:
    def reverse(self, x: int) -> int:
        minus = False
        if x == 0:
            return 0
        if x < 0:
            minus = True
        xx = str(x)[::-1].rstrip('-').rstrip('0')
        if minus:
            xx = int(xx) * -1
        else:
            xx = int(xx)
        if xx > 2 ** 31 - 1 or xx < -2 ** 31:
            return 0
        return xx


print(Solution().reverse(-123))
print(Solution().reverse(123))
print(Solution().reverse(120))
print(Solution().reverse(-120))
print(Solution().reverse(1534236469))
print(2 ** 31 - 1)
