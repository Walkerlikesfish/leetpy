class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n_s = len(s)
        if num_rows == 1:
            return s
        ind_list = []
        p_value = 0
        for irow in range(num_rows):
            ind_row = irow
            inter_a = 2*num_rows-(ind_row+1)*2
            inter_b = (ind_row)*2
            a = False
            cur_v = irow + 1
            p_value = 0
            while cur_v <= n_s:
                a = not a
                if cur_v != p_value:
                    ind_list.append(cur_v)
                    p_value = cur_v
                if a:
                    cur_v += inter_a
                else:
                    cur_v += inter_b
        result = []
        for each_ind in ind_list:
            result.append(s[each_ind-1])
        return ''.join(result)


def stringToString(input):
    return input[1:-1].decode('string_escape')


def stringToInt(input):
    return int(input)


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            s = stringToString(line)

            line = sys.stdin.readline().rstrip('\n')
            numRows = stringToInt(line)

            ret = Solution().convert(s, numRows)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()