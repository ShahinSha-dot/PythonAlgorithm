from empty import Empty

class heap():
    def __init__(self):
        self.maxsize = 10
        self.data = [-1]*self.maxsize
        self.current_size = 0
    
    def _len(self):
        return len(self.data)
    
    def _empty(self):
        return len(self.data) == 0
    
    def max_heap(self):
        if self.current_size == 0:
            raise Empty('list is empty')
        else:
            return self.data[1]
    
    def insert(self, e):
        if self.current_size == self.maxsize:
            raise  Empty('no space')
        else:
           self.current_size += 1
           i = self.current_size
           while i != 1 and e > self.data[i//2]:
                self.data[i] = self.data[i//2]
                i = i//2
           self.data[i] = e
    
    def del_max(self):
            if self.current_size == self.maxsize:
               raise  Empty('no space')
            else:
                y = self.data[self.current_size]
                self.current_size -= 1
                i = 1
                ci =2
                while ci <= self.current_size:
                    if ci < self.current_size and self.data[ci] < self.data[ci+1]:
                        ci += 1
                    if y >= self.data[ci]:
                        break
                    self.data[i] = self.data[ci]
                    i = ci
                    ci *= 2
                self.data[i] = y