class Queue:
    def __init__(self):
        self.q = []
    def add(self, item):
        self.q.append(item)
    def get(self):
        item = self.q[0]
        self.q = self.q[1:]
        return item
    def isempty(self):
        if len(self.q) == 0:
            return True
        return False
    def display(self):
        print("items in queue: ", end="")
        for item in self.q:
            print(item, end="  ")
        print("")