class Node:
    def __init__(self, **keys):
        self.keys = keys
        self.next = None
        
class Things:
    def __init__(self):
        self.head = None
    
    def insert(self, **keys):
        new_node = Node(**keys)
        
        if not self.head:
            self.head = new_node
            
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new_node
            
    def display(self):
        current = self.head
        while current:
            print(f"{current.keys}")
            current = current.next
            
thin = Things()
thin.insert(name = "Vimal", std = 4)
thin.insert(model = "BMW")
thin.display()
        
    