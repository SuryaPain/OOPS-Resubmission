#1
class Circle:
    def __init__(self,a):
     self.a=a
    def number(self):
        print(self.a)
p= Circle("10,501,22,37,100,999,87,351")
p.number()
 
 #2
class myClass:
    a=3.141
    def __privMeth(self):
        print("Im inside class myClass")
    def hello(self):
        print("Private Variable value:",myClass.a)
f = myClass()
f.hello()
f.a

#3
class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**3.141
    def perimeter(self):
        return 2*self.radius*3.141
NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())