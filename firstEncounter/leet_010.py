class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n_s = len(s)
        n_p = len(p)

        d = [[0 for _ in range(n_s+1)] for _
             in range(n_p+1)]


        # initialize the d matrix
        # i=0, j=0, nothing is nothing
        d[0][0] = True
        # when i=0 (no pattern is considered) d[i][-] = 0
        # when j=0 (no string is considered)
        for i in range(1, n_p+1):
            if p[i-1] == '*':
                if i==1:
                    d[i][0] = True
                elif i>1:
                    d[i][0] = d[i-2][0]

        # iterate through the matrix
        for i in range(1, n_p+1):
            cur_p = p[i-1]
            for j in range(1, n_s+1):
                if cur_p.islower():
                    if d[i-1][j-1] and s[j-1] == cur_p:
                        d[i][j] = True
                elif cur_p == '.':
                    d[i][j] = d[i-1][j-1]
                elif cur_p == '*':
                    if i>=2 and d[i-2][j]:
                        d[i][j] = True
                    if d[i-1][j]:
                        d[i][j] = True
                    if d[i][j-1]:
                        if p[i-2] == '.':
                            d[i][j] = True
                        elif p[i-2] == s[j-1]:
                            d[i][j] = True

        # print d
        if d[n_p][n_s] == 0:
            return False
        return True


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
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