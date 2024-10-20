class TreeNode:
    def __init__(self, data = None, address = None, left = None, right = None):
        self.data = data if data != None else ''
        self.address = address
        self.left = left
        self.right = right
    
    def search(self, address):
        if len(address) <= '1':
            return self.data
        elif address[1] == '0':
            return self.left.search(address[1:])
        else:
            return self.right.search(address[1:])

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __str__(self):
        return self.data
        
    def __eq__(self, other):
        return self.data == other.data
    
    def __lt__(self, other):
        return self.data < other.data
    
    def __gt__(self, other):
        return self.data > other.data

    def __le__(self, other):
        return self.data <= other.data
    
    def __ge__(self, other):
        return self.data >= other.data