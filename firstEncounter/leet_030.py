import json


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        n_words = len(words)
        if n_words == 0:
            return []
        if len(s) == 0:
            return []
        results = []

        cnt_dict = {}
        for w in words:
            if w in cnt_dict:
                cnt_dict[w] += 1
            else:
                cnt_dict[w] = 1

        l_w = len(words[0])

        for i in range(0, len(s)-l_w*n_words+1):
            l = i
            w_cnt = 0
            cur_dict = {}
            while w_cnt < n_words:
                cur_w = s[l:l+l_w]
                l += l_w
                if cur_w in cnt_dict:
                    if cur_w in cur_dict:
                        cur_dict[cur_w] += 1
                    else:
                        cur_dict[cur_w] = 1
                    if cur_dict[cur_w] > cnt_dict[cur_w]:
                        break
                else:
                    break
                w_cnt += 1
            if w_cnt == n_words:
                results.append(i)
        return results


def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringToStringArray(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            words = stringToStringArray(line)

            ret = Solution().findSubstring(s, words)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()