class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i - 1]:
                return False
        return True


'''
        return str(x) == str(x)[::-1]
'''

print(Solution().isPalindrome(0))
