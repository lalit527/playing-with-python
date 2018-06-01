a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First Four', a[:4])
print('Last Four', a[-4:])
print('Middle Two', a[3:-3])

# When slicing from the start of a list, you should leave out the zero index to reduce visual noise.

assert a[:5] == a[0:5]

# When slicing to the end of a list, you should leave out the final index because it’s redundant.
assert a[5:] == a[5:len(a)]

"""
Some form of Slicing
"""
print("========================================================")
print("========Some form of slicing=====")
print("========================================================")
print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

print("========================================================")
print("========Slicing deals with start and end index beyond the list=====")
print("========================================================")
first_twenty_items = a[:20]
last_twenty_items = a[-20:]
# Accessing same directly gives index error

print(first_twenty_items)
print(last_twenty_items)

# a[-20] a[20] will give error IndexError

"""
The result of slicing a list is a whole new list
"""
print("========================================================")
print("========Negetive slicing=====")
print("========================================================")
print(a[-1:])
## Below 3 will return all elements in an array
print(a[-0:])
print(a[0:])
print(a[:])