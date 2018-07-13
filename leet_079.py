import json
import numpy as np

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.nh = len(board)
        self.nw = len(board[0])
        self.board = board
        self.word = word
        past = np.zeros([self.nh, self.nw])

        for ih in range(self.nh):
            for iw in range(self.nw):
                if board[ih][iw] == word[0]:
                    past[ih,iw] = 1
                    if self.nh == 1 and self.nw == 1 and len(word)==1:
                        return True
                    if ih>0:
                        if self.findExi([ih-1,iw, 1], 1, past):
                            return True
                    if iw>0:
                        if self.findExi([ih, iw-1], 1, past):
                            return True
                    if ih<self.nh-1:
                        if self.findExi([ih+1, iw], 1, past):
                            return True
                    if iw<self.nw-1:
                        if self.findExi([ih, iw+1], 1, past):
                            return True
                    past[ih,iw] = 0
        return False

    def findExi(self, cur_coord, cur_n, cur_map):
        if cur_n >= len(self.word):
            return True
        else:
            ch = cur_coord[0]
            cw = cur_coord[1]

            if self.board[ch][cw] == self.word[cur_n]:
                if cur_n == len(self.word)-1:
                    return True
                cur_map[ch, cw] = 1
                if ch>0 and cur_map[ch-1, cw] == 0:
                    if self.findExi([ch-1, cw], cur_n+1, cur_map):
                        return True
                if cw>0 and cur_map[ch, cw-1] == 0:
                    if self.findExi([ch, cw-1], cur_n+1, cur_map):
                        return True
                if ch<self.nh-1 and cur_map[ch+1, cw]==0:
                    if self.findExi([ch+1, cw], cur_n+1, cur_map):
                        return True
                if cw<self.nw-1 and cur_map[ch, cw+1]==0:
                    if self.findExi([ch, cw+1], cur_n+1, cur_map):
                        return True
                cur_map[ch, cw] = 0


def stringToChar2dArray(input):
    return json.loads(input)


def stringToString(input):
    return input[1:-1].decode('string_escape')


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
            line = sys.stdin.readline().rstrip('\n')
            word = stringToString(line)

            ret = Solution().exist(board, word)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()