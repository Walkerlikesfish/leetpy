import json

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)

        cur_rest = limit
        ptr_min = 0
        ptr_max = len(people)-1
        cnt = 0

        while ptr_max >= ptr_min:
            # print people[ptr_min], people[ptr_max]
            cur_rest -= people[ptr_max]
            ptr_max -= 1
            if cur_rest >= people[ptr_min]:
                ptr_min += 1
            cnt += 1
            cur_rest = limit

        return cnt



def stringToIntegerList(input):
    return json.loads(input)


def stringToInt(input):
    return int(input)


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
            people = stringToIntegerList(line)
            line = sys.stdin.readline().rstrip('\n')
            limit = stringToInt(line)

            ret = Solution().numRescueBoats(people, limit)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()