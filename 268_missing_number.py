class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return list(set(range(len(nums) + 1)) - set(nums))[0]


print(Solution().missingNumber(nums=[3, 0, 1]))

'''
        summ = sum(nums)
        n = len(nums)
        return (n * (n + 1)) // 2 - summ
'''
