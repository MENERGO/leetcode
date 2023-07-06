class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        while l < len(s) // 2:
            s[l], s[-l - 1] = s[-l - 1], s[l]
            l += 1


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
