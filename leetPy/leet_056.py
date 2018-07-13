import json

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n==0:
            return []
        intervals_list = []
        results = []
        for each_int in intervals:
            intervals_list.append([each_int.start, each_int.end])
        intervals_list = sorted(intervals_list, key=lambda x: x[0])

        cur_int = Interval(intervals_list[0][0], intervals_list[0][1])
        for each_int in intervals_list:
            if each_int[0] >= cur_int.start and each_int[0] <= cur_int.end:
                if each_int[1] > cur_int.end:
                    cur_int.end = each_int[1]
            elif each_int[0] > cur_int.end:
                new_int = Interval(cur_int.start, cur_int.end)
                results.append(new_int)
                cur_int.start = each_int[0]
                cur_int.end = each_int[1]
        new_int = Interval(cur_int.start, cur_int.end)
        results.append(new_int)
        return results


def stringToInterval(input):
    tokens = json.loads(input)
    return Interval(tokens[0], tokens[1])


def stringToIntervalArray(input):
    intervalArrays = json.loads(input)
    nodes = []
    for intervalArray in intervalArrays:
        nodes.append(stringToInterval(json.dumps(intervalArray)))
    return nodes


def intervalToString(interval):
    return "[{}, {}]".format(interval.start, interval.end)


def intervalArrayToString(intervalArray):
    serializedIntervals = []
    for interval in intervalArray:
        serializedInterval = intervalToString(interval)
        serializedIntervals.append(serializedInterval)
    return "[{}]".format(', '.join(serializedIntervals))


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            intervals = stringToIntervalArray(line)

            ret = Solution().merge(intervals)

            out = intervalArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()