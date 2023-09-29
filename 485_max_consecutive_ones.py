class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counts = 0
        max_counts = 0
        for i in nums:
            if i:
                counts += 1
            else:
                if counts > max_counts:
                    max_counts = counts
                counts = 0
        return max(max_counts, counts)
