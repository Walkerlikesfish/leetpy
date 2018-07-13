class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x<0:
            neg = True
            x = -x
        s = str(x)
        s = s[::-1]
        x_new = int(s)
        v_max = 2147483648
        if neg and x_new<=v_max:
            return -x_new
        if not neg and x_new<v_max:
            return x_new
        return 0


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
            x = stringToInt(line)

            ret = Solution().reverse(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()