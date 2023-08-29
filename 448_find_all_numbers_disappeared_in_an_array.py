class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return set(range(1, len(nums) + 1)).difference(set(nums))

#
