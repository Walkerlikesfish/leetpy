import json

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # do not consider the N=0 case
        cur_sum = 0
        tou_sum = 0
        N = len(gas)
        res_i = 0

        for i in range(N):
            cur_gain = gas[i] - cost[i]
            tou_sum += cur_gain
            cur_sum += cur_gain
            if cur_sum < 0:
                cur_sum = 0
                res_i = i+1
        if tou_sum < 0 or res_i >= N:
            return -1
        else:
            return res_i


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
            gas = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            cost = stringToIntegerList(line)

            ret = Solution().canCompleteCircuit(gas, cost)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()