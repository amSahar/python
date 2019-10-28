'''
mytuple=("laptop","mobile","tablet")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr="ENGINEERING"
myit=iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple=("laptop","mobile","tablet")
for x in mytuple:
    print(x)

mystr="ENGINEERING"
for x in mystr:
    print(x)

class my_num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1
        return x

myclass = my_num ()
myiter = iter (myclass)

print(next (myiter))
print(next (myiter))
print(next (myiter))
print(next (myiter))
print(next (myiter))
'''
class my_num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myclass = my_num ()
myiter = iter (myclass)

for x in myiter:
    print (x)






