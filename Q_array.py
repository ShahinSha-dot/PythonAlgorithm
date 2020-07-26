from empty import Empty

class que():
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0
    def _len_(self):
        return len(self.data)
    def _is_empty(self):
        return self.size == 0
    
    def enque(self, e):
        self.data.append(e)
        self.size+=1
    
    def deque(self):
        if self.size == 0:
            raise Empty("que is empty")
        else:
            value = self.data[self.front]
            self.front += 1
            self.size -= 1
            return value
    def front(self):
        if self.data._is_empty():
            raise Empty("que is empty")
        else:
            return self.data[self.front]

#changes below ///
q = que()
q.enque(10)
print(q)
print(q._is_empty())
print(q._len_())
q.deque()
print(q._is_empty())
print(q._len_())
