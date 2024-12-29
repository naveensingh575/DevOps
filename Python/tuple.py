#we will read about tuples
#tuples are immutable
#tuples are inclosed in ()
#tuples are collection of data types which inclosed in ( ) and seperated by , with ''
#tuples are read only.
print(dir(tuple))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
tuple = ('navi','singh','kumar','ji')
print(tuple.index('navi'))
print(tuple.index('kumar'))
print(tuple.count('navi'))
