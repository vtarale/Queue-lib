import queue_lib.queue as q

# test
new_q = q.Queue()
print(f"Is the queue empty {new_q.isempty()}")
new_q.add(1)
new_q.add(2)
new_q.add(3)
new_q.add(4)
print(f"Is the queue empty {new_q.isempty()}")
new_q.display()
item = new_q.get()
print(f"Item recived: {item}")
new_q.display()