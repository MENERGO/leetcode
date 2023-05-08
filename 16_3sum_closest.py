class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == target:
                    return sums
                if abs(sums - target) < abs(result - target):
                    result = sums
                if sums < target:
                    j += 1
                elif sums > target:
                    k -= 1
        return result


print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))
