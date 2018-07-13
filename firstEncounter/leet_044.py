import numpy as np
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        d = np.zeros((n+1,m+1), dtype=np.int8)

        if n==0 and m ==0:
            return True
        if n>0 and m==0:
            return False

        d[0,0] = True
        for i in range(1, n):
            d[i, 0] = False
        if p[0] == '*':
            d[0, 1] = True
        for j in range(1,m+1):
            if p[j-1] == '*':
                d[0, j] = True
            else:
                break

        for i in range(1, n+1):
            cur_s = s[i-1]
            for j in range(1, m+1):
                cur_p = p[j-1]
                if cur_p.islower():
                    if cur_s == cur_p and d[i-1, j-1]:
                        d[i, j] = True
                elif cur_p == '?':
                    if d[i-1, j-1]:
                        d[i, j] = True
                elif cur_p == '*':
                    if d[i-1, j-1] or d[i, j-1] or d[i-1, j]:
                        d[i, j] = True

        print d

        if d[n,m] == 0:
            return False
        else:
            return True


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
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            p = stringToString(line)

            ret = Solution().isMatch(s, p)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()