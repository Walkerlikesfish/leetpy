import json

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n_r = len(board)
        n_c = len(board[0])
        # scan the four boarder line to mark all the board-connected 'O' zone
        for ic in range(0, n_c):
            sq = []
            nxt = []
            if board[0][ic] == 'O':
                sq.append((0, ic))
            if board[n_r-1][ic] == 'O':
                sq.append((n_r-1, ic))
            while sq:
                for each_pt in sq:
                    cr = each_pt[0]
                    cc = each_pt[1]
                    board[cr][cc] = 'P'
                    if cr > 1 and board[cr-1][cc] == 'O':
                        nxt.append((cr-1, cc))
                    if cc > 1 and board[cr][cc-1] == 'O':
                        nxt.append((cr, cc-1))
                    if cr < n_r-1 and board[cr+1][cc] == 'O':
                        nxt.append((cr+1, cc))
                    if cc < n_c-1 and board[cr][cc+1] == 'O':
                        nxt.append((cr, cc+1))
                sq = nxt
                nxt = []

        for ir in range(1, n_r-1):
            sq = []
            nxt = []
            if board[ir][0] == 'O':
                sq.append((ir, 0))
            if board[ir][n_c-1] == 'O':
                sq.append((ir, n_c-1))
            while sq:
                for each_pt in sq:
                    cr = each_pt[0]
                    cc = each_pt[1]
                    board[cr][cc] = 'P'
                    if cr > 1 and board[cr - 1][cc] == 'O':
                        nxt.append((cr - 1, cc))
                    if cc > 1 and board[cr][cc - 1] == 'O':
                        nxt.append((cr, cc - 1))
                    if cr < n_r - 1 and board[cr + 1][cc] == 'O':
                        nxt.append((cr + 1, cc))
                    if cc < n_c - 1 and board[cr][cc + 1] == 'O':
                        nxt.append((cr, cc + 1))
                sq = nxt
                nxt = []

        for ir in range(n_r):
            for ic in range(n_c):
                if board[ir][ic] == 'P':
                    board[ir][ic] = 'O'
                elif board[ir][ic] == 'O':
                    board[ir][ic] = 'X'
                else:
                    continue


def stringToChar2dArray(input):
    return json.loads(input)


def char2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            board = stringToChar2dArray(line)

            ret = Solution().solve(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print "Do not return anything, modify board in-place instead."
            else:
                print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()