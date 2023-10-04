class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        am = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm',
        ]
        result = []
        for word in words:
            for string in am:
                if set(word.lower()) <= set(string):
                    result.append(word)
                    break
        return result
