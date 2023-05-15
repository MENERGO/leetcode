class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        x = nums[0]
        res = 1
        k = 1
        for i in range(1, len(nums)):
            if x == nums[i]:
                k -= 1
            else:
                res += 1
                nums[k] = nums[i]
            x = nums[i]
            k += 1
        return res


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
