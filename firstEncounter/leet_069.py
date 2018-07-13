class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        start = 1
        end = x
        while start<=end:
            mid = (start + end)/2
            v = x/mid
            if v<mid:
                end = mid-1
            else:
                if v == mid:
                    return mid
                else:
                    start = mid+1
        return end


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
            x = stringToInt(line)

            ret = Solution().mySqrt(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()