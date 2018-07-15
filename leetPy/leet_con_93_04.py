import json

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if not stations:
            if target <= startFuel:
                return 0
            else:
                return -1
        ns = len(stations)
        d = [[-1] * (ns+1) for _ in range(ns+1)]
        d[0][0] = startFuel
        for i in range(1, ns+1):
            if i == 1:
                cur_dist = stations[0][0]
            else:
                cur_dist = stations[i - 1][0] - stations[i - 2][0]
            for j in range(0, i+1):
                if j>=1 and d[i-1][j-1]-cur_dist>=0:
                    d[i][j] = d[i-1][j-1]-cur_dist+stations[i-1][1]
                if d[i-1][j] - cur_dist >= 0:
                    d[i][j] = max(d[i][j], d[i-1][j]-cur_dist)
        print d
        for i in range(ns+1):
            if d[ns][i] >= target - stations[-1][0]:
                return i
        return -1


def stringToInt(input):
    return int(input)


def stringToInt2dArray(input):
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
            target = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            startFuel = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            stations = stringToInt2dArray(line)

            ret = Solution().minRefuelStops(target, startFuel, stations)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()