# The guess API is already defined for you
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        while True:
            x = int(guess(start + (end - start) / 2))
            if x == 0:
                return x
            if x == 1:
                end = x + 1
            if x == -1:
                start = x - 1
