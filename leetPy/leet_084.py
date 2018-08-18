import json

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        res, stack = 0, [0]
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i-1-stack[-1]
                res = max(res, h*w)
            stack.append(i)
        return res


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
            line = sys.stdin.readline().strip('\n')
            heights = stringToIntegerList(line)

            ret = Solution().largestRectangleArea(heights)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()