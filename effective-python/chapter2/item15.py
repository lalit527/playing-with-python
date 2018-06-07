def sort_priority(values, group):
  def helper(x):
    if x in group:
      return (0, x)
    return (1, x)
  values.sort(key = helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

"""
1. Supports closures
2. functions are first-class object
3. Specific rules for comparing items in tuple.
   It first compares item in index zero, then 1, then 2 so on..
"""

print("========================================================")
print("=======Getting data out of Closure=====")
print("========================================================")

def sort_priority2(numbers, group):
  found = False
  def helper(x):
    if x in group:
      found = True
      return (0, x)
    return (1, x)
  numbers.sort(key=helper)
  return found

found = sort_priority2(numbers, group) 
print('Found:', found) 
print(numbers)

print("========================================================")
print("=======Getting data out of Closure using nonlocal=====")
print("========================================================")
"""
Use special syntax nonlocal to get data out of closure
"""
def sort_priority3(numbers, group):
  found = False
  def helper(x):
    if x in group:
      nonlocal found = True
      return (0, x)
    return (1, x)
  numbers.sort(key=helper)
  return found

found = sort_priority3(numbers, group) 
print('Found:', found) 
print(numbers)


print("========================================================")
print("=======Accept function for simple interface=====")
print("========================================================")
class Sorter:
  def __init__(self, group):
    self.group = group
    self.found = False
  
  def __call__(self, x):
    if x in self.group:
      self.Found = True
      return (0, x)
    return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True