class _Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def append(self, value):
        new_node = _Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def prepend(self, value):
        new_node = _Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Índice fuera de rango")
        if index == 0:
            self.prepend(value)
            return
        new_node = _Node(value)
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fuera de rango")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fuera de rango")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.value = value

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Índice fuera de rango")
        curr = self.head
        if index == 0:
            removed_value = curr.value
            self.head = curr.next
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            curr = prev.next
            removed_value = curr.value
            prev.next = curr.next
        self.size -= 1
        return removed_value

    def remove_value(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def clear(self):
        self.head = None
        self.size = 0

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next
    def __repr__(self):
        return f"MyLinkedList({self.to_list()})"
