import json

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.cnt_solutions = 0
        self.rec_solutions = []
        self.results = []

        self.placeQs(0, [])
        self.showResults()

        print self.cnt_solutions
        return self.results


    def placeQs(self, cur_row, cur_qs):
        if cur_row == self.n: # reach the final state row
            self.cnt_solutions += 1
            self.rec_solutions.append(cur_qs)
        else:
            for cur_col in range(0,self.n):
                good = True
                for pr,pc in enumerate(cur_qs):
                    if pc == cur_col:  # same col
                        good = False
                        break
                    if abs(pr-cur_row) == abs(pc-cur_col):  # in diag
                        good = False
                        break
                if good:
                    new_qs = list(cur_qs)
                    new_qs.append(cur_col)
                    self.placeQs(cur_row+1, new_qs)

    def showResults(self):
        for cur_res in self.rec_solutions:
            cur_out = []
            for irow,icol in enumerate(cur_res):
                curline = ['.']*self.n
                curline[icol] = 'Q'
                curline = ''.join(curline)
                cur_out.append(curline)
            self.results.append(cur_out)




def stringToInt(input):
    return int(input)


def string2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            n = stringToInt(line)

            ret = Solution().solveNQueens(n)

            out = string2dArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()