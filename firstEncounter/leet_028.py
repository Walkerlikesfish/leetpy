class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # deal with the pos/neg
        NEG = 0
        MAX_NEG = 2147483648

        if (dividend>=0 and divisor>0) or (dividend<0 and divisor<0):
            NEG = 0
        else:
            NEG = 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        cur_sum = 0
        for ii in range(31, -1, -1):
            cur_v = divisor<<ii
            if dividend-cur_v >= 0:
                cur_sum += 1<<ii
                dividend -= cur_v
        print dividend

        if NEG:
            return -cur_sum
        else:
            if cur_sum > MAX_NEG-1:
                return MAX_NEG-1
        return cur_sum



def stringToInt(input):
    return int(input)


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
            dividend = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            divisor = stringToInt(line)

            ret = Solution().divide(dividend, divisor)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()