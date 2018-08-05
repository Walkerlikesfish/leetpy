class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        N = 0
        for ic, c in enumerate(S):
            if c.isdigit():
                N *= int(c)
            else:
                N += 1
            if N>=K:
                break

        for i in range(ic, -1, -1):
            c = S[i]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K==N or K==0:
                    return c
                else:
                    N -= 1



def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringToInt(input):
    return int(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            S = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            K = stringToInt(line)

            ret = Solution().decodeAtIndex(S, K)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()