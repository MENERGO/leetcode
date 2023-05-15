class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        res = 0
        k = 0
        for i in range(0, len(nums)):
            if val == nums[i]:
                k -= 1
            else:
                res += 1
                nums[k] = nums[i]
            k += 1
        return res, nums


print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
