class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        re = cnt
        for each_char in s:
            if each_char != ' ':
                cnt += 1
            else:
                if cnt > 0:
                    re = cnt
                cnt = 0
        if cnt > 0:
            re = cnt
        return re

def stringToString(input):
    return input[1:-1].decode('string_escape')


def intToString(input):
    if input is None:
        input = 0
    return str(input)


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

            ret = Solution().lengthOfLastWord(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()