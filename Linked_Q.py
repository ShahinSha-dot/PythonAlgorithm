from empty import Empty

class Linkedlist():
    class _node:
        __slots__ = 'element','next'
        def __init__(self,element,next):
            self.element = element
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def _len(self):
        return self._size
    def _is_empty(self):
        return self._size == 0
    
    def enque(self, e):
        NewNode = self._node(e, None)
        if self._is_empty():
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = NewNode
        self.tail = NewNode
        self.size += 1
    
    def deque(self):
        if self._is_empty():
            raise Empty('empty list')
        else:
            value = self.head.element
            self.head = self.head.next
            self.size -= 1
            if self._is_empty():
                self.tail = None
            return value
    
    def first(self):
        if self._is_empty():
            raise Empty('Empty list')
        else:
            val = self.head.element
            return val
    def display(self):
        if self._is_empty():
            raise Empty('Empty list')
        else:
            temp = self.head
            while temp:
                print(temp.element, "--->")
    
   
            
        