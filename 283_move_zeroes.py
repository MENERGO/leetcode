class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = 0
        len_n = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                count_zeros += 1
                for j in range(i + 1, len_n + 1 - count_zeros):
                    nums[j - 1] = nums[j]
        for i in range(len(nums) - 1, len(nums) - 1 - count_zeros, -1):
            nums[i] = 0
        return nums


print(Solution().moveZeroes(nums=[0, 0, 0]))

# no = []
# z = []
# for i in nums:
#     if i != 0:
#         no.append(i)
#     else:
#         z.append(i)
# nums[:] = no + z


# count_zeros = 0
# len_n = len(nums)
# for n, i in enumerate(range(len(nums) - 1, -1, -1)):
#     if nums[i] == 0:
#         count_zeros += 1
#         nums = nums[:i] + nums[i + 1:len_n + 1 - count_zeros] + [0] * count_zeros
# return nums
