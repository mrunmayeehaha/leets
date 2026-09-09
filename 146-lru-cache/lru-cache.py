class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.map:
            return -1

        node = self.map[key]

        self.remove_node(node)
        self.add_node(node)

        return node.value

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value

            self.remove_node(node)
            self.add_node(node)

        else:
            node = Node(key, value)
            self.map[key] = node
            self.add_node(node)

            if len(self.map) > self.capacity:
                lru = self.head.next

                self.remove_node(lru)
                del self.map[lru.key]