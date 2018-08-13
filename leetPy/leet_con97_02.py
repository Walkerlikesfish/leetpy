import json

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph_map = [[] for _ in range(N+1)]
        colors = [-1] * (N+1)

        for ed in dislikes:
            graph_map[ed[0]].append(ed[1])
            graph_map[ed[1]].append(ed[0])

        def isValid(node, color):
            if colors[node] != -1:
                return colors[node] == color
            else:
                colors[node] = color
                for ed in graph_map[node]:
                    if not isValid(ed, 1-color):
                        return False
                return True

        for i in range(1, N+1):
            if colors[i] == -1 and not isValid(i, 0):
                return False

        return True


def stringToInt(input):
    return int(input)


def stringToInt2dArray(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            N = stringToInt(line)
            line = sys.stdin.readline().rstrip('\n')
            dislikes = stringToInt2dArray(line)

            ret = Solution().possibleBipartition(N, dislikes)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()


"""
    def possibleBipartition(self, N, dislikes):
        tovisit = [x+1 for x in range(N)]
        # build graph
        gmap = {}
        for ed in dislikes:
            ea = ed[0]
            eb = ed[1]
            if ea not in gmap:
                gmap[ea] = [eb]
            else:
                gmap[ea].append(eb)
        while tovisit:
            cur = [tovisit.pop(0)]
            while cur:
                for each in cur:

"""