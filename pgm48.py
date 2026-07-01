class Grandfather:
    def property(self):
        print("Grandfather's Property")
class Father(Grandfather):
    pass
class Son(Father):
    pass
s= Son()
s.property()