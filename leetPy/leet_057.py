# Definition for an interval.
import json


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        intervals_list = []
        results = []
        for each_int in intervals:
            intervals_list.append([each_int.start, each_int.end])
        # intervals_list = sorted(intervals_list, key=lambda x: x[0])
        last_append = True

        print len(intervals)
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        # first the proper place for the start point
        for cur_ind, each_int in enumerate(intervals):
            if newInterval.start <= each_int.end:
                last_append = False
                r_start = min(each_int.start, newInterval.start)

                # now search for the place for the end point
                e_ind  = cur_ind
                while e_ind < len(intervals):
                    if newInterval.end >= intervals[e_ind].start:
                        e_ind += 1
                    else:
                        break
                e_ind -= 1
                r_end = max(intervals[e_ind].end, newInterval.end)

                # insert before cur_ind : r_end < cur_ind.start
                if e_ind<cur_ind:
                    intervals.insert(cur_ind, newInterval)
                else:
                    newInterval.start = r_start
                    newInterval.end = r_end
                    num_int = e_ind - cur_ind + 1
                    while num_int > 0:
                        num_int -= 1
                        intervals.pop(cur_ind)
                    intervals.insert(cur_ind, newInterval)
                break

        # the newInterval should be appended after all ints
        if last_append:
            intervals.append(newInterval)

        return intervals

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
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            intervals = stringToIntervalArray(line)
            line = sys.stdin.readline().rstrip('\n')
            newInterval = stringToInterval(line)

            ret = Solution().insert(intervals, newInterval)

            out = intervalArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()