class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1000: 'M', 900: 'CM', 500:'D', 400:'CD', 100:'C', 90: 'XC', 50: 'L', 40: 'XL', 10:'X', 9:'IX', 5:'V',
             4:'IV', 1:'I'}
        out = ''
        for cur in sorted(d, reverse=True):
            n_cur = num/cur
            out += d[cur]*n_cur
            num -= n_cur * cur
            print num, cur, n_cur
        return out


def stringToInt(input):
    return int(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            num = stringToInt(line)

            ret = Solution().intToRoman(num)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()