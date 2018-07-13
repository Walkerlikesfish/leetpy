class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool

        0 1 2 4 6 7 8
        7 8 0 1 2 4 6
        4 6 7 8 0 1 2
        2 4 6 7 8 0 1

        mid = (left + right)/2
        nums[mid]

        """


def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            target = stringToInt(line)

            ret = Solution().search(nums, target)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()