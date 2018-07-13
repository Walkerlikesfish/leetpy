class Solution(object):
    def longestPalindrome_brute(self, s):
        """
        O(n^3) -> Time Exceed
        :type s: str
        :rtype: str
        """
        max_len = len(s)
        s_max_rever = None
        # iterate all substring
        if max_len<2:
            return s
        for cur_len in range(1, max_len+1):
            for cur_c in range(0, max_len-cur_len+1):
                hlf = cur_len / 2
                if cur_len%2 == 1:
                    a_str = s[cur_c:cur_c+hlf+1]
                    b_str = s[cur_c+hlf:cur_c+cur_len]
                else:
                    a_str = s[cur_c: cur_c+hlf]
                    b_str = s[cur_c+hlf: cur_c+cur_len]
                b_rstr = b_str[::-1]
                # print b_rstr,a_str
                if b_rstr == a_str:
                    s_max_rever = s[cur_c: cur_c+cur_len]
        return s_max_rever

    def longestPalindrome_dp(self, s):
        """
        O(n^2) DP
        :param s:
        :return:
        """
        n = len(s)
        if n<2:
            return s

        max_len = 0
        cur_result = s[0]

        d = [[0 for x in range(n)] for y
            in range(n)]
        for i in range(n):
            d[i][i] = True

        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                if l == 2:
                    if s[i]==s[j]:
                        d[i][j] = True
                        max_len = j - i + 1
                        cur_result = s[i:j + 1]
                    else:
                        d[i][j] = False
                else:
                    #print s[i],s[j]
                    if s[i] == s[j] and d[i+1][j-1]:
                        d[i][j] = True
                        if j-i+1 > max_len:
                            max_len = j-i+1
                            cur_result = s[i:j+1]
        return cur_result


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)

            ret = Solution().longestPalindrome_dp(s)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()