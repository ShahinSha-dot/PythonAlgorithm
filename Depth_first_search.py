class Node():
    def __init__(self,name):
        self.children = []
        self.name = name
        
    def add_child(self, name):
        self.children.append(Node(name))
    def display(self):
        return self.children.name
    
    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        return array
    
#code below

