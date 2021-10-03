
# https://newbedev.com/is-it-possible-to-create-anonymous-objects-in-python


class Anonymous:
    def __init__(self, **kargs) -> None:
        self.__dict__.update(kargs)

def anom(**kargs):
    return type('anonymous', (), kargs)


a = Anonymous(name = 'Fabiano', age = 29)
b = anom(name = 'Fabiano', age = 40)

print('a', a)
print(a.__dict__)

print('b', b)
print(b.__dict__)