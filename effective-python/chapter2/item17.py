print("========================================================")
print("=======Be Defensive while Iterating over arguments=====")
print("========================================================")
def normalize(number):
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result

print("========================================================")
print("=======Reading data from a file=====")
print("========================================================")
def read_vists(data_path):
  with open(data_path) as f:
    for line in f:
      yield int(line)
    
it = read_vists('tmp/my_numbers.txt')
percentages = normalize(it)
print(percentages)

"""
If you iterate over an iterator or generator that has already raised a StopIteration exception, 
you won’t get any results the second time around.
"""
it = read_visits(‘/tmp/my_numbers.txt’) 
print(list(it)) # [15, 35, 80]
print(list(it)) # [] -- Already exhausted

print("========================================================")
print("=======Explicitly exahausting an input iterator=====")
print("========================================================")
"""
This function copies the array
"""
def normalize_copy(numbers):
  numbers = list(numbers)
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result

it = read_visits(‘/tmp/my_numbers.txt’) 
percentages = normalize_copy(it) 
print(percentages) # [11.538461538461538, 26.923076923076923, 61.53846153846154]


def normalize_func(get_iter):
  total = sum(get_iter())
  result = []
  for value in get_iter():
    percent = 100 * value / total
    result.append(percent)
  return result