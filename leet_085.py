import json

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n_r = len(matrix)
        if n_r == 0:
            return 0
        n_c = len(matrix[0])
        res = 0
        d = [0] * n_c
        for ir in range(n_r):
            for ic in range(n_c):
                if matrix[ir][ic] == '0':
                    d[ic] = 0
                else:
                    d[ic] += 1
            res = max(res, self.calcOneLine(d))

        # d= [0,1]
        # res = self.calcOneLine(d)

        return res

    def calcOneLine(self, td):
        res = 0
        st = []
        d = list(td)
        d.append(0)

        for indd, ed in enumerate(d):
            if len(st) == 0 or ed>=d[st[-1]]:  # append the index
                st.append(indd)
            else:
                while len(st)>0 and d[st[-1]]>ed:
                    t_id = st.pop()
                    t_height = d[t_id]
                    if len(st) == 0: # if the stack is empty
                        pre_id = -1
                    else:
                        pre_id = st[-1]
                    res = max(res, t_height*(indd-pre_id-1))
                st.append(indd)
        return res

def stringToChar2dArray(input):
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
            matrix = stringToChar2dArray(line)

            ret = Solution().maximalRectangle(matrix)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()