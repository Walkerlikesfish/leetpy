import json

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        cn = n-1
        v = digits[cn] + 1
        digits[cn] = v%10
        c = v/10
        while c>0 and cn>=0:
            cn-=1
            if cn<0:
                break
            v = digits[cn]+c
            digits[cn] = v%10
            c = v/10
        if c>0 and cn<0:
            digits.insert(0,1)
        return digits



def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys

    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            digits = stringToIntegerList(line)

            ret = Solution().plusOne(digits)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()