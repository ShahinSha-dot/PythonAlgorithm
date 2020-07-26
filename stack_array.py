from empty import Empty

class stack_array():
    def __init__(self):
        self.data = []
    def __len(self):
        return len(self.data)
    def _is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)
    
    def pop(self):
        if self._is_empty():
            raise Empty('this stack is empty')
        else:
            self.data.pop()
    
    def top(self):
        if self._is_empty():
            raise Empty('this stack is empty')
        else:
            return self.data[-1]
        
#test should be done below
s = stack_array()
s.push(10)
s.push(20)
print(s.data)
s.pop()
print(s._is_empty())
s.pop()
print(s._is_empty())
s.pop()
print(s.data)