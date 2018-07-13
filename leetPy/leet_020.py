class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        ptr_s = 0
        bracket_dict = {'(':')', '[':']', '{':'}'}
        for cur_s in s:
            if cur_s in bracket_dict:
                stack.append(bracket_dict[cur_s])
                ptr_s += 1
            else:
                try:
                    cur_r = stack.pop()
                    if cur_s != cur_r:
                        return False
                except IndexError:
                    return False
        if len(stack) == 0:
            return True
        return False



def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)

            ret = Solution().isValid(s)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()