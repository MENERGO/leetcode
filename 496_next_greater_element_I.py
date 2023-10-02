class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        out = []
        for i in nums1:
            n = nums2.index(i)
            lst = [x for x in nums2[n + 1:] if x > nums2[n]]
            if lst:
                out.append(lst[0])
            else:
                out.append(-1)
        return out
