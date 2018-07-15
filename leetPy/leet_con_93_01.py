import json
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        mask = 1
        pre_bit = None
        cnt = 0
        res = 0
        while mask < N:
            cur_bit = N & mask
            if cur_bit:
                if pre_bit is not None:

                    res = max(res, cnt - pre_bit)
                pre_bit = cnt
            cnt += 1
            mask = mask << 1
        return res



def stringToInt(input):
    return int(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            N = stringToInt(line)

            ret = Solution().binaryGap(N)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()