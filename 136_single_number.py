class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        while True:
            if nums.count(nums[0]) == 1:
                return nums[0]
            else:
                x = nums[0]
                del nums[0]
                nums.remove(x)


print(Solution().singleNumber([4, 1, 2, 1, 2]))
