class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mx = 0
        result = 0
        for i in set(nums):
            if nums.count(i) > mx:
                mx = nums.count(i)
                result = i
        return result
