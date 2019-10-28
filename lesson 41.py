'''
class FirstClass:
    x=1

f1= FirstClass()
print(f1.x)
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def func(self):
        print("Hello my name is " + self.name + " I'm " + self.age)

f1=person("Jim Hopper","47")
f1.func()
