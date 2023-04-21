class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # def get_short_list(nums: list[int], n_value: int):
        #     n_list = sorted(nums)
        #     print(nums)
        #     left = 0
        #     right = len(n_list)
        #     while (right - left > 1):
        #         i = left + (right - left) // 2
        #         if n_value < n_list[i]:
        #             right = i
        #         else:
        #             left = i
        #     return nums[:right]

        def twice_num(x):
            ind_1 = nums.index(x)
            ind_2 = nums[ind_1 + 1:].index(x) + ind_1 + 1
            return [ind_1, ind_2]

        short_list = nums
        for n, x in enumerate(short_list):
            for y in short_list[n + 1:]:
                if x + y == target:
                    if x != y:
                        return [nums.index(x), nums.index(y)]
                    else:
                        return twice_num(x)
        if target == 0:
            return twice_num(0)


nums, target = [1, 2, 3, 10, 10, 10, 10, 3], 6
print(Solution().twoSum(nums, target))
