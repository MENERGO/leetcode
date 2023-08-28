class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 0:
            return 0
        if len(chars) == 1:
            return len(chars)
        x = chars[0]
        result = []
        k = 1
        for i in chars:
            if i == x:
                if i not in result:
                    result.append(x)
                else:
                    k += 1
            else:
                if k != 1:
                    for j in list(str(k)):
                        result.append(j)
                x = i
                k = 1
                result.append(x)
        if k != 1:
            for j in list(str(k)):
                result.append(j)
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)
