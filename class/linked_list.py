class Node:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None
        
class Car:
    def __init__(self):
        self.head = None
        
    def insert(self, name, price):
        new_node = Node(name, price)
        if not self.head:
                self.head = new_node
                
        else:
            current  = self.head
            while current.next:
                current = current.next
               
            current.next = new_node
    def display(self):
        current = self.head
        while current:
                print(f"Car: {current.name}, Price: {current.price}")
                current = current.next
            
car_list = Car()
car_list.insert("Toyata", 400000)
car_list.insert("BMW", 354656768)
car_list.insert("Audi", 467788)
car_list.display()