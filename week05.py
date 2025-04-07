class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


s1 = Stack()
s2 = Stack()
print(s1.is_empty())
s1.push("Data structure")
print(s1.is_empty())
print(s2.is_empty())
s1.push("Database")
print(s1.size())
print(s1.peek())
print(s1.size())
print(s1.pop())
print(s1.size())
print(s1.peek())