"""
Stride:
list[start, end, stride]
"""
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

print("========================================================")
print("=======Reversing a String=====")
print("========================================================")
x = b'mongoose'
y = x[::-1]
print(y)

## This will break for Unicode characters encoded as UTF-8

print("========================================================")
print("=======Negetive Stride=====")
print("========================================================")

a= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])
print(a[::-2])

"""
::2   means select every second item starting at the begining
::-2  means select every second item starting at the end and moving backwards
"""

print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])

"""
Slicing and striding will create extra shallow copy of the data
"""