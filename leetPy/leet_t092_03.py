class Solution(object):
    def is_hw(self, m):
        m_str = str(m)
        l = len(m_str)
        for i in range(l/2):
            if m_str[i] != m_str[l-1-i]:
                return False
        return True

    def get_next_dixround(self, m):
        """
        get m 10base bit number
        :param m:
        :return:
        """
        res = 1
        for i in range(1, m):
            res *= 10
        return res

    def is_prime(self, m):
        i = 3
        while i*i <= m:
            if m % i == 0:
                return False
            i+=2
        return True

    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return 2
        a = N-1
        if N >= 10000001:
            return 100030001
        while True:
            # print a
            a += 1
            if a % 2 == 0 and a != 2:
                continue
            if a % 5 == 0 and a != 5:
                continue
            if not self.is_hw(a):
                continue
            if len(str(a)) % 2 == 0 and a != 11:
                a = self.get_next_dixround(len(str(a))+1)
                continue
            if not self.is_prime(a):
                continue
            return a


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
            line = sys.stdin.readline().strip('\n')
            N = stringToInt(line)

            ret = Solution().primePalindrome(N)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()