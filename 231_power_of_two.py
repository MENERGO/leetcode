class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n & (n - 1) or n == 0:
            return False
        else:
            return True


print(Solution().isPowerOfTwo(0))
