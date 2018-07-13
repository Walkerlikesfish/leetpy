class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ns = len(s)
        nt = len(t)
        d = [0]*(nt+1)
        d[0] = 1

        for ii in range(1, ns+1):
            for ij in range(nt, 0, -1):
                if s[ii-1] == t[ij-1]:
                    d[ij] += d[ij-1]
        return d[nt]



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
            line = sys.stdin.readline().rstrip('\n')
            t = stringToString(line)

            ret = Solution().numDistinct(s, t)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()