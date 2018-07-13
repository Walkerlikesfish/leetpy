import json

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""

        minlen = len(strs[0])
        for s in strs:
            cur_len = len(s)
            if cur_len < minlen:
                minlen = cur_len

        if minlen == 0:
            return ""
        else:
            for i in range(minlen):
                cs = strs[0][i]
                for s in strs:
                    if s[i] != cs:
                        print i,s[i],cs
                        if i==0:
                            return ""
                        return strs[0][0:i]
            return strs[0][0:minlen]


def stringToStringArray(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            strs = stringToStringArray(line)

            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()