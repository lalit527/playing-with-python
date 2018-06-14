from collections import defaultdict
names = ['Socrates', 'Archidedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)

print("========================================================")
print("=======First class Functions=====")
print("========================================================")

def log_missing():
  print('Key Added')
  return 0

current = {'green': 12, 'blue': 3}
increments = [
  ('red', 5),
  ('blue', 17),
  ('orange', 9)
]
result = defaultdict(log_missing, current)
print('Befor:', dict(result))
for key, amount in increments:
  result[key] += amount
print('After:', dict(result))


print("========================================================")
print("=======Functions closures=====")
print("========================================================")
def increment_with_report(current, increments):
  added_count = 0

  def missing():
    nonlocal added_count 
    added_count += 1
    return 0
  
  result = defaultdict(missing, current)
  for key, amount in increments:
    result[key] += amount

  return result, added_count

"""
The problem with defining a closure for stateful hooks is that it’s harder to read than the stateless function example.
"""
class CountMissing:
  def __init__(self):
    self.added = 0
  
  def missing(self):
    self.added += 1
    return 0

"""
1. Instead of defining and instantiating classes, functions are often all you need for simple interfaces between components in Python.
2. References to functions and methods in Python are first class, meaning they can be used in expressions like any other type.
3. The __call__ special method enables instances of a class to be called like plain Python functions.
4. When you need a function to maintain state, consider defining a class that provides the __call__ method instead of defining a stateful closure
"""