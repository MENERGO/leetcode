class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = ''.join(map(str, digits))
        return list(str(int(number) + 1))


print(Solution().plusOne([1, 2, 3]))
