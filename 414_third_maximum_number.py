class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        set_n = set(nums)
        sort_list_n = sorted(list(set_n), reverse=True)
        return sort_list_n[2]
