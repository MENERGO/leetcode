class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                return end + 1
        return end + 1


print(Solution().searchInsert(nums=[1, 4, 6, 7, 8, 9], target=6))
