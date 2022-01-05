import shelve

dbb = shelve.open('sample.shlv', flag='w')

dbb.close()
