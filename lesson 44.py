class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print (self.firstname, self.lastname)

class student(person):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        self.age=age

    def introduce(self):
        print("My name is ",self.firstname,self.lastname,", I'm ", self.age )

x=student("Will","Bayers",10)
x.introduce()
