
class Metadata:
    pass


m = Metadata()
n = type("Dynamic", (), { "x": 1 })

print(m.__class__)
print(type(m) is Metadata)
print(isinstance(m, Metadata))

print(type(n))
print(n.__name__)


class SuperClass:
    pass

class SubClass(SuperClass):
    def __init__(self):
        self.x = 0    
    

ss = SubClass()
ss2 = SubClass

print("Superclass is instance of SuperClass:", isinstance(ss, SuperClass))
print("Subclass is subclass of Superclass:", issubclass(SubClass, SuperClass))
print("Subclass is subclass of Metadata:", issubclass(SubClass, Metadata))
print("ss = ", ss)
print("ss2 = ", ss2)
print("x =", ss.__getattribute__("x"))
print(dir(ss))
#print(dir(SuperClass))
print(SubClass.__dict__)