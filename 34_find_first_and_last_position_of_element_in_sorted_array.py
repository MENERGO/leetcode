class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = [-1, -1]
        if target in nums:
            result[0] = nums.index(target)
            result[1] = len(nums) - nums[::-1].index(target) - 1
        return result


print(Solution().searchRange(nums=[], target=0))
