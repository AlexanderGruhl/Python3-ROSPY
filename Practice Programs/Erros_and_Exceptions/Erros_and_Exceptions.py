#class B(Exception):
 #   pass

#class C(B):
#    pass

#class D(C):
 #   pass

#for cls in [B, C, D]:
 #   try:
 #       raise cls()
 #   except D:
 #       print("D")
 #   except C:
  #      print("C")
  #  except B:
  #      print("B")

#a_num = 10
#print(dir())

#def some_func():
 #   b_num = 11
#    print(dir())

#some_func()
#print(dir())

class Original:
    def ofunct(self):
        print("Original")

class Base1 (Original):
    def funct1(self):
        print("Base1")

class Base2 (Original):
    def funct2(self):
        print("Base2")

class DerivedClass (Base1, Base2):
    def funct(self):
        print("Derived")

    def call_functs(self):
        print("calling functions")
        self.funct()
        self.funct1()
        self.funct2()
        self.ofunct()

#x = DerivedClass()
#x.funct()
#x.funct1()
#x.funct2()
#x.ofunct()
#x.call_functs()

class Iterate:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index += 1
        return self.data[self.index]

iterate = Iterate('spam')
print(iter(iterate))
for char in iterate:
    print(char)

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

for char in reverse('coom'):
    print(char)

