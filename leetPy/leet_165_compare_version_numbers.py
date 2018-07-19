class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1array = version1.split('.')
        v2array = version2.split('.')
        cur = 1
        v1n = 0
        v2n = 0
        for ie in v1array:
            tmp = int(ie) * cur
            v1n += tmp
            cur = float(cur * 0.1)
        cur = 1
        for ie in v2array:
            tmp = int(ie) * cur
            v2n += tmp
            cur = float(cur * 0.1)
        if v1n > v2n:
            return 1
        elif v1n < v2n:
            return -1
        else:
            return 0


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
            version1 = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            version2 = stringToString(line)

            ret = Solution().compareVersion(version1, version2)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()