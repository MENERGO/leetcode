class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result_list = []
        sub_string = ''
        for i in words:
            if len(i) == maxWidth:
                if sub_string != '':
                    result_list.append(sub_string.lstrip(' '))
                    sub_string = ''
                result_list.append(i)
            elif len(sub_string + i) + 1 > maxWidth:
                result_list.append(sub_string.lstrip(' '))
                sub_string = i
            else:
                if sub_string != '':
                    sub_string += ' ' + i
                else:
                    sub_string += i
        if result_list != []:
            if sub_string != result_list[-1]:
                if sub_string != '':
                    result_list.append(sub_string.lstrip(' '))
        else:
            result_list = [sub_string.lstrip(' ').rstrip(' ')]
        for i in range(len(result_list)):
            if len(result_list[i]) < maxWidth:
                len_i = len(result_list[i])
                words_i = result_list[i].split(' ')
                count_words = len(words_i)
                need_spaces = maxWidth - len_i
                if count_words == 1:
                    result_list[i] = result_list[i] + ' ' * (maxWidth - len(result_list[i]))
                    continue
                every = (need_spaces + count_words - 1) // (count_words - 1)
                need_spaces = (need_spaces + count_words - 1) - every * (count_words - 1)
                new_substring = ''
                for j in range(len(words_i) - 1):
                    more = ''
                    if need_spaces > 0:
                        more = ' '
                        need_spaces -= 1
                    new_substring += words_i[j] + ' ' * every + more
                result_list[i] = new_substring + words_i[-1]
        last = ' '.join([z for z in result_list[-1].split(' ') if z != ''])
        result_list[-1] = last + ' ' * (maxWidth - len(last))
        return result_list


print(Solution().fullJustify(["a", "b", "c", "d", "e"], maxWidth=3))

