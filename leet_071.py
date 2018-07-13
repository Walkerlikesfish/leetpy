class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')
        res_stack = []
        for each_ele in path_list:
            if each_ele == '' or each_ele == '.':
                continue
            elif each_ele == '..':
                if len(res_stack) == 0:
                    continue
                else:
                    res_stack.pop()
            else: # legal data root
                res_stack.append(each_ele)
        res = ''
        for each in res_stack:
            res += ('/' + each)
        if res == '':
            res = '/'
        return res


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
            path = stringToString(line)

            ret = Solution().simplifyPath(path)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()