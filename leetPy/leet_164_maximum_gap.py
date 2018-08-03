import json


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        A,B = min(nums), max(nums)
        mgap = (B - A)/n + 1 # gap value between different buckets
        n_bucket = (B - A)/mgap + 1
        buckets = [[] for _ in range(n_bucket)]

        for ie in nums:
            targ_buck = (ie - A) / mgap
            if not buckets[targ_buck]:
                buckets[targ_buck].append(ie)
                buckets[targ_buck].append(ie)
            else:
                buckets[targ_buck][0] = min(buckets[targ_buck][0], ie)
                buckets[targ_buck][1] = max(buckets[targ_buck][1], ie)

        i=0
        while i < len(buckets):
            if buckets[i] == []:
                buckets.pop(i)
            else:
                i+=1
        # print buckets
        res = 0
        for i in range(1, len(buckets)):
            res = max(buckets[i][0] - buckets[i-1][1], res)

        return res


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            nums = stringToIntegerList(line)

            ret = Solution().maximumGap(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()