class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True


print(Solution().containsDuplicate(nums=[1, 1]))
