class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        st = [0]
        for es in S:
            if es == '(':
                st.append(0)
            elif es == ')':
                if st[-1] == 0:
                    st.pop()
                    st[-1] += 1
                elif st[-1] > 0:
                    v = st.pop()
                    st[-1] += v*2
        # print st
        return st[0]


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            S = stringToString(line)

            ret = Solution().scoreOfParentheses(S)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()