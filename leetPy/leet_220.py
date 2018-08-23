import json
import collections

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        interval = max(t, 1)
        for ix, x in enumerate(nums):
            cur_key = x / interval
            for ek in [cur_key - 1, cur_key, cur_key + 1]:
                if ek in numDict and abs(x - numDict[ek]) <= t:
                    return True
            numDict[cur_key] = x
            if ix >= k:
                numDict.popitem(last=False)
        return False


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
            k = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            t = stringToInt(line)

            ret = Solution().containsNearbyAlmostDuplicate(nums, k, t)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()