import json
import numpy as np

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        val_row = [[False]*10]*9
        val_col = [[False]*10]*9
        val_block = [[[False]*10]*3]*3

        self.val_block = np.array(val_block)
        self.val_row = np.array(val_row)
        self.val_col = np.array(val_col)
        self.place2t = []
        self.board = board
        self.found = False

        for irow,each_row in enumerate(board):
            for icol,each_ele in enumerate(each_row):
                if each_ele.isdigit():
                    each_ele = int(each_ele)
                    self.val_row[irow, each_ele] = True
                    self.val_col[icol, each_ele] = True
                    self.val_block[irow/3][icol/3][each_ele] = True
                else:
                    self.place2t.append((irow, icol))

        self.resultsa = [0] * len(self.place2t)

        results = self.placeSudoku(0)
        for i,each_coord in enumerate(self.place2t):
            v = self.resultsa[i]
            board[each_coord[0]][each_coord[1]] = str(v)

    def placeSudoku(self, cur_ind):
        # print cur_ind
        if cur_ind >= len(self.place2t):
            self.found = True
            return self.resultsa
        else:
            cur_row = self.place2t[cur_ind][0]
            cur_col = self.place2t[cur_ind][1]
            for vr in range(1, 10):
                if self.val_row[cur_row, vr] == False and self.val_col[cur_col,vr] == False and self.val_block[cur_row/3, cur_col/3, vr] == False:
                    self.board[cur_row][cur_col] = str(vr)
                    self.val_row[cur_row, vr] = True
                    self.val_col[cur_col, vr] = True

                    self.resultsa[cur_ind] = vr

                    self.val_block[cur_row/3, cur_col/3, vr] = True
                    self.placeSudoku(cur_ind+1)
                    if self.found:
                        return

                    self.val_row[cur_row, vr] = False
                    self.val_col[cur_col, vr] = False
                    self.val_block[cur_row/3, cur_col/3, vr] = False



def stringToChar2dArray(input):
    return json.loads(input)


def char2dArrayToString(input):
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
            board = stringToChar2dArray(line)

            ret = Solution().solveSudoku(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print "Do not return anything, modify board in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()