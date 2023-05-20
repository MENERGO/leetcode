class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        if len(nums) == 2:
            if nums[0] < nums[1]:
                return nums
            nums[0], nums[1] = nums[1], nums[0]
        for j in range(1, len(nums)):
            end = False
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    end = False
                if nums[-i] < nums[-i - 1]:
                    nums[-i], nums[-i - 1] = nums[-i - 1], nums[-i]
                    end = False
            if end:
                break


print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
