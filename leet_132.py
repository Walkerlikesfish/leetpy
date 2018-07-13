import json

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n_s = len(s)
        isPa = [[0]*n_s for _ in range(n_s)] # record if s[i:j] is palindrome
        d = [n_s] * (n_s+1)

        for i in range(n_s-1, -1, -1):
            for j in range(i, n_s):
                if i==j or (isPa[i+1][j-1] and s[i] == s[j]) or (j-i==1 and s[i]==s[j]):
                    isPa[i][j] = 1

        d[0] = 0
        for i in range(n_s+1):
            for j in range(i):
                if isPa[j][i-1]:
                    d[i] = min(d[i], d[j]+1)

        return d[n_s]-1

    def is_hw(self, s):
        i = 0
        n = len(s)
        while i<n/2:
            if s[i] != s[n-1-i]:
                return False
            i += 1
        return True


def stringToString(input):
    return input[1:-1].decode('string_escape')


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

            ret = Solution().minCut(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()