class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        if lb>la: # b is always shorter one
            lb,la,a,b = la,lb,b,a

        res = []
        cc = 0
        for i in range(lb):
            ca = int(a[la-1-i])
            cb = int(b[lb-1-i])
            v = ca+cb+cc
            res.append(v%2)
            cc = v/2
        for i in range(la-lb-1,-1,-1):
            v = int(a[i]) + cc
            res.append(v%2)
            cc = v/2
        if cc>0:
            res.append(1)
        res = reversed(res)

        return ''.join(str(x) for x in res)


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            a = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            b = stringToString(line)

            ret = Solution().addBinary(a, b)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()