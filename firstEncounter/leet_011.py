import json

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n_h = len(height)
        if n_h == 1:
            return height[0]
        maxA = 0
        l = 0
        r = n_h-1
        while l<r:
            maxA = max(maxA, min(height[l], height[r])*(r-l))
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return maxA


def stringToIntegerList(input):
    return json.loads(input)


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
            height = stringToIntegerList(line)

            ret = Solution().maxArea(height)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()