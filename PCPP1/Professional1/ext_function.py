def combiner(a, b, *args, c=60, **kwargs):
    super_combiner(b, a, c, *args, **kwargs)

def super_combiner(*args, **kwargs):
    print('my_args', args)
    print('kw_args', kwargs)

combiner(10, 20, 30, key1=40, key2=50, c=70)