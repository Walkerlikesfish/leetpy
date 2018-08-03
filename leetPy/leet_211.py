class TNode(object):
    def __init__(self,c):
        self.children = {}
        self.is_word = False
        self.c = c

class Trie(object):
    def __init__(self):
        self.head = TNode()

    def insert_word(self, word):
        cur_ptr = self.head
        for each_c in word:
            if each_c not in cur_ptr.children:
                cur_ptr.children[each_c] = TNode(each_c)
            cur_ptr = cur_ptr.children[each_c]
        cur_ptr.is_word = True

    def search_with_dot(self, word):
        cur_ptr = self.head
        sq_now = []
        sq_nxt = []
        cnt = 0
        # init the sq_now
        for each_child in cur_ptr.children:
            sq_now.append(cur_ptr.children[each_child])
        for each_c in word:
            if each_c == '.':
                for each_ele in sq_now:
                    for each_child in each_ele.children:
                        sq_nxt.append(each_ele.children[each_child])
            else:
                for each_ele in sq_now:
                    if each_ele.c == each_c:
                        for each_child in each_ele.children:
                            sq_nxt.append(each_ele.children[each_child])
            sq_now = sq_nxt
            sq_nxt = []
            cnt += 1
        print cnt, sq_now
        if cnt == len(word) and not sq_now:
            return True
        else:
            return False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.t.insert_word(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.t.search_with_dot(word)



        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)