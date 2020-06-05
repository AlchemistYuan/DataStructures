class DLList:
    class Node:
        def __init__(self, prev, element, next):
            self.prev = prev
            self.element = element
            self.next = next

    def __init__(self, item=None):
        self._sentinel = DLList.Node(self, 0, self)
        if item:
            self._size = 1
            new_node = DLList.Node(self._sentinel, item, self._sentinel)
            self._sentinel.next = new_node
            self._sentinel.prev = new_node
        else:
            self._size = 0

    def __str__(self):
        p = self._sentinel
        string = ''
        for i in range(self._size):
            string  = string + str(p.next.element) + ' '
            p = p.next
        string = string[:-1]
        return string

    def add_first(self, item):
        new_node = DLList.Node(None, item, None)
        self._sentinel.next.prev = new_node
        new_node.next = self._sentinel.next
        self._sentinel.next = new_node
        new_node.prev = self._sentinel
        self._size += 1

    def add_last(self, item):
        new_node = DLList.Node(None, item, None)
        self._sentinel.prev.next = new_node
        new_node.prev = self._sentinel.prev
        self._sentinel.prev = new_node
        new_node.next = self._sentinel
        self._size += 1
    
    def insert(self, item, position):
        p = self._sentinel
        for i in range(position):
            p = p.next
        new_node = DLList.Node(None, item, None)
        new_node.next = p
        new_node.prev = p.prev
        p.prev.next = new_node
        p.prev = new_node
        self._size += 1

    def remove_first(self):
        removed = self._sentinel.next
        removed.next.prev = self._sentinel
        self._sentinel.next = removed.next
        removed.next = null
        self._size -= 1
        return removed.element

    def remove_last(self):
        removed = self._sentinel.prev
        remove.prev.next = self._sentinel
        self._sentinel.prev = removed.prev
        removed.prev = null
        self._size -= 1
        return removed.element

    def get_first(self):
        return self._sentinel.next.element

    def get_last(self):
        return self._sentinel.prev.element

    def get(index):
        p = self._sentinel
        for i in range(index):
            p = p.next
        return p.element
    
    def size(self):
        return self._size

if __name__ == "__main__":
    l = DLList()
    l.add_first(10)
    l.add_first(20)
    l.add_first(30)
    l.add_first(40)

    print(l.size())
    print(l)

