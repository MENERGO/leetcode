class Solution:
    def reverseVowels(self, s: str) -> str:
        swap = []
        result = ''
        for i in s:
            if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                swap.append(i)
        for i in s:
            if i.lower() in ['a', 'e', 'i', 'o', 'u']:
                result += swap.pop()
            else:
                result += i
        return result


print(Solution().reverseVowels(s="hello"))
