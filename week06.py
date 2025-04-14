from queue import Queue

q = Queue()
q.put("Database")
q.put("Data structure")
q.put("Java script")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
# print(q.size, q.front, q.rear)
# print(q.dequeue())
