"""
List comprehension will create a whole new list
"""
# Generator 
"""
Generator epressions don't materialize the whole output sequence when they're run
It evaluates to an iterator 
"""
it = (len(x) for x in open('tmp/my_file.txt'))
print(it) # <generator object <genexpr> at 0x1098941a8>
print(next(it)) # 5
print(next(it)) # 4
print("========================================================")
print("=======Root of Data=====")
print("========================================================")
roots = ((x, x**0.5) for x in it)
print(next(roots))