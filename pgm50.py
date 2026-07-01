class A:
    def displayA(self):
        print("Class A")
class B(A):
    def displayB(self):
        print("Class B")
class C(A):
    def displayC(self):
        print("Class C")
class D(B,C):
    def displayD(self):
        print("Class D")
obj=D()
obj.displayA()
obj.displayB()
obj.displayC()
obj.displayD()