class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        vals = list(set(nums1) & set(nums2))
        for i in vals:
            if nums1.count(i) > nums2.count(i):
                count = nums2.count(i)
            else:
                count = nums1.count(i)
            for n in range(count):
                result.append(i)
        return result


print(Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
