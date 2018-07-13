class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        s_re = s[::-1]
        #print s_re

        if s == s_re:
            return True
        else:
            return False


def stringToInt(input):
    return int(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            x = stringToInt(line)

            ret = Solution().isPalindrome(x)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()