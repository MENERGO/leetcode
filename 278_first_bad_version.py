class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        result = 1
        while start <= end:
            x = (start + end) // 2
            if not isBadVersion(x):
                start = x + 1
            else:
                end = x - 1
                result = x
        return result
