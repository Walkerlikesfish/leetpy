import json

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sa = sum(A)
        sb = sum(B)
        dif = abs(sa - sb)
        dif /= 2
        f_swap = False
        if sa > sb:
            A,B = B,A # A is always smaller
            f_swap = True
        for a in A:
            if a + dif in B:
                if f_swap:
                    return [a+dif, a]
                return [a, a+dif]


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
            A = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            B = stringToIntegerList(line)

            ret = Solution().fairCandySwap(A, B)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()