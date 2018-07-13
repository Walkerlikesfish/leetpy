import json

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n_left = len(words)
        n = n_left
        cur_line_words = []
        cur_line_left = maxWidth
        self.f_res = []

        while n_left>0:
            cur_word = words[n-n_left]
            cur_word_len = len(cur_word)
            if cur_line_left >= cur_word_len:
                if cur_line_left == cur_word_len and len(cur_line_words) == 0:
                    self.f_res.append(cur_word)
                    n_left -= 1
                else:
                    cur_line_words.append(cur_word)
                    cur_line_left -= (cur_word_len+1) # count one space at least
                    n_left -= 1
            else: # cur_line_left < cur_word_len
                cur_line_cnt = len(cur_line_words)
                cur_line_left += 1
                if cur_line_cnt > 1:
                    cur_line_spaces = [1] * cur_line_cnt
                    cur_line_spaces = [cur_line_left / (cur_line_cnt - 1) + x for x in cur_line_spaces]
                    for i in range(cur_line_left % (cur_line_cnt - 1)):  # left have more space than right space
                        cur_line_spaces[i] += 1
                    res = ''
                    for i in range(cur_line_cnt):
                        res += cur_line_words[i]
                        if i == cur_line_cnt - 1:
                            continue
                        res += ' ' * cur_line_spaces[i]
                elif cur_line_cnt == 1:
                    res = cur_line_words[0] + ' ' * (maxWidth - len(cur_line_words[0]))
                cur_line_words = []
                cur_line_left = maxWidth
                self.f_res.append(res)

            # deal with the last line
            if n_left == 0:
                if len(cur_line_words) == 1:
                    res = cur_line_words[0] + ' '* (maxWidth-len(cur_line_words[0]))
                    self.f_res.append(res)
                elif len(cur_line_words) > 1:
                    res = ''
                    for w in cur_line_words:
                        res+=w
                        res+=' '
                    res += ' '*(maxWidth-len(res))
                    if len(res) > maxWidth:
                        res = res[0:-1]
                    self.f_res.append(res)

        return self.f_res


def stringToStringArray(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            words = stringToStringArray(line)
            line = sys.stdin.readline().rstrip('\n')
            maxWidth = stringToInt(line)

            ret = Solution().fullJustify(words, maxWidth)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()