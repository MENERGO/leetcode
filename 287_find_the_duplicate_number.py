class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))


'''
        for i in nums:
            if nums.count(i) > 1:
                return i
'''

print(Solution().findDuplicate([2, 2]))
