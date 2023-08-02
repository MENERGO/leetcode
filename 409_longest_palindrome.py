from collections import Counter


class Solution:
    def longestPalindrome_2(self, s: str) -> int:
        result = 0
        key = True
        list_s = []
        for i in set(s):
            list_s.append(s.count(i))
        for v in list_s:
            if v % 2 == 0:
                result += v
            else:
                result += v - 1
                if key:
                    if v % 2 != 0:
                        result += 1
                        key = False
        return result


'''
    def longestPalindrome(self, s):
        ans = 0
        for v in Counter(s).values():
            print(v)
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
'''
