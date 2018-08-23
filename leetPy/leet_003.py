class Solution(object):
    def lengthOfLongestSubstring0(self, s):
        """
        :type s: str
        :rtype: int
        """
        past_chars = []
        max_nrc = 0
        cur_nrc = []
        cur_len = 0
        for s_ind, cur_char in enumerate(s):
            if cur_char not in past_chars:
                cur_nrc.append(cur_char)
                cur_len += 1
                max_nrc = max(max_nrc, cur_len)
            else:
                if cur_char not in cur_nrc:
                    cur_nrc.append(cur_char)
                    cur_len += 1
                    max_nrc = max(max_nrc, cur_len)
                else:
                    last_ind = cur_nrc.index(cur_char)
                    cur_nrc = cur_nrc[last_ind+1:]
                    cur_nrc.append(cur_char)
                    cur_len = len(cur_nrc)
                    max_nrc = max(max_nrc, cur_len)
            past_chars.append(cur_char)
        return max_nrc

    def lengthOfLongestSubstring(self, s):
        max_nrc = 0
        cur_nrc = []
        cur_len = 0
        for s_ind, cur_c in enumerate(s):
            if cur_c not in cur_nrc:
                cur_nrc.append(cur_c)
                cur_len += 1
                max_nrc = max(max_nrc, cur_len)
            else:
                last_ind = cur_nrc.index(cur_c)
                cur_nrc = cur_nrc[last_ind+1:]
                cur_len = len(cur_nrc)
                cur_nrc.append(cur_c)
                cur_len += 1
                max_nrc = max(max_nrc, cur_len)
        return max_nrc


# abbcdefeabca


def stringToString(input):
    return input[1:-1].decode('string-escape')


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)

            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()