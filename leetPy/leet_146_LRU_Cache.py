class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList(object):
    """
    A FIFO list, support two methods:

    - insert: insert on the tail of queue
    - delete: delete a certain node in the queue

    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_dict = {}
        self.node_queue = LinkedList()

    def _insert(self, key, val):
        cur_node = Node(key, val)
        self.node_queue.insert(cur_node)
        self.node_dict[key] = cur_node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.node_dict:
            key_val = self.node_dict[key].val
            self.node_queue.delete(self.node_dict[key])
            self._insert(key, key_val)
            return key_val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.node_dict:
            self.node_queue.delete(self.node_dict[key])
        else:
            if len(self.node_dict) == self.capacity:
                del self.node_dict[self.node_queue.head.key]
                self.node_queue.delete(self.node_queue.head)
        self._insert(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


