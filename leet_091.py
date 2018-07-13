import json

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            if int(s) > 0 and int(s) < 10:
                return 1
        d = [0] * (n + 1)
        d[0] = 1

        for i in range(1, n+1): # ptr to d array
            i1 = i-1 # ptr to string
            cur_d = int(s[i1])
            vd = 0
            if cur_d > 0 and cur_d < 10:
                vd += d[i-1]
            cur_d += int(s[i1-1])*10
            if i>1 and cur_d >= 10 and cur_d <= 26:
                vd += d[i-2]
            d[i] = vd
        return d[n]



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

            ret = Solution().numDecodings(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()