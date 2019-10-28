class Library:
    def __init__(self,book,shelf):
        self.book=book
        self.shelf=shelf

p1= Library("300","45")

print(p1.book,p1.shelf)


class science_section(Library):
    def __init__(self,book,shelf):
        super().__init__(book,shelf)
        self.name="Physics book"

x=science_section("300","45")
x.book=20
x.shelf=4

print(x.book, x.shelf,x.name)

