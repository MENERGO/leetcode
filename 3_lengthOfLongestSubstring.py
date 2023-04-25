class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        was = []
        long = 0
        if len(s) == len(set(s)):
            return len(s)
        for j in range(len(s) - 1):
            for i in s[j:]:
                if i not in was:
                    was.append(i)
                else:
                    if len(was) > long:
                        long = len(was)
                    was = []
                    break
        if len(was) > long:
            long = len(was)
        return long

        # import itertools
        # set_s = set(s)
        # if set_s == 1:
        #     return 1
        # for L in range(len(s) + 1, 0, -1):
        #     for subset in itertools.permutations(set_s, L):
        #         if ''.join(subset) in s:
        #             return len(subset)
        # return 0
