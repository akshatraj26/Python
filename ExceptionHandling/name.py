a, b = 10, 20
try:
    c = a/b * d
except Exception as e:
    print("Defined the variable::::",e)
    
else:
    print("No problems")
    
finally:
    print("I will be run every time")