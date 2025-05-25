class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        # If full, ignore push instead of raising error
        if len(self.items) >= self.limit:
            return
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        # Return distance from top of stack (last element), starting at 0
        # If not found, return -1
        if target not in self.items:
            return -1
        # index from bottom
        index_from_bottom = self.items.index(target)
        # distance from top = size - 1 - index_from_bottom
        return len(self.items) - 1 - index_from_bottom
