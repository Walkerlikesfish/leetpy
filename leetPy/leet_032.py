class Solution(object):
    def longestValidParentheses(self, s):
        n = len(s)

        # Create a stack and push -1 as initial index to it.
        stk = []
        stk.append(-1)

        # Initialize result
        result = 0

        # Traverse all characters of given string
        for i in xrange(n):

            # If opening bracket, push index of it
            if s[i] == '(':
                stk.append(i)

            else:  # If closing bracket, i.e., str[i] = ')'

                # Pop the previous opening bracket's index
                stk.pop()

                # Check if this length formed with base of
                # current valid substring is more than max
                # so far
                if len(stk) != 0:
                    result = max(result, i - stk[len(stk) - 1])

                # If stack is empty. push current index as
                # base for next valid substring (if any)
                else:
                    stk.append(i)

        return result


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
            line = sys.stdin.readline().strip('\n')
            s = stringToString(line)

            ret = Solution().longestValidParentheses(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()