from empty import Empty

class deque():
    def __init__(self):
        self.data = []
        self.front = 0
    def _len(self):
        return len(self.data)
    def _is_empty(self):
        return len(self.data) == 0
    
    def first(self):
        if self._is_empty():
            raise Empty('the que is empty')
        else:
            return self.data[self.front]
    def add_front(self, e):
            self.data.insert(self.front, e)
    def add_last(self, e):
            self.data.append(e)
    def rem_first(self):
        if self._is_empty():
            raise Empty('the que is empty')
        else:
            self.data.pop(self.front)
    def rem_last(self):
        if self._is_empty():
            raise Empty('the que is empty')
        else:
            self.data.pop()
    
#code below::::
dq = deque()
dq.add_last(10)
dq.add_front(20)
print(dq.data)
