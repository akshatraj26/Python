class Fruit:
    count = 0
    
    def __init__(self, name= '', size = 0, color = ''):
        self.name = name
        self.size = size
        self.color = color
        Fruit.count += 1
        
    def display():
        print(Fruit.count)
        
        
f1 = Fruit('Banana', 5, 'Yellow')
f2 = Fruit("Apple", 4, 'Red')
f3 = Fruit('Orange', 4, 'Orange')
f3 = Fruit('Orange', 4, 'Orange')
Fruit.display()