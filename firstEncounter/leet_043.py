import json
import numpy as np

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        results = []

        if len1 < len2:
            len1,len2 = len2, len1
            num1,num2 = num2, num1

        if int(num2) == 0:
            return "0"

        sc = np.zeros((len2, len1 + len2+1))

        for i2 in range(len2-1,-1,-1):
            c2 = int(num2[i2])
            cc = 0
            for i1 in range(len1-1,-1,-1):
                c1 = int(num1[i1])
                m = c2*c1+cc
                sc[len2-1-i2, len2-1-i2+len1-1-i1] = m%10
                cc = m/10
            if cc > 0:
                sc[len2-1-i2, len2-1-i2+len1] = cc

        cc = 0
        for i1 in range(len2+len1):
            m = sum(sc[:, i1]) + cc

            results.append(m % 10)
            cc = int(m/10)
        m = sum(sc[:, len1+len2])+cc
        if m>0:
            results.append(m)

        if results[len1+len2-1] == 0:
            results.pop()

        return ''.join(str(int(x)) for x in reversed(results))


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            num1 = stringToString(line)
            line = sys.stdin.readline().rstrip('\n')
            num2 = stringToString(line)

            ret = Solution().multiply(num1, num2)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()