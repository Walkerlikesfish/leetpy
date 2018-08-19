import json


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie(object):
    def __init__(self):
        self.head = TrieNode()

    def insert_word(self, word):
        cur_ptr = self.head
        for each_c in word:
            if each_c not in cur_ptr.children:
                cur_ptr.children[each_c] = TrieNode()
            cur_ptr = cur_ptr.children[each_c]
        cur_ptr.is_word = True
        cur_ptr.word = word


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        t = Trie()
        self.res = []
        self.board = board
        # init the Trie
        for each_word in words:
            t.insert_word(each_word)

        cur_ptr = t.head
        for ix in xrange(len(board)):
            for iy in xrange(len(board[0])):
                if board[ix][iy] in cur_ptr.children:
                    self.dfs((ix, iy), cur_ptr.children[board[ix][iy]])

        return self.res

    def dfs(self, coord, cur_ptr):
        if cur_ptr.is_word:
            if cur_ptr.word not in self.res:
                self.res.append(cur_ptr.word)
        # check the 4-neighbours of coord, to see if there exists one in the cur_ptr.children
        cx, cy = coord
        # up
        bk = self.board[cx][cy]
        self.board[cx][cy] = 'X'
        if cx-1 > -1 and self.board[cx-1][cy] != 'X':
            tmp = self.board[cx-1][cy]
            if tmp in cur_ptr.children:
                self.dfs((cx-1, cy),cur_ptr.children[tmp])
        if cy-1 > -1 and self.board[cx][cy-1] != 'X':
            tmp = self.board[cx][cy-1]
            if tmp in cur_ptr.children:
                self.dfs((cx, cy-1), cur_ptr.children[tmp])
        if cx+1 < len(self.board) and self.board[cx+1][cy] != 'X':
            tmp = self.board[cx+1][cy]
            if tmp in cur_ptr.children:
                self.dfs((cx+1, cy), cur_ptr.children[tmp])
        if cy+1 < len(self.board[0]) and self.board[cx][cy+1] != 'X':
            tmp = self.board[cx][cy+1]
            if tmp in cur_ptr.children:
                self.dfs((cx, cy+1), cur_ptr.children[tmp])

        self.board[cx][cy] = bk


def stringToChar2dArray(input):
    return json.loads(input)


def stringToStringArray(input):
    return json.loads(input)


def stringArrayToString(input):
    return json.dumps(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = sys.stdin.readline().strip('\n')
            board = stringToChar2dArray(line)
            line = sys.stdin.readline().strip('\n')
            words = stringToStringArray(line)

            ret = Solution().findWords(board, words)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()