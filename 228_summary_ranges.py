class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        def check(s, e):
            if s != e:
                result.append(f'{s}->{e}')
            else:
                result.append(f'{s}')

        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        result = []
        start = end = nums[0]
        for n, i in enumerate(range(1, len(nums))):
            if nums[i] != end + 1:
                check(start, end)
                start = end = nums[i]
            else:
                end = nums[i]
            if n == len(nums) - 2:
                check(start, end)
        return result


print(Solution().summaryRanges(nums=[]))
