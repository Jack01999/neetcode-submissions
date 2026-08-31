class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # { key : Node }
        self.left, self.right = Node(0,0), Node(0,0)
        # Doubly linked-list. Left <--> Right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Init
        prev = node.prev
        nextNode = node.next
        # Setting
        prev.next = nextNode
        nextNode.prev = prev

    def insert(self, node):
        # init
        prev = self.right.prev
        nextNode = self.right
        # Setting
        prev.next = nextNode.prev = node
        node.next = nextNode
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            # Remove node, and put it on the right side (Most recently used)
            self.remove(node)
            self.insert(node)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            # Remove LRU key
            lruKey = self.left.next
            self.remove(lruKey)
            del self.cache[lruKey.key]

        
