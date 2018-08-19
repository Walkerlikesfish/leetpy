import json

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        A = sorted(A)
        t = 1
        mask = 10**9+7
        res = 0
        for i in range(n):
            res = (res + A[i] * (t<<i) - A[i] * (t << (n-1-i))) % mask
        return res%mask


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            A = stringToIntegerList(line)

            ret = Solution().sumSubseqWidths(A)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()