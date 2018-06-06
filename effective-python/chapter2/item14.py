print("========================================================")
print("=======Prefer Exception over returning None=====")
print("========================================================")
def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return None
"""
Code using this function can interpret the return value accordingly.
"""
result = divide(x, y) 
if result is None:
  print(‘Invalid inputs’)

print("========================================================")
print("=======Returning False and None as tuple=====")
print("========================================================")
def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return None

_, result = divide(x, y) 
if not result:
  print(‘Invalid inputs’)

"""
Raise error in case of exception rather than returning None
"""
print("========================================================")
print("=======Raise error=====")
print("========================================================")
def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError as e:
    raise ValueError('Invalid inputs') from e

# TO call the function 

x, y = 5, 2 
try:
  result = divide(x, y) 
except ValueError:
  print(‘Invalid inputs’) 
else:
  print(‘Result is %.1f’ % result

"""
Functions that return None to indicate special meaning are error prone because None and 
other values (e.g., zero, the empty string) all evaluate to False in conditional expressions.

Raise exceptions to indicate special situations instead of returning None. 
Expect the calling code to handle exceptions properly when they’re documented.
"""