import json

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rstr = ""
        for es in s:
            if es.isalpha() or es.isdigit():
                rstr += es
        rstr = rstr.lower()
        nstr = len(rstr)
        if nstr == 0 and len(s) > 0:
            return False
        if nstr % 2 == 0:
            if rstr[0:nstr/2] == rstr[-1:nstr/2-1:-1]:
                return True
            else:
                return False
        else:
            # 0 1 2 3 4
            if rstr[0:nstr/2] == rstr[-1:nstr/2:-1]:
                return True
            else:
                return False



def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            s = stringToString(line)

            ret = Solution().isPalindrome(s)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()