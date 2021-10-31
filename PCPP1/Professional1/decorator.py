from datetime import datetime


def simple_decorator(f):
    print('Hello from decorator.')

    def x(*args, **kwargs):
        print('calling...')
        f(*args, **kwargs)

    return x

@simple_decorator
def sample_fun(x=10):
    print('Hello World!', x)



def logTime(f):
    def time_wrapper(*args, **kwargs):
        print('Calling at', datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        f(*args, **kwargs)
    
    return time_wrapper

@logTime
def say_hello():
    print('Hello world!!!!!')
     
say_hello()

#print(sample_fun.__annotations__)

sample_fun()
sample_fun(11)
sample_fun(11)

say_hello()