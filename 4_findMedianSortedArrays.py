class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        import statistics
        new = nums1 + nums2
        return statistics.median(new)


print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
print(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
