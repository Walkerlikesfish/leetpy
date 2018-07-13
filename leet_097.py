class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)

        if l1+l2 != len(s3):
            return False

        if len(s3) == 0:
            return True

        d = [[False]*(l2+1) for _ in range(l1+1)]

        d[0][0] = True
        for i in range(1, l1+1):
            if s1[i-1] == s3[i-1]:
                d[i][0] = True
            else:
                break
        for i in range(1, l2+1):
            if s2[i-1] == s3[i-1]:
                d[0][i] = True
            else:
                break

        for i in range(l1+1):
            for j in range(l2+1):
                if i>=1 and d[i-1][j] and s1[i-1] == s3[i+j-1]:
                    d[i][j] = True
                if j>=1 and d[i][j-1] and s2[j-1] == s3[i+j-1]:
                    d[i][j] = True

        print d
        return d[l1][l2]


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
            s1 = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            s2 = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            s3 = stringToString(line)

            ret = Solution().isInterleave(s1, s2, s3)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()