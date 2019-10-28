'''
class car:
    def __init__(self, name, speed):
        self.name=name
        self.speed=speed

    def func (self):
        print("The car's name is "+self.name)
f1=car("BMW",240)
f1.func()


class car:
    def __init__(self, name, speed):
        self.name=name
        self.speed=speed

    def func (self):
        print("The car's name is "+self.name)
        
f1=car("BMW",240)
f1.speed=230
print(f1.speed)
'''

class car:
    def __init__(self, name, speed):
        self.name=name
        self.speed=speed

    def func (self):
        print("The car's name is "+self.name)
        
f1=car("BMW",240)
'''
del f1.speed
print (f1.speed)
'''

del f1
print(f1)


