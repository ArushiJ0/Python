class A:
    def show(self):
        print("A msg")
class B (A):
    def show(self):
        print("B msg")

class C(A):
    def show(self):
        print("C msg")

class D(B,C):
    pass

d =D()
d.show()
