
class Metadata:
    pass


m = Metadata()
n = type("Dynamic", (), { "x": 1 })

print(m.__class__)
print(type(m) is Metadata)
print(isinstance(m, Metadata))

print(type(n))
print(n.__name__)


class Subclass:
    pass

class SuperClass(Subclass):
    def __init__(self):
        self.x = 0    
    

ss = SuperClass()

print("Superclass is instance of SubClass:", isinstance(ss, Subclass))
print("Superclass is subclass of Subclass:", issubclass(SuperClass, Subclass))
print("Superclass is subclass of Metadata:", issubclass(SuperClass, Metadata))
print(ss)
print("x =", ss.__getattribute__("x"))
print(dir(ss))
#print(dir(SuperClass))
print(SuperClass.__dict__)