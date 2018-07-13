class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        result = 0
        str = str.strip()
        NEG = False

        if len(str) < 1:
            return 0
        if str[0] == '-':
            NEG = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        nums = []
        for c in str:
            if c.isdigit():
                nums.append(c)
            else:
                break
        if len(nums) < 1:
            return 0

        nums = ''.join(nums)
        result = int(nums)

        if NEG:
            result = -result
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result


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
            str = stringToString(line)

            ret = Solution().myAtoi(str)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()